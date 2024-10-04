
# Live Stream Transcript Capture Project

## Project Overview

This project aims to automatically detect live streams on a specified website, capture the audio, transcribe it in real-time, and store the transcript for later use. The system is designed to be modular, scalable, and easily adaptable to different streaming platforms.

## Key Features

1. Automated live stream detection
2. Real-time notification system
3. Stream capture and audio extraction
4. Speech-to-text transcription
5. Secure transcript storage

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

## Setup and Configuration

1. **Environment Setup**
   - Install Python 3.8+ and PostgreSQL
   - Create a virtual environment and activate it
   - Install required packages via `pip install -r requirements.txt`

2. **Configuration File (.env)**
   - Set API keys and credentials
   - Configure email settings
   - Provide S3 bucket information

3. **Customization**
   - Update website-specific selectors in the Scrapy spider
   - Adjust transcription settings (language, model, etc.)
   - Define storage naming conventions and organization

## Usage

1. **Running the Application**:
   - Use Docker to build and run the application
   - Access the frontend UI to configure and monitor streams

2. **Monitoring and Alerts**:
   - Set keywords to monitor in the transcript
   - View alerts and transcript details on the dashboard

3. **Automatic Capture**:
   - The system automatically starts capturing when a stream goes live

## Deployment

- Deploy on a cloud server (e.g., AWS EC2) for 24/7 operation
- Use Docker for containerization and easy deployment
- Schedule execution using cron jobs or a task scheduler

## Future Enhancements

1. Support for multiple streaming platforms
2. Advanced text analysis of transcripts (e.g., sentiment analysis, keyword extraction)
3. Integration with a database for better transcript management and searching
4. Web interface for monitoring and managing the system
5. Real-time subtitle generation for live streams

## Challenges and Considerations

- Handling changes in website structure (requires regular maintenance of selectors)
- Managing long-running streams and large audio files
- Ensuring high availability and fault tolerance
- Compliance with streaming platform terms of service and copyright considerations
- Optimizing resource usage and costs, especially for cloud-based deployments

## Conclusion

This Live Stream Transcript Capture Project provides a robust solution for automatically detecting, capturing, and transcribing live streams. Its modular design allows for easy customization and expansion, making it adaptable to various use cases and platforms. By leveraging modern technologies and cloud services, it offers a scalable and efficient way to generate and manage transcripts from live content.
