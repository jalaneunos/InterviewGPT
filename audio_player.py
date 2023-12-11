import subprocess
from pathlib import Path
import time
import os


class AudioPlayer:
    def __init__(self, player="mpg123"):
        self.player = player
        self.current_process = None

    def play_audio(self, file_path):
        if not Path(file_path).is_file():
            print("Audio file does not exist.")
            return

        # Wait for the current audio to finish if it's playing
        while self.current_process and self.current_process.poll() is None:
            time.sleep(0.1)

        try:
            self.current_process = subprocess.Popen([self.player, "-q", str(file_path)])
            self.wait_and_delete(file_path)
        except FileNotFoundError:
            print(f"{self.player} is not installed or not found in the system path.")

    def wait_for_last(self):
        # Wait for the last audio file to finish playing
        if self.current_process:
            self.current_process.wait()

    def wait_and_delete(self, file_path):
        if self.current_process:
            self.current_process.wait()

        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting file {file_path}: {e}")
