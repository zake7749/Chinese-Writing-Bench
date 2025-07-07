import os
import re
import json
import asyncio
from typing import List, Dict, Any

import pandas as pd
from datasets import load_dataset, Dataset, DatasetDict

# Assuming these are your external modules
from zhiyin.judge_template import PairwiseJudgeTemplate
from zhiyin.client import AsyncOpenAIClient


class Judge:
    """
    An evaluator that uses a Large Language Model for pairwise comparison of two model responses.
    """

    def __init__(
        self,
        api_base: str = "https://api.openai.com/v1",
        api_key: str | None = None,
        judge_model_name: str = "o3-2025-04-16",
        benchmark_dataset_path: str = "zake7749/chinese-writing-benchmark",
        max_concurrency: int = 16,
    ) -> None:
        """
        Initializes the Judge instance.

        Args:
            api_base (str): The base URL for the OpenAI-compatible API.
            api_key (str | None): The API key. If None, it's read from the OPENAI_API_KEY environment variable.
            judge_model_name (str): The name of the LLM to use for judging.
            benchmark_dataset_path (str): The path to the benchmark dataset on the Hugging Face Hub.
            max_concurrency (int): The maximum number of concurrent requests to the API.
        """
        self.openai_client = AsyncOpenAIClient(
            api_key=api_key or os.getenv("OPENAI_API_KEY"),
            model=judge_model_name,
            max_concurrency=max_concurrency,
        )

        self.judge_model_name = judge_model_name
        self.benchmark_dataset_path = benchmark_dataset_path
        self.judge_template = PairwiseJudgeTemplate()
        
        self.benchmark: DatasetDict = load_dataset(benchmark_dataset_path)
        self.sampling_params: Dict[str, Any] = self._get_sampling_params()

    def _get_sampling_params(self) -> Dict[str, Any]:
        """Returns specific sampling parameters."""
        # O3 currently does not support temperature=0.
        if self.judge_model_name == "o3-2025-04-16":
            return {"temperature": 1.0}
        return {"temperature": 0.0}

    @staticmethod
    def load_predictions(path: str) -> Dict[str, str]:
        """
        Loads model predictions from a JSON file.
        Expected format is a dictionary where the key is a writing prompt,
        and the value is the assistant_response.
        """
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Prediction file not found: {path}")

    def _build_judge_prompt(
        self, user_prompt: str, baseline_response: str, assistant_response: str
    ) -> str:
        """Builds a single judge prompt using the template."""
        return self.judge_template.template.substitute(
            user_prompt=user_prompt,
            baseline_response=baseline_response,
            assistant_response=assistant_response,
        )

    def _parse_raw_judgement(self, raw: str) -> Dict[str, Any] | None:
        """
        Parses the JSON judgement block from the judge model's raw response.

        Args:
            raw (str): The raw text response from the judge model.

        Returns:
            Dict[str, Any] | None: The parsed JSON object, or None if parsing fails.
        """
        pat = r"\[START_OF_JUDGEMENT\]\s*(\{.*?\})\s*\[END_OF_JUDGEMENT\]"
        m = re.search(pat, raw, re.DOTALL)
        if not m:
            print(f"Warning: Could not find a valid judgement block in the response.\nRaw response: {raw[:500]}...")
            return None
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            print(f"Warning: JSON parsing failed.\nData: {m.group(1)}")
            return None

    def _add_judgement_scores(self, judgement_df: pd.DataFrame):
        """Extract the judgement score from the judge result."""
        def get_score(judgement, criterion):
            if pd.isna(judgement) or not isinstance(judgement, dict):
                return None # Note: early-failed for non-guided decoding cases?
            return judgement.get(criterion, {}).get('score')
    
        for c in self.judge_template.criteria:
            judgement_df[f'{c}_score'] = judgement_df['judgement'].apply(lambda j: get_score(j, c))

    async def _llm_infer(self, judge_prompts: List[str]) -> List[str]:
        """Executes LLM inference asynchronously in batches."""
        return await self.openai_client.chat_batch(judge_prompts, **self.sampling_params)
        
    async def judge(
        self,
        prediction_path: str,
        baseline_model_name: str,
        experiment_name: str = "default_experiment",
        output_dir: str = "judgements",
        strip_think: bool = True,
    ) -> None:
        """
        Executes the full judging pipeline.

        Args:
            prediction_path (str): Path to the JSON file of the assistant model's predictions.
            baseline_model_name (str): The baseline model name to use from the benchmark dataset (split name).
            experiment_name (str): The name for the output CSV file (without extension).
            strip_think (bool): Flag to determine if skip the content within <think>...</think> for reasoning models.

        Raises:
            ValueError: If the predictions do not fully match the prompts in the benchmark dataset.
        """
        if baseline_model_name not in self.benchmark.keys():
            raise KeyError(
                f"Specified baseline model '{baseline_model_name}' does not exist in dataset '{self.benchmark_dataset_path}'. "
                f"Available options: {list(self.benchmark.keys())}"
            )

        # Load the predictions of the model to be evaluated
        prompt2resp = self.load_predictions(prediction_path)
        if strip_think:
            prompt2resp = {k: v.split("</think>")[-1].strip() for k, v in prompt2resp.items()}

        # Prepare the judgement dataframe
        df = self.benchmark[baseline_model_name].to_pandas()
        df["assistant_response"] = df["prompt"].map(prompt2resp)

        if df["assistant_response"].isna().any():
            missing_count = df["assistant_response"].isna().sum()
            raise ValueError(
                f"{missing_count} prompts could not find a corresponding response in the prediction file. "
            )

        # Build the judge prompts
        df["judge_prompt"] = df.apply(
            lambda r: self._build_judge_prompt(
                user_prompt=r["prompt"],
                baseline_response=r["response"],
                assistant_response=r["assistant_response"],
            ),
            axis=1,
        )

        # Apply asynchronous judging
        raw_judgements = await self._llm_infer(df["judge_prompt"].tolist())
        df["raw_judgement"] = raw_judgements
        
        # Parse the judgements
        df["judgement"] = df["raw_judgement"].apply(self._parse_raw_judgement)

        # Extract the detailed judgement.
        self._add_judgement_scores(df)

        # Save the results
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        output_path = os.path.join(output_dir, f"{experiment_name}.csv")
        df.to_csv(output_path, index=False,)
        
        print(f"Judging complete! Results have been saved to {output_path}")