from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="School Service API")

app.include_router(api_router.router, prefix="/api/v1")

