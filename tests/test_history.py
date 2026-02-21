from app.crud import crud
from app.schemas.schemas import UserCreate
from app.services import history_service, prediction_service

def test_history_logging(db_session):
    user = crud.create_user(db_session, UserCreate(username="histuser", email="hist@test.com"))
    prediction = prediction_service.make_prediction(db_session, user.id, "input hist")
    
    history = history_service.get_user_history(db_session, user.id)
    
    assert len(history) > 0
    assert history[0].prediction_id == prediction.id
