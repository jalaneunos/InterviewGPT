import os

from audio_recorder import AudioRecorder
from audio_player import AudioPlayer
from openai_speech_to_text import OpenAISpeechToText
from openai_text_generator import OpenAITextGenerator
from openai_text_to_speech import OpenAITextToSpeech
from conversation import Conversation


def main():

    openai_api_key = os.environ.get("OPENAI_API_KEY")

    audio_recorder = AudioRecorder()

    audio_recorder.set_input_device()

    speech_to_text = OpenAISpeechToText(openai_api_key)

    text_generator = OpenAITextGenerator(openai_api_key)

    text_to_speech = OpenAITextToSpeech(openai_api_key)

    audio_player = AudioPlayer()

    conversation = Conversation()

    while True:

        path_to_input_file = audio_recorder.record_user_input()

        transcribed_input = speech_to_text.convert_speech_to_text(
            path_to_input_file)

        conversation.add_user_message(transcribed_input)

        generated_text = text_generator.get_text(
            conversation.get_conversation())

        speech_file_path = text_to_speech.convert_text_to_speech(
            generated_text)
        audio_player.play_audio(speech_file_path)

        conversation.add_assistant_message(generated_text)


if __name__ == "__main__":
    main()
