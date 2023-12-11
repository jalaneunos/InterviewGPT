from openai import OpenAI
from pathlib import Path
from models.message import Message
from typing import List


class OpenAIClient:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key=api_key)

    def chat_completion(self, model: str, messsages: List[Message]) -> str:
        """ Gets generated text synchronously """
        response = self.client.chat.completions.create(
            messages=messsages,
            model=model,
            max_tokens=256,
        )
        return response

    def stream_chat_completion(self, model: str, messsages: List[Message]) -> str:
        """ returns a stream of chunks """
        response = self.client.chat.completions.create(
            messages=messsages,
            model=model,
            max_tokens=256,
            stream=True
        )
        current_sentence = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                if any(char in content for char in ['.', '?', '!']):
                    yield current_sentence
                    current_sentence = ""
                else:
                    current_sentence += content

        if current_sentence.strip().isalnum():  # Yield any remaining incomplete sentence
            yield current_sentence

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
