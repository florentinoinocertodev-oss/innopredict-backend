import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# DB temporário para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria tabelas de teste
Base.metadata.create_all(bind=engine)

# Override get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_create_and_get_prediction():
    # Criar previsão
    response = client.post("/api/v1/predictions/", params={"user_id": 1}, json={"input_data": "Teste"})
    assert response.status_code == 200
    data = response.json()
    assert data["input_data"] == "Teste"
    assert "value" in data

    # Listar previsões
    response = client.get("/api/v1/predictions/1")
    assert response.status_code == 200
    predictions = response.json()
    assert len(predictions) > 0
    assert predictions[0]["input_data"] == "Teste"

def test_create_and_get_history():
    # Criar histórico
    response = client.post("/api/v1/history/", params={"user_id": 1}, json={"action": "TestAction", "result": "Success"})
    assert response.status_code == 200
    data = response.json()
    assert data["action"] == "TestAction"
    assert data["result"] == "Success"

    # Listar histórico
    response = client.get("/api/v1/history/1")
    assert response.status_code == 200
    history = response.json()
    assert len(history) > 0
    assert history[0]["action"] == "TestAction"
