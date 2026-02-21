from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    prediction_id = Column(Integer, ForeignKey('predictions.id'))
    result_multiplier = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())