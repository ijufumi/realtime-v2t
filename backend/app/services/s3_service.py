import boto3
import os
import tempfile
from datetime import datetime
from pathlib import Path

from app.config import Config
from app.models import Result
from app.repositories import ResultRepository


class S3Service:
    def __init__(self):
        self.client = boto3.client('s3',
                                   aws_access_key_id=Config.AWS_KEY,
                                   aws_secret_access_key=Config.AWS_SECRET,
                                   region_name=Config.AWS_REGION)
        self.result_repository = ResultRepository()

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

    @staticmethod
    def save_to_tmp(data: bytes) -> Path:
        with tempfile.NamedTemporaryFile() as file:
            with open(file.name, 'wb') as writer:
                writer.write(data)

            return Path(file.name)

    def store_to_db(self, key: str) -> Result:
        result = Result(audio_key=key)
        result = self.result_repository.create(result)
        return result
