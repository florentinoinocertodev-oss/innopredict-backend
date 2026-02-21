from sqlalchemy import Column, Integer, Float, ForeignKey, String
from app.database import Base

class Analytics(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    predicted_multiplier = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    message = Column(String)