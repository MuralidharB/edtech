from fastapi import FastAPI
from .api.v1.api_router import api_router

app = FastAPI(title="Communication Service")
app.include_router(api_router, prefix="/api/v1")

