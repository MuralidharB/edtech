from fastapi import FastAPI
from app.api.v1.api_router import router as api_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Enrollment Service")
app.include_router(api_router, prefix="/api/v1")
