from sqlalchemy import create_engine

from app.config.config import Config
from sqlalchemy.orm import sessionmaker


engine = create_engine(Config.DATABASE.value)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
