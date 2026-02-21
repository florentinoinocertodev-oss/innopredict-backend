from app.models.user_models import User, Bet
from app.database import SessionLocal

def create_user(db, username, email):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return {"id": user.id, "username": user.username, "email": user.email, "detail": "Email já cadastrado"}
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

def create_bet(db, user_id, prediction_id, stake):
    new_bet = Bet(user_id=user_id, prediction_id=prediction_id, stake=stake)
    db.add(new_bet)
    db.commit()
    db.refresh(new_bet)
    return {"prediction_id": prediction_id, "user_id": user_id, "stake": stake, "detail": "Aposta criada com sucesso"}
