from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, index=True)
    score = Column(Float)
    verdict = Column(String)
    raw_data = Column(Text)
