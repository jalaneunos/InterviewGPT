from audio_recorder import AudioRecorder
from openai_speech_to_text import OpenAISpeechToText
from openai_text_generator import OpenAITextGenerator
from openai_text_to_speech import OpenAITextToSpeech
from audio_player import AudioPlayer
from message_log import MessageLog

import time


class Chat:
    """ Controls the flow of the chat between the user and assistant """

    def __init__(self, audio_recorder: AudioRecorder, speech_to_text: OpenAISpeechToText,
                 chat_completion: OpenAITextGenerator, text_to_speech: OpenAITextToSpeech, audio_player: AudioPlayer,
                 message_log: MessageLog):
        self.audio_recorder = audio_recorder
        self.speech_to_text = speech_to_text
        self.chat_completion = chat_completion
        self.text_to_speech = text_to_speech
        self.audio_player = audio_player
        self.message_log = message_log

    def start_conversation(self):
        """ Starts conversation between user and assistant """
        try:
            while True:
                path_to_input_file = self.audio_recorder.record_user_input()

                transcribed_input = self.speech_to_text.convert_speech_to_text(path_to_input_file)

                print("User input: ", transcribed_input)

                self.message_log.add_user_message(transcribed_input)

                generated_response = self.chat_completion.get_text(self.message_log.get_message_log())

                speech_file_path = self.text_to_speech.convert_text_to_speech(generated_response)

                print("Assistant's reponse: ", generated_response)

                self.audio_player.play_audio(speech_file_path)

                self.message_log.add_assistant_message(generated_response)
        except KeyboardInterrupt:
            print()
