from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.schemas import PredictionCreate, Prediction
from ..services.prediction_service import generate_prediction, get_predictions_by_user
from ..database import get_db

router = APIRouter(tags=["Predictions"])  # Sem prefix interno

@router.post("/", response_model=Prediction)
def create_prediction_endpoint(pred: PredictionCreate, user_id: int, db: Session = Depends(get_db)):
    prediction = generate_prediction(db, user_id, pred.input_data)
    return prediction

@router.get("/{user_id}", response_model=list[Prediction])
def list_user_predictions(user_id: int, db: Session = Depends(get_db)):
    predictions = get_predictions_by_user(db, user_id)
    if not predictions:
        raise HTTPException(status_code=404, detail="No predictions found for user")
    return predictions
