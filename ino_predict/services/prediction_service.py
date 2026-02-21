# app/services/prediction_service.py

from sqlalchemy.orm import Session
from app.crud.crud_prediction import create_prediction

def generate_prediction(db: Session, user_id: int, suggested_multiplier: float, confidence: float, message: str):
    return create_prediction(
        db,
        user_id=user_id,
        suggested_multiplier=suggested_multiplier,
        confidence=confidence,
        message=message
    )
