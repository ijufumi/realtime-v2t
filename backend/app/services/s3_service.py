import boto3
import os
from datetime import datetime
from pathlib import Path

from app.config import Config


class S3Service:
    def __init__(self):
        self.client = boto3.client('s3',
                                   aws_access_key_id=Config.AWS_KEY,
                                   aws_secret_access_key=Config.AWS_SECRET,
                                   region_name=Config.AWS_REGION)

    def upload(self, path: Path) -> str:
        key = os.path.join(datetime.utcnow().strftime("%Y%m%d-%H%M%S"), path.name)
        self.client.upload_file(File=str(path.resolve()),
                                Bucket=Config.AWS_S3_BUCKET,
                                Key=key,
                                ExtraArgs={'ContentType': 'audio/wav'})
        return key

    def get_pre_signed_url(self, key: str) -> str:
        return self.client.generate_presigned_url(ClientMethod='get_object',
                                                  Params={'Bucket': Config.AWS_S3_BUCKET, 'Key': key},
                                                  ExpiresIn=3600,
                                                  HttpMethod='GET')

    def remove(self, key):
        self.client.delete_obj(Bucket=Config.AWS_S3_BUCKET, Key=key)
