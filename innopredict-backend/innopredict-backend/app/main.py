from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import PredictionRequest, PredictionResponse, Base
from app.ml_predict import predict
from app.database import engine, get_db
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="InnoPredictAutoplay Backend", version="1.0.0")

@app.get("/")
def root():
    return {"status": "InnoPredictAutoplay Backend Online"}

@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest, db: Session = Depends(get_db)):
    values = [request.param1, request.param2, request.param3]
    result = predict(values)
    crud.save_prediction(db, request.param1, request.param2, request.param3, result)
    return PredictionResponse(predicted_value=result)
