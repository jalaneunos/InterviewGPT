from clients.openai_client import OpenAIClient


class OpenAISpeechToText:
    def __init__(self, api_key: str, model: str = "whisper-1"):
        self.openai_client = OpenAIClient(api_key)
        self.model = model

    def convert_speech_to_text(self, filepath: str) -> str:
        return self.openai_client.speech_to_text(self.model, filepath).text
