from sqlalchemy import Column, String, Integer
from .database import Base
# from extensions import db
class GuessCounter(Base):
    __tablename__ = "guess_counters"
    word = Column(String, primary_key=True)
    count = Column(Integer, default=0)
