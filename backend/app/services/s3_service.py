import boto3
import ffmpeg
import os
import tempfile
from datetime import datetime
from pathlib import Path
from typing import List

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
        key = os.path.join("realtime-v2t", datetime.utcnow().strftime("%Y%m%d-%H%M%S"), path.name)
        self.client.upload_file(Filename=str(path.resolve()),
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
        self.client.delete_object(Bucket=Config.AWS_S3_BUCKET, Key=key)

    def save_to_tmp(self, data: List[bytes]) -> Path:
        webm_file = self._get_tmp_file("webm")
        with open(webm_file, 'wb') as writer:
            for d in data:
                writer.write(d)

        return Path(webm_file)

    def convert(self, path: Path) -> Path:
        wav_file = self._get_tmp_file("wav")
        ffmpeg.input(str(path.resolve())).output(wav_file).run()

        return Path(wav_file)

    def store_to_db(self, key: str) -> Result:
        result = Result(audio_key=key)
        result = self.result_repository.create(result)
        return result

    def save(self, model: Result) -> Result:
        return self.result_repository.update(model)

    def delete(self, result_id: str) -> None:
        result = self.result_repository.find_by_id(result_id)
        if result:
            self.remove(result.audio_key)
            self.result_repository.delete(result)

    def get_all_from_db(self) -> List[Result]:
        return self.result_repository.all()

    @staticmethod
    def _get_tmp_file(suffix: str) -> str:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            return f"{file.name}.{suffix}"
