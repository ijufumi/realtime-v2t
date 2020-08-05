from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config

engine = create_engine(Config.MYSQL_URI, echo=True)
session = sessionmaker(bind=engine)
