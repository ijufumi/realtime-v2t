from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config
from .results_repository import ResultRepository

engine = create_engine(Config.MYSQL_URI, echo=True)
session_maker = sessionmaker(bind=engine)

