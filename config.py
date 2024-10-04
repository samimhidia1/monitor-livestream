import os

class Config:
    STREAM_URL = os.getenv('STREAM_URL', 'http://example.com/livestreams')
    HTML_ELEMENT = os.getenv('HTML_ELEMENT', 'div.live-stream')
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'livestream.capture.test@gmail.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'abcd efgh ijkl mnop')
    SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'sender@example.com')
    RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL', 'receiver@example.com')
    DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY', 'your_deepgram_api_key')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'your_s3_bucket_name')
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:new_password@localhost/postgres')
