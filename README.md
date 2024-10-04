
## Technical Architecture

### 1. Web Scraping / Stream Detection (Scrapy)
- Periodically checks the target website for live streams
- Uses custom CSS selectors to identify when a stream goes live
- Extracts the stream URL for further processing

### 2. Notification System (Email)
- Sends instant email notifications when a live stream is detected
- Includes stream URL and other relevant information in the notification

### 3. Stream Capture (Streamlink)
- Connects to the detected live stream
- Extracts the audio stream for transcription

### 4. Speech-to-Text Conversion (Deepgram)
- Processes the audio stream in real-time
- Converts speech to text with high accuracy
- Handles various accents and languages

### 5. Transcript Storage (Amazon S3)
- Securely stores the generated transcripts
- Organizes transcripts with appropriate metadata (e.g., date, stream title)
- Allows easy retrieval and management of stored transcripts

## Implementation Details

### Technologies Used
- Python 3.8+
- Scrapy for web scraping
- SMTP library for email notifications
- Streamlink for stream capture
- Deepgram SDK for speech-to-text conversion
- Boto3 (AWS SDK for Python) for S3 interaction

### Key Components

1. **LiveStreamSpider (Scrapy Spider)**
   - Customizable start URLs and CSS selectors
   - Implements the core logic for stream detection

2. **Email Notification Module**
   - Configurable sender and receiver email addresses
   - Uses SMTP for reliable email delivery

3. **Stream Capture Module**
   - Utilizes Streamlink to handle various streaming protocols
   - Extracts audio from the captured stream

4. **Transcription Module**
   - Interfaces with Deepgram's API for real-time transcription
   - Handles chunked audio processing for long streams

5. **S3 Storage Module**
   - Manages connections to Amazon S3
   - Implements error handling and retry logic for robust storage
