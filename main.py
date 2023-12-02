import os
from openai_text_generator import OpenAITextGenerator
from conversation import Conversation


def main():
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    text_generator = OpenAITextGenerator(OPENAI_API_KEY)

    conversation = Conversation()

    while True:
        user_input = input('Prompt: ')

        if user_input.lower() == 'end':
            print("Shutting down.")
            break

        conversation.add_user_message(user_input)

        generated_text = text_generator.get_text(
            conversation.get_conversation())
        conversation.add_assistant_message(generated_text)
        print(conversation.get_conversation())


if __name__ == "__main__":
    main()
