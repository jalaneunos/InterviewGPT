import os
from audio_player import AudioPlayer
from openai_text_generator import OpenAITextGenerator
from openai_text_to_speech import OpenAITextToSpeech
from conversation import Conversation


def main():
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    text_generator = OpenAITextGenerator(OPENAI_API_KEY)

    text_to_speech = OpenAITextToSpeech(OPENAI_API_KEY)

    audio_player = AudioPlayer()

    conversation = Conversation()

    while True:
        user_input = input('Prompt: ')

        if user_input.lower() == 'end':
            print("Shutting down.")
            break

        conversation.add_user_message(user_input)

        generated_text = text_generator.get_text(
            conversation.get_conversation())

        speech_file_path = text_to_speech.convert_text_to_speech(
            generated_text)
        audio_player.play_audio(speech_file_path)

        conversation.add_assistant_message(generated_text)


if __name__ == "__main__":
    main()
