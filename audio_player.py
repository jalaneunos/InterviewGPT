import subprocess
from pathlib import Path


class AudioPlayer:
    def __init__(self, player="mpg123"):
        self.player = player

    def play_audio(self, file_path):
        if not Path(file_path).is_file():
            print("Audio file does not exist.")
            return
        try:
            subprocess.run([self.player, str(file_path)], check=True)
        except subprocess.CalledProcessError:
            print("Error occurred while playing the audio file.")
        except FileNotFoundError:
            print(
                f"{self.player} is not installed or not found in the system path.")
