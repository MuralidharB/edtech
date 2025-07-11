from fastapi import FastAPI
from app.api.v1.api_router import router as api_router

app = FastAPI(title="Quiz Service")
app.include_router(api_router, prefix="/api/v1")

