from clients.openai_client import OpenAIClient


class OpenAITextToSpeech:
    def __init__(self, api_key: str, model: str = "tts-1"):
        self.openai_client = OpenAIClient(api_key)
        self.model = model

    def convert_text_to_speech(self, text: str) -> str:
        return self.openai_client.text_to_speech(self.model, text)
