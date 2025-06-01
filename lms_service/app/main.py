from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api_router import router as api_router

app = FastAPI(
    title="LMS Service",
    version="1.0.0",
    description="Handles courses, lessons, quizzes, and content delivery for the school automation platform."
)

# CORS setup (if used with frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include versioned API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "lms-service is running"}

