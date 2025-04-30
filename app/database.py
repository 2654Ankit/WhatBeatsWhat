from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

# Base.metadata.create_all(bind=engine)

# async def get_db():
#     async with SessionLocal() as session:
#         yield session





import time
import logging
from sqlalchemy.exc import OperationalError
# from app.extensions import db

MAX_RETRIES = 5
RETRY_DELAY = 2




def init_db(app):
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            engine.init_app(app)
            with app.app_context():
                engine.create_all()
            return True
        except OperationalError as e:
            retry_count += 1
            logging.warning(f"Database connection failed (attempt {retry_count}/{MAX_RETRIES}): {str(e)}")
            if retry_count < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
    logging.error("Failed to connect to database after multiple retries")
    return False