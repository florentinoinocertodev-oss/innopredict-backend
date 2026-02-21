from sqlalchemy.orm import Session
from ..crud.crud import (
    create_history as crud_create_history,
    get_user_history as crud_get_user_history
)

# Função para registrar histórico
def record_history(db: Session, user_id: int, action: str, result: str):
    return crud_create_history(db, user_id, action, result)

# Função para listar histórico de um usuário
def get_user_history(db: Session, user_id: int):
    return crud_get_user_history(db, user_id)
