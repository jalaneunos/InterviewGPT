import os
from audio_recorder import AudioRecorder
from audio_player import AudioPlayer
from openai_speech_to_text import OpenAISpeechToText
from openai_text_generator import OpenAITextGenerator
from openai_text_to_speech import OpenAITextToSpeech
from message_log import MessageLog
from chat import Chat


def main():
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    audio_recorder = AudioRecorder()

    audio_recorder.setup_input_device()

    speech_to_text = OpenAISpeechToText(openai_api_key)

    chat_completion = OpenAITextGenerator(openai_api_key)

    text_to_speech = OpenAITextToSpeech(openai_api_key)

    audio_player = AudioPlayer()

    message_log = MessageLog()

    chat = Chat(audio_recorder, speech_to_text, chat_completion, text_to_speech, audio_player, message_log)

    chat.start_conversation()


if __name__ == "__main__":
    main()
