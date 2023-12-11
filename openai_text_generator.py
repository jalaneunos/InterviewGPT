from clients.openai_client import OpenAIClient
from models.message import Message
from typing import List


class OpenAITextGenerator:
    def __init__(self, api_key: str, model: str = 'gpt-3.5-turbo') -> None:
        self.openai_client = OpenAIClient(api_key)
        self.model = model

    def get_generated_text(self, messages: List[Message]) -> str:
        """ Returns generated text synchronously """
        return self.openai_client.chat_completion(self.model, messages)

    def stream_generated_text(self, messages: List[Message]) -> str:
        """ Returns a stream of chunks following the Server-sent events standard."""
        for sentence in self.openai_client.stream_chat_completion(self.model, messages):
            yield sentence
