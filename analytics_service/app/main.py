from fastapi import FastAPI
from app.api.v1.api_router import router as api_router

app = FastAPI(
    title="Analytics Service",
    version="1.0.0",
    description="Service to handle academic and operational analytics"
)

@app.get("/")
def health_check():
    return {"status": "ok", "service": "analytics"}

app.include_router(api_router, prefix="/api/v1")

