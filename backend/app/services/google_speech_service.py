from typing import List
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums


class GoogleSpeechService:
    def __init__(self):
        self.client = speech_v1p1beta1.SpeechClient()

    def to_text(self, audio_file: str) -> str:
        config = {
            "language_code": "ja-JP",
        }
        with open(audio_file, 'rb') as reader:
            content = reader.read()

        audio = {
            "content": content
        }

        response = self.client.recognize(config, audio)
        return "".join([res.alternatives[0].transcript for res in response.results])
