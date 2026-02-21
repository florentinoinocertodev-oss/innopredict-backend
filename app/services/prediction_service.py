from sqlalchemy.orm import Session
from ..crud.crud import create_prediction as crud_create_prediction, get_user_predictions as crud_get_user_predictions
import random

def generate_prediction(db: Session, user_id: int, input_data: str):
    # Aqui geramos um valor fictício (ou você pode usar modelo real)
    value = random.uniform(0, 100)
    return crud_create_prediction(db, user_id, input_data, value)

def get_predictions_by_user(db: Session, user_id: int):
    return crud_get_user_predictions(db, user_id)
