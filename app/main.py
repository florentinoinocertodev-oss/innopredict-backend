from fastapi import FastAPI
from .routes.prediction_routes import router as prediction_router
from .routes.history_routes import router as history_router
from .database import init_db

app = FastAPI(
    title="InnoPredict API",
    version="1.0.0",
    description="Enterprise-level prediction API",
)

# Evento de inicialização
@app.on_event("startup")
def on_startup():
    init_db()

# Versionamento de API
api_v1_prefix = "/api/v1"
app.include_router(prediction_router, prefix=f"{api_v1_prefix}/predictions")
app.include_router(history_router, prefix=f"{api_v1_prefix}/history")
