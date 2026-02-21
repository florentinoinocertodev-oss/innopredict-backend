from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class PredictionRequest(BaseModel):
    param1: float
    param2: float
    param3: float

class PredictionResponse(BaseModel):
    predicted_value: float

class PredictionHistory(Base):
    __tablename__ = "prediction_history"
    id = Column(Integer, primary_key=True, index=True)
    param1 = Column(Float, nullable=False)
    param2 = Column(Float, nullable=False)
    param3 = Column(Float, nullable=False)
    predicted_value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
