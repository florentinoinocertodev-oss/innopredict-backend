from app.crud import crud
from app.schemas.schemas import PredictionCreate, UserCreate
from app.services import prediction_service

def test_make_prediction(db_session):
    user = crud.create_user(db_session, UserCreate(username="preduser", email="pred@test.com"))
    prediction = prediction_service.make_prediction(db_session, user.id, "input test")
    
    assert prediction.id is not None
    assert 0 <= prediction.predicted_value <= 1
    assert 0.5 <= prediction.confidence <= 1.0
