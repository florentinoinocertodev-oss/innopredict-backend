from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.routes.prediction_routes import router as prediction_router
from app.routes.user import router as user_router
from app.routes.analytics_routes import router as analytics_router
from app.routes.history_routes import router as history_router

from app.database import Base, engine, get_db

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="INO-Predict Express", version="1.0.0",
              description="Aplicativo de previsão multitécnica para jogos de apostas (Fases 1 a 5)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Incluindo routers
app.include_router(prediction_router)
app.include_router(user_router)
app.include_router(analytics_router)
app.include_router(history_router)

@app.on_event("startup")
async def startup_event():
    print("INO-Predict Express iniciou com sucesso!")

@app.on_event("shutdown")
async def shutdown_event():
    print("INO-Predict Express finalizado!")

@app.get("/")
def root():
    return {"message": "INO-Predict Express API está funcionando!"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT 1").scalar()
        return {"status": "ok", "db_connection": result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
