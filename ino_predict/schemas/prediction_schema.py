# app/schemas/prediction_schema.py

from pydantic import BaseModel

class PredictionRequest(BaseModel):
    user_id: int
    suggested_multiplier: float
    confidence: float
    message: str

class PredictionOut(BaseModel):
    id: int
    user_id: int
    suggested_multiplier: float
    confidence: float
    message: str

    class Config:
        orm_mode = True
