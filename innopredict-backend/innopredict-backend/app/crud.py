from sqlalchemy.orm import Session
from app.models import PredictionHistory

def save_prediction(db: Session, param1: float, param2: float, param3: float, predicted_value: float):
    prediction = PredictionHistory(
        param1=param1,
        param2=param2,
        param3=param3,
        predicted_value=predicted_value
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction
