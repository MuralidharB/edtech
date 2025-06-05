# --- Stage 1: Base Image ---
FROM python:3.12-slim AS base

# Environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY app app
COPY alembic alembic
COPY alembic.ini .
COPY .env .

# --- Stage 2: Runtime Image ---
FROM python:3.12-slim

# Copy from builder stage
COPY --from=base /usr/local /usr/local
COPY --from=base /app /app

WORKDIR /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

