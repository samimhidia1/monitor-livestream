from deepgram import Deepgram, DeepgramClient, PrerecordedOptions
import asyncio
from config import Config
import re
from datetime import datetime

class TranscriptionModule:
    def __init__(self):
        self.deepgram = DeepgramClient(Config.DEEPGRAM_API_KEY)

    async def transcribe_audio(self, audio_source, keywords):
        # Use Deepgram's API for real-time transcription
        options = PrerecordedOptions(
            punctuate=True,
            language='en-US'  # Adjust language as needed
        )
        with open(audio_source, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/wav'}
            response = await self.deepgram.transcription.prerecorded(source, options)

        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']

        # Detect keywords and record timestamps
        alerts = []
        for word in keywords:
            for match in re.finditer(r'\b' + re.escape(word) + r'\b', transcript):
                alerts.append({'keyword': word, 'timestamp': datetime.now()})

        return transcript, alerts
