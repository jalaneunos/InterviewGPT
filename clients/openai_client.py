from openai import OpenAI
from models.message import Message
from typing import List


class OpenAIClient:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def chat_completion(self, model: str, messsages: List[Message]) -> str:
        response = self.client.chat.completions.create(
            messages=messsages,
            model=model,
        )
        return response.choices[0].message.content
