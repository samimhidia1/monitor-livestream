import asyncio
from livestream_spider import LiveStreamSpider
from notification_module import EmailNotifier
from stream_capture import StreamCapture
from transcription_module import TranscriptionModule
from s3_storage import S3Storage

def main():
    # Initialize modules
    notifier = EmailNotifier()
    capture = StreamCapture()
    transcriber = TranscriptionModule()
    storage = S3Storage()

    # Example usage
    stream_info = {'title': 'Example Stream', 'url': 'http://example.com/stream'}
    notifier.send_notification(stream_info)
    capture.capture_audio('output.mp3')
    transcript = asyncio.run(transcriber.transcribe_audio('output.mp3'))
    storage.store_transcript('example_transcript.txt', transcript, {'title': stream_info['title']})

if __name__ == "__main__":
    main()
