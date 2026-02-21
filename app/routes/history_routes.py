from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.history_service import record_history, get_user_history
from ..schemas.schemas import HistoryCreate, History
from ..database import get_db

router = APIRouter(tags=["History"])  # Sem prefix interno

@router.post("/", response_model=History)
def create_history_endpoint(history: HistoryCreate, user_id: int, db: Session = Depends(get_db)):
    return record_history(db, user_id, history.action, history.result)

@router.get("/{user_id}", response_model=list[History])
def list_user_history(user_id: int, db: Session = Depends(get_db)):
    return get_user_history(db, user_id)
