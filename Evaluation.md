# Evaluation Guide

This guide outlines the two-step process for benchmarking your model's performance.

### Prerequisites

  - Python 3
  - Prepare the evaluation scripts: `git clone https://github.com/zake7749/Chinese-Writing-Bench.git`
  - Prepare the environment: `pip instrall -r requirements.txt`
  - An OpenAI API Key for O3 judge.

----

### Step 1: Generate Predictions

First, run your model against the prompts from the benchmark dataset and save the outputs to a JSON file.

The following is a sample script. You must implement the `infer(prompt)` function with your model's inference logic.

```python
import json
from datasets import load_dataset

# 1. Load the benchmark dataset.
ds = load_dataset("zake7749/chinese-writing-benchmark", split="gpt_4.1_2025_04_14")
prompt_to_response = {}

# 2. TODO: Implement your model's inference logic here.
def infer(prompt: str) -> str:
    # Replace this with your actual model inference call.
    response = f"This is a sample response for the prompt: {prompt}"
    return response

# 3. Generate a response for each prompt.
for prompt in ds['prompt']:
    prompt_to_response[prompt] = infer(prompt)

# 4. Save the results to a file.
with open("your_path_to_output.json", "w") as handle:
    json.dump(prompt_to_response, handle)
```

-----

### Step 2: Apply Judgement

Next, use the `run_judgement.py` script to evaluate the predictions generated in the previous step.

Run the following command in your terminal, replacing the placeholders with your information.

```bash
# Set necessary environment variables and file paths
EXPERIMENT_NAME=sample_experiment
PREDICTION_FILE_PATH=your_path_to_output.json

# Run the judgement script
OPENAI_API_KEY="YOUR_OPENAI_API_KEY" python3 run_judgement.py $PREDICTION_FILE_PATH $EXPERIMENT_NAME
```

  - `PREDICTION_FILE_PATH`: The path to the JSON file you created in Step 1.
  - `EXPERIMENT_NAME`: A name for your evaluation run.
  - `YOUR_OPENAI_API_KEY`: Your secret key from OpenAI.

The judgement results will be saved in the `judgement/${EXPERIMENT_NAME}` directory.