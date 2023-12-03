import wave
import pyaudio
from pydub import AudioSegment


class AudioRecorder:
    def __init__(self, filename="audio/input.wav", chunk=1024, audio_format=pyaudio.paInt16, channels=1, rate=44100, record_seconds=20, device_index=0):
        self.filename = filename
        self.chunk = chunk
        self.format = audio_format
        self.channels = channels
        self.rate = rate
        self.record_seconds = record_seconds
        self.device_index = device_index
        self._initialize_audio()

    def _initialize_audio(self):
        self.audio = pyaudio.PyAudio()

    def list_input_devices(self):
        info = self.audio.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')

        print("Available input devices:")
        for i in range(0, num_devices):
            if self.audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
                print(
                    f"Device ID {i} - {self.audio.get_device_info_by_host_api_device_index(0, i).get('name')}")

    def set_input_device(self):
        self.list_input_devices()
        chosen_device_index = input(
            "Enter the ID of the desired input device: ")
        try:
            chosen_device_index = int(chosen_device_index)
            self.device_index = chosen_device_index
        except ValueError:
            print("Invalid input. Please enter a device ID number.")

    def record_user_input(self) -> None:
        frames = self.get_frames()
        self.save(frames)

        return self.filename

    def get_frames(self):
        stream = self.audio.open(format=self.format, channels=self.channels,
                                 rate=self.rate, input=True, frames_per_buffer=self.chunk, input_device_index=self.device_index)
        print("Recording...")
        frames = []

        try:
            for _ in range(int(self.rate / self.chunk * self.record_seconds)):
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            print("\nRecording interrupted. Stopping early...")
        finally:
            print("Finished recording.")

            stream.stop_stream()
            stream.close()
            self.audio.terminate()
            self._initialize_audio()  # Create new pyaudio instance

        return frames

    def save(self, frames):
        wave_file = wave.open(self.filename.replace('.mp3', '.wav'), 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(self.format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

        # Convert to MP3
        # sound = AudioSegment.from_wav(self.filename.replace('.mp3', '.wav'))
        # sound.export(self.filename, format="mp3")
        # print(f"File saved as {self.filename}")
