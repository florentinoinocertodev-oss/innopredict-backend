import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models.models import Base

# --- Cria banco de teste ---
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    yield TestClient(app)

@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
