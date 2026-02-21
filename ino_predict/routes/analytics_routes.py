# app/routes/analytics_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.analytics_schema import AnalyticsCreate, AnalyticsOut
from app.crud.crud_prediction import create_analytics, get_analytics_by_user
from app.database import get_db

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.post("/", response_model=AnalyticsOut)
def create_analytics_endpoint(analytics: AnalyticsCreate, db: Session = Depends(get_db)):
    return create_analytics(db, analytics)

@router.get("/user/{user_id}", response_model=list[AnalyticsOut])
def get_analytics_endpoint(user_id: int, db: Session = Depends(get_db)):
    analytics_list = get_analytics_by_user(db, user_id)
    if not analytics_list:
        raise HTTPException(status_code=404, detail="Not Found")
    return analytics_list
