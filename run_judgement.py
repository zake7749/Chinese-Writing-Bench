import fire
from zhiyin.judge import Judge


async def judge(
    prediction_path,
    experiment_name="default_experiment",
    baseline_model_name="gpt_4.1_2025_04_14",
    judge_model_name="o3-2025-04-16",
    api_base="https://api.openai.com/v1",
):        
    try:
        # 1. Initialize the Judge
        # If your API host is not the standard OpenAI endpoint, pass the api_base parameter.
        judge_instance = Judge(
            api_base=api_base,
            judge_model_name=judge_model_name,
        )

        # 2. Run the judging pipeline
        await judge_instance.judge(
            prediction_path=prediction_path,
            baseline_model_name=baseline_model_name,
            experiment_name=experiment_name,
        )

    except (KeyError, ValueError, FileNotFoundError, ConnectionError) as e:
        print(f"An error occurred during execution: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fire.Fire(judge)