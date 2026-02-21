from pydantic import BaseModel
from datetime import datetime

class HistoryCreate(BaseModel):
    user_id: int
    prediction_id: int
    result_multiplier: float

class HistoryOut(HistoryCreate):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True