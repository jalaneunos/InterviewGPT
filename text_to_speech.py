from openai import OpenAI
from pathlib import Path
client = OpenAI(api_key=OPENAI_API_KEY)


speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=chat_completion.choices[0].message.content
)

response.stream_to_file(speech_file_path)
