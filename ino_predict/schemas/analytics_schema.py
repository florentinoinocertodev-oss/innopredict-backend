from pydantic import BaseModel

class AnalyticsCreate(BaseModel):
    user_id: int
    predicted_multiplier: float
    confidence: float
    message: str

class AnalyticsOut(AnalyticsCreate):
    id: int
    class Config:
        orm_mode = True