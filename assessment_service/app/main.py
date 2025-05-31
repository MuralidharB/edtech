from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api_router import api_router

app = FastAPI(
    title="Assessment Service",
    version="1.0.0",
    description="Handles exams, grading, and result processing in the school automation platform.",
)

# CORS Middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specific origins like ["https://your-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(api_router, prefix="/api/v1")

# Root route (optional health check)
@app.get("/")
def read_root():
    return {"message": "Assessment Service is running."}

