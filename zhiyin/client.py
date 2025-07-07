from __future__ import annotations

import asyncio
import os
from typing import Any, Dict, List

import backoff
from openai import AsyncOpenAI
from openai._exceptions import (
    APIError,
    RateLimitError,
    APITimeoutError,
)

from tqdm import tqdm


Message = Dict[str, str]


class AsyncOpenAIClient:
    """Wrapper around OpenAI Chat Completions for asynchronous usage."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gpt-4o-2024-05-13",
        max_concurrency: int = 16,
    ) -> None:
        self._client = AsyncOpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self._model = model
        self._semaphore = asyncio.Semaphore(max_concurrency)


    @backoff.on_exception(
        backoff.expo,
        (RateLimitError, APITimeoutError, APIError),
        max_tries=5,
        jitter=backoff.full_jitter,
    )
    async def _chat_single(self, *, messages: List[Message], **kwargs: Any) -> str:
        """
        Send a single chat completion request with automatic exponential back-off.
        """
        # Concurrency guard
        async with self._semaphore:
            resp = await self._client.chat.completions.create(
                model=self._model,
                messages=messages,
                **kwargs,
            )
        return resp.choices[0].message.content  # type: ignore[attr-defined]
    
    async def chat_batch(self, prompts: List[str], **kwargs: Any) -> List[str]:
        async def _run(i: int, prompt: str):
            msg = [{"role": "user", "content": prompt}]
            content = await self._chat_single(messages=msg, **kwargs)
            return i, content

        # Maintain the idx and task for llm-inference,
        # to keep the results follow the same order as prompts.
        tasks = [asyncio.create_task(_run(i, p)) for i, p in enumerate(prompts)]
        results: List[str | None] = [None] * len(prompts)
    
        for fut in tqdm(asyncio.as_completed(tasks),
                        total=len(tasks),
                        desc="Processing Prompts"):
            idx, content = await fut
            results[idx] = content
    
        return results  # type: ignore

    
    async def __aenter__(self) -> "AsyncOpenAIClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # noqa: D401
        await self._client.close()


if __name__ == "__main__":
    async def test() -> None:
        # A list of independent user prompts to be processed in a batch.
        user_prompts = [
            "Say hello.",
            "Tell me a joke about computers.",
            "What is the capital of France?",
            "Write a short poem about the sea.",
            "Say three words",
            "What is the square root of 144? Just give me a number",
            "Say a random word.",
        ]

        async with AsyncOpenAIClient(max_concurrency=3) as client:
            answers = await client.chat_batch(user_prompts, temperature=1.0)
            
            print("\n--- All tasks completed. Final results:")
            for i, ans in enumerate(answers):
                print(f"Prompt {i+1}: {user_prompts[i]}")
                print(f"Answer {i+1}: {ans}")
                print("-" * 30)

    asyncio.run(test())