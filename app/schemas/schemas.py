from pydantic import BaseModel, ConfigDict
from datetime import datetime

# ------------------ USERS ------------------
class UserBase(BaseModel):
    full_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# ------------------ BETS ------------------
class BetBase(BaseModel):
    amount: float
    game: str

class BetCreate(BetBase):
    pass

class Bet(BetBase):
    id: int
    user_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# ------------------ PREDICTIONS ------------------
class PredictionBase(BaseModel):
    input_data: str
    value: float | None = None

class PredictionCreate(PredictionBase):
    pass

class Prediction(PredictionBase):
    id: int
    user_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# ------------------ HISTORY ------------------
class HistoryBase(BaseModel):
    action: str
    result: str

class HistoryCreate(HistoryBase):
    pass

class History(HistoryBase):
    id: int
    user_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
