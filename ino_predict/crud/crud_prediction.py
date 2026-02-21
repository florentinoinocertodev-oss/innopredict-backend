# app/crud/crud_prediction.py

from sqlalchemy.orm import Session
from app.models.prediction import Prediction

def create_prediction(db: Session, user_id: int, suggested_multiplier: float, confidence: float, message: str):
    new_prediction = Prediction(
        user_id=user_id,
        suggested_multiplier=suggested_multiplier,
        confidence=confidence,
        message=message
    )
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    return new_prediction

def get_prediction_by_id(db: Session, prediction_id: int):
    return db.query(Prediction).filter(Prediction.id == prediction_id).first()
