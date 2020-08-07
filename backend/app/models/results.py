from datetime import datetime
from sqlalchemy import Column, String, DATETIME, BIGINT
from .base import Base


class Result(Base):
    __tablename__ = 'results'

    id = Column('id', BIGINT, primary_key=True, autoincrement=True)
    audio_key = Column('audio_key', String(255), nullable=False, default='')
    text = Column('text', String(500), nullable=False, default='')
    created_at = Column('created_at', DATETIME, nullable=False, default=datetime.utcnow)
