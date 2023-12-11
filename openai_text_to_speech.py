from clients.openai_client import OpenAIClient


class OpenAITextToSpeech:
    def __init__(self, api_key: str, model: str = "tts-1", output_filename='output.mp3'):
        self.openai_client = OpenAIClient(api_key)
        self.model = model
        self.output_filename = output_filename

    def convert_text_to_speech(self, text: str, output_filename) -> str:
        return self.openai_client.text_to_speech(self.model, text, output_filename)
