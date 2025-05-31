from fastapi import FastAPI
from app.api.v1.api_router import api_router

app = FastAPI(title="Attendance Service")

app.include_router(api_router)

