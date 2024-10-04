import subprocess
from config import Config

class StreamCapture:
    def __init__(self):
        self.stream_url = Config.STREAM_URL

    def capture_audio(self, output_file):
        # Use Streamlink to capture audio from the live stream
        command = [
            'streamlink', self.stream_url, 'best',
            '--stdout', '|', 'ffmpeg', '-i', '-', '-f', 'mp3', '-ab', '192000', '-vn', output_file
        ]
        subprocess.run(command, shell=True, check=True)
