#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/home/ubuntu/livestream_transcript_capture
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
