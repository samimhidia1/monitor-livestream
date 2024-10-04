from fastapi import FastAPI, HTTPException
from livestream_spider import LiveStreamSpider
from notification_module import EmailNotifier
from stream_capture import StreamCapture
from transcription_module import TranscriptionModule
from s3_storage import S3Storage
import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config
from pydantic import BaseModel
from typing import List

app = FastAPI()

class KeywordUpdate(BaseModel):
    keywords: List[str]

class WebpageURL(BaseModel):
    url: str

@app.post("/set_webpage_url")
async def set_webpage_url(webpage_url: WebpageURL):
    Config.STREAM_URL = webpage_url.url
    return {"status": "Webpage URL updated successfully"}

@app.post("/update_keywords")
async def update_keywords(keyword_update: KeywordUpdate):
    conn = psycopg2.connect(Config.DATABASE_URL)
    try:
        with conn.cursor() as cur:
            # Clear existing keywords
            cur.execute("DELETE FROM keywords")
            # Insert new keywords
            for keyword in keyword_update.keywords:
                cur.execute("INSERT INTO keywords (word) VALUES (%s)", (keyword,))
        conn.commit()
        return {"status": "Keywords updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/start")
async def start_capture():
    # Initialize modules
    notifier = EmailNotifier()
    capture = StreamCapture()
    transcriber = TranscriptionModule()
    storage = S3Storage()

    # Example usage
    stream_info = {'title': 'Example Stream', 'url': 'http://example.com/stream'}
    notifier.send_notification(stream_info)
    capture.capture_audio('output.mp3')
    transcript = await transcriber.transcribe_audio('output.mp3')
    storage.store_transcript('example_transcript.txt', transcript, {'title': stream_info['title']})

    return {"status": "Capture started"}

@app.get("/alerts")
async def get_alerts():
    conn = psycopg2.connect(Config.DATABASE_URL)
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT s.title as stream_title, k.word as keyword, a.timestamp
                FROM alerts a
                JOIN streams s ON a.stream_id = s.id
                JOIN keywords k ON a.keyword_id = k.id
                ORDER BY s.title, a.timestamp
            """)
            alerts = cur.fetchall()

        # Group alerts by stream
        alert_data = {}
        for alert in alerts:
            stream_title = alert['stream_title']
            if stream_title not in alert_data:
                alert_data[stream_title] = []
            alert_data[stream_title].append({
                'keyword': alert['keyword'],
                'timestamp': alert['timestamp'].isoformat()
            })

        return alert_data
    finally:
        conn.close()
