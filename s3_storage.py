import boto3
from botocore.exceptions import BotoCoreError, ClientError
import logging
from config import Config

class S3Storage:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.bucket_name = Config.S3_BUCKET_NAME

    def store_transcript(self, file_name, transcript, metadata):
        try:
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=transcript,
                Metadata=metadata
            )
            logging.info(f"Transcript stored successfully: {file_name}")
        except (BotoCoreError, ClientError) as error:
            logging.error(f"Failed to store transcript: {error}")
            # Implement retry logic if needed

    def retrieve_transcript(self, file_name):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)
            transcript = response['Body'].read().decode('utf-8')
            metadata = response['Metadata']
            return transcript, metadata
        except (BotoCoreError, ClientError) as error:
            logging.error(f"Failed to retrieve transcript: {error}")
            return None, None

    def list_transcripts(self, prefix=''):
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
            return [obj['Key'] for obj in response.get('Contents', [])]
        except (BotoCoreError, ClientError) as error:
            logging.error(f"Failed to list transcripts: {error}")
            return []

    def delete_transcript(self, file_name):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=file_name)
            logging.info(f"Transcript deleted successfully: {file_name}")
        except (BotoCoreError, ClientError) as error:
            logging.error(f"Failed to delete transcript: {error}")
