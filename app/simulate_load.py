import random
from datetime import datetime, timedelta
from app.crud import crud
from app.schemas.schemas import UserCreate, PredictionCreate
from app.services import prediction_service, history_service
from app.database import SessionLocal

db = SessionLocal()

NUM_USERS = 50
PREDICTIONS_PER_USER = 20

def random_username():
    return f"user{random.randint(1000, 9999)}"

def random_email():
    return f"{random.randint(1000,9999)}@test.com"

def random_input():
    return f"input_{random.randint(1,1000)}"

def simulate():
    users = []
    # Criar usuários
    for _ in range(NUM_USERS):
        user_data = UserCreate(username=random_username(), email=random_email())
        user = crud.create_user(db, user_data)
        users.append(user)
    
    # Criar previsões e histórico
    for user in users:
        for _ in range(PREDICTIONS_PER_USER):
            input_data = random_input()
            prediction = prediction_service.make_prediction(db, user.id, input_data)
            history_service.log_prediction(db, user.id, prediction.id)
    
    print(f"Simulação completa: {NUM_USERS} usuários x {PREDICTIONS_PER_USER} previsões cada")

if __name__ == "__main__":
    simulate()
