from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Base única para todos os models
Base = declarative_base()

# ------------------ USERS ------------------
class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}  # evita erro de redefinição

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    bets = relationship("BetModel", back_populates="user")
    predictions = relationship("PredictionModel", back_populates="user")
    history = relationship("HistoryModel", back_populates="user")


# ------------------ BETS ------------------
class BetModel(Base):
    __tablename__ = "bets"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    game = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("UserModel", back_populates="bets")


# ------------------ PREDICTIONS ------------------
class PredictionModel(Base):
    __tablename__ = "predictions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    input_data = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("UserModel", back_populates="predictions")


# ------------------ HISTORY ------------------
class HistoryModel(Base):
    __tablename__ = "history"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    result = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("UserModel", back_populates="history")
