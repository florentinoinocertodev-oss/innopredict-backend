import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/innopredict.db")
    
    # FastAPI
    APP_NAME: str = "InnoPredict"
    APP_VERSION: str = "1.0.0"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Prediction settings
    DEFAULT_PREDICTION_THRESHOLD: float = 0.5

settings = Settings()
