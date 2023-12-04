from openai import OpenAI
from pathlib import Path
from models.message import Message
from typing import List


class OpenAIClient:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def chat_completion(self, model: str, messsages: List[Message]) -> str:
        response = self.client.chat.completions.create(
            messages=messsages,
            model=model,
            max_tokens=256
        )
        return response.choices[0].message.content

    def text_to_speech(self, model: str, text: str, output_filename: str) -> str:
        current_path = Path(__file__).parent
        audio_dir_path = current_path.parent / 'audio'
        speech_file_path = audio_dir_path / output_filename
        response = self.client.audio.speech.create(
            model=model,
            voice="alloy",
            input=text
        )
        response.stream_to_file(speech_file_path)
        return speech_file_path

    def speech_to_text(self, model: str, filepath: str):
        audio_file = open(filepath, "rb")
        transcript = self.client.audio.transcriptions.create(
            model=model,
            file=audio_file,
            language="en"
        )
        return transcript
