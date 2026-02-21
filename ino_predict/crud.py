from sqlalchemy.orm import Session
from app.models.user import User
from app.models.prediction import Prediction
from app.models.analytics import Analytics
from app.models.history import UserHistory

def get_or_create_user(db: Session, username: str, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user, False
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user, True

def save_prediction(db: Session, user_id: int, bet_platform: str, game_type: str, suggested_multiplier: float, confidence: float):
    pred = Prediction(user_id=user_id, bet_platform=bet_platform, game_type=game_type,
                      suggested_multiplier=suggested_multiplier, confidence=confidence)
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred

def save_analytics(db: Session, user_id: int | None, predicted_multiplier: float, confidence: float):
    a = Analytics(user_id=user_id, predicted_multiplier=predicted_multiplier, confidence=confidence)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

def save_history(db: Session, user_id: int, bet_platform: str, game_type: str, stake: float, suggested_multiplier: float, confidence: float):
    h = UserHistory(user_id=user_id, bet_platform=bet_platform, game_type=game_type,
                    stake=stake, suggested_multiplier=suggested_multiplier, confidence=confidence)
    db.add(h)
    db.commit()
    db.refresh(h)
    return h

def get_history_by_user(db: Session, user_id: int):
    return db.query(UserHistory).filter(UserHistory.user_id == user_id).all()
