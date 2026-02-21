from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.crud_history import create_history, get_history_by_user
from app.schemas.history_schema import HistoryCreate, HistoryOut
from app.database import get_db

router = APIRouter(prefix="/history", tags=["History"])

@router.post("/", response_model=HistoryOut)
def create_history_endpoint(history: HistoryCreate, db: Session = Depends(get_db)):
    return create_history(db, history)

@router.get("/user/{user_id}", response_model=list[HistoryOut])
def get_history_endpoint(user_id: int, db: Session = Depends(get_db)):
    histories = get_history_by_user(db, user_id)
    if not histories:
        raise HTTPException(status_code=404, detail="Not Found")
    return histories