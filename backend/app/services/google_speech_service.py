from typing import List
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums


class GoogleSpeechService:
    def __init__(self):
        self.client = speech_v1p1beta1.SpeechClient()

    def to_text(self, audio_file: str) -> List[str]:
        config = {
            "language": "ja-JP"
        }
        audio = {
            "uri": audio_file
        }

        response = self.client.recognize(config, audio)
        return [res.alternatives[0].transcript() for res in response.results]
