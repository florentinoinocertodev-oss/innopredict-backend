from sqlalchemy.orm import Session
from app.models.history import History
from app.schemas.history_schema import HistoryCreate

def create_history(db: Session, history: HistoryCreate):
    db_obj = History(**history.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_history_by_user(db: Session, user_id: int):
    return db.query(History).filter(History.user_id == user_id).all()