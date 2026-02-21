from sqlalchemy.orm import Session

from ..models.models import (
    UserModel,
    PredictionModel,
    HistoryModel,
    BetModel,
)


# ------------------ PREDICTIONS ------------------

def create_prediction(
    db: Session,
    user_id: int,
    input_data: str,
    value: float
):
    prediction = PredictionModel(
        user_id=user_id,
        input_data=input_data,
        value=value,
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_user_predictions(db: Session, user_id: int):
    return (
        db.query(PredictionModel)
        .filter(PredictionModel.user_id == user_id)
        .all()
    )


# ------------------ HISTORY ------------------

def create_history(
    db: Session,
    user_id: int,
    action: str,
    result: str,
):
    history = HistoryModel(
        user_id=user_id,
        action=action,
        result=result,
    )
    db.add(history)
    db.commit()
    db.refresh(history)
    return history


def get_user_history(db: Session, user_id: int):
    return (
        db.query(HistoryModel)
        .filter(HistoryModel.user_id == user_id)
        .all()
    )
