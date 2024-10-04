#!/bin/bash
# Script to check if the stream is live every minute
# Log the status and trigger capture if live

LOG_FILE="/home/ubuntu/livestream_transcript_capture/stream_check.log"
STREAM_URL=$(cat /home/ubuntu/livestream_transcript_capture/config.py | grep STREAM_URL | cut -d "'" -f 2)
CAPTURE_SCRIPT="/home/ubuntu/livestream_transcript_capture/main.py"

echo "$(date): Checking stream status..." >> $LOG_FILE

# Function to check if stream is live
check_stream() {
    # Use streamlink to check if the stream is available
    if streamlink --stream-url $STREAM_URL > /dev/null 2>&1; then
        echo "Stream is live"
        return 0
    else
        echo "Stream is not live"
        return 1
    fi
}

# Check if stream is live
if check_stream; then
    echo "$(date): Stream is live. Triggering capture process." >> $LOG_FILE
    python3 $CAPTURE_SCRIPT
else
    echo "$(date): Stream is not live." >> $LOG_FILE
fi

# To run this script every minute, add the following line to crontab:
# * * * * * /bin/bash /home/ubuntu/livestream_transcript_capture/check_stream.sh
