# app/routes/prediction_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.prediction_schema import PredictionRequest, PredictionOut
from app.services.prediction_service import generate_prediction
from app.database import get_db

router = APIRouter(prefix="/predictions", tags=["Predictions"])

@router.post("/", response_model=PredictionOut)  # endpoint "/predictions/"
def create_prediction_endpoint(request: PredictionRequest, db: Session = Depends(get_db)):
    return generate_prediction(
        db,
        user_id=request.user_id,
        suggested_multiplier=request.suggested_multiplier,
        confidence=request.confidence,
        message=request.message
    )
