from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreateSchema
from app.services.user_service import create_user
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user_endpoint(user: UserCreateSchema, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email)
