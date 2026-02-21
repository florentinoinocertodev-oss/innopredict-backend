import os

BASE_DIR = os.getcwd()
APP_DIR = os.path.join(BASE_DIR, "app")

# --- Criar estrutura de diretórios ---
dirs = [
    APP_DIR,
    os.path.join(APP_DIR, "models"),
    os.path.join(APP_DIR, "routes")
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# --- Arquivos e conteúdos ---
files_content = {
    # ---------------- main.py ----------------
    os.path.join(APP_DIR, "main.py"): '''from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.routes.prediction_routes import router as prediction_router
from app.routes.user import router as user_router
from app.routes.analytics_routes import router as analytics_router
from app.routes.history_routes import router as history_router

from app.database import Base, engine, get_db

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="INO-Predict Express", version="1.0.0",
              description="Aplicativo de previsão multitécnica para jogos de apostas (Fases 1 a 5)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Incluindo routers
app.include_router(prediction_router)
app.include_router(user_router)
app.include_router(analytics_router)
app.include_router(history_router)

@app.on_event("startup")
async def startup_event():
    print("INO-Predict Express iniciou com sucesso!")

@app.on_event("shutdown")
async def shutdown_event():
    print("INO-Predict Express finalizado!")

@app.get("/")
def root():
    return {"message": "INO-Predict Express API está funcionando!"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT 1").scalar()
        return {"status": "ok", "db_connection": result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
''',

    # ---------------- database.py ----------------
    os.path.join(APP_DIR, "database.py"): '''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./innopredict.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
''',

    # ---------------- crud.py ----------------
    os.path.join(APP_DIR, "crud.py"): '''from sqlalchemy.orm import Session
from app.models.user import User
from app.models.prediction import Prediction
from app.models.analytics import Analytics
from app.models.history import UserHistory

def get_or_create_user(db: Session, username: str, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user, False
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user, True

def save_prediction(db: Session, user_id: int, bet_platform: str, game_type: str, suggested_multiplier: float, confidence: float):
    pred = Prediction(user_id=user_id, bet_platform=bet_platform, game_type=game_type,
                      suggested_multiplier=suggested_multiplier, confidence=confidence)
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred

def save_analytics(db: Session, user_id: int | None, predicted_multiplier: float, confidence: float):
    a = Analytics(user_id=user_id, predicted_multiplier=predicted_multiplier, confidence=confidence)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

def save_history(db: Session, user_id: int, bet_platform: str, game_type: str, stake: float, suggested_multiplier: float, confidence: float):
    h = UserHistory(user_id=user_id, bet_platform=bet_platform, game_type=game_type,
                    stake=stake, suggested_multiplier=suggested_multiplier, confidence=confidence)
    db.add(h)
    db.commit()
    db.refresh(h)
    return h

def get_history_by_user(db: Session, user_id: int):
    return db.query(UserHistory).filter(UserHistory.user_id == user_id).all()
''',

    # ---------------- ml_predict.py ----------------
    os.path.join(APP_DIR, "ml_predict.py"): '''def predict(values: list):
    # Retornar valor fictício baseado na média
    if not values:
        return 1.0
    return round(sum(values)/len(values), 2)
''',

    # ---------------- models/user.py ----------------
    os.path.join(APP_DIR, "models/user.py"): '''from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    predictions = relationship("Prediction", back_populates="user")
    history = relationship("UserHistory", back_populates="user")
''',

    # ---------------- models/prediction.py ----------------
    os.path.join(APP_DIR, "models/prediction.py"): '''from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bet_platform = Column(String)
    game_type = Column(String)
    suggested_multiplier = Column(Float)
    confidence = Column(Float)

    user = relationship("User", back_populates="predictions")
''',

    # ---------------- models/analytics.py ----------------
    os.path.join(APP_DIR, "models/analytics.py"): '''from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Analytics(Base):
    __tablename__ = "analytics"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    predicted_multiplier = Column(Float)
    confidence = Column(Float)
''',

    # ---------------- models/history.py ----------------
    os.path.join(APP_DIR, "models/history.py"): '''from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class UserHistory(Base):
    __tablename__ = "user_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bet_platform = Column(String, nullable=False)
    game_type = Column(String, nullable=False)
    stake = Column(Float, nullable=False)
    suggested_multiplier = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="history")
''',

    # ---------------- routes/history_routes.py ----------------
    os.path.join(APP_DIR, "routes/history_routes.py"): '''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import save_history, get_history_by_user
from app.models.user import User

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/user/{user_id}")
def get_user_history(user_id: int, db: Session = Depends(get_db)):
    history = get_history_by_user(db, user_id)
    if not history:
        raise HTTPException(status_code=404, detail="Not Found")
    return [{"bet_platform": h.bet_platform,
             "game_type": h.game_type,
             "stake": h.stake,
             "suggested_multiplier": h.suggested_multiplier,
             "confidence": h.confidence,
             "timestamp": h.timestamp} for h in history]

@router.post("/user/{user_id}")
def create_user_history(user_id: int, payload: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    h = save_history(db, user_id, payload["bet_platform"], payload["game_type"],
                     payload["stake"], payload["suggested_multiplier"], payload["confidence"])
    return {"message": "History created", "history_id": h.id}
'''
}

# --- Criar arquivos ---
for path, content in files_content.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Backend INO-Predict Express (Fases 1-5) criado com sucesso!")
