import pytest
from app.crud import crud
from app.schemas.schemas import UserCreate

def test_create_user(db_session):
    user_data = UserCreate(username="testuser", email="test@test.com")
    user = crud.create_user(db_session, user_data)
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "test@test.com"

def test_get_user(db_session):
    user_data = UserCreate(username="anotheruser", email="another@test.com")
    created_user = crud.create_user(db_session, user_data)
    user = crud.get_user(db_session, created_user.id)
    assert user.username == "anotheruser"
