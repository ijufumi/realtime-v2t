from datetime import datetime
from sqlalchemy import Column, String, DATETIME, BIGINT
from . import Base


class Result(Base):
    id = Column('id', BIGINT, primary_key=True, autoincrement=True)
    audio_key = Column('audio_key', String(255), nullable=False, default='')
    text = Column('text', String(500), nullable=False, default='')
    created_at = Column('created_at', DATETIME, nullable=False, default=datetime.utcnow)
