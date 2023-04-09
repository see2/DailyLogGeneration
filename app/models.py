from sqlalchemy import Column, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(String, primary_key=True)
    content_hash = Column(String, unique=True, nullable=False)
    input = Column(Text, nullable=False)
    output = Column(Text, nullable=False)
    date = Column(String, nullable=False)
