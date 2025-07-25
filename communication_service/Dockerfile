FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code
COPY ./app ./app

# Set environment variable for Google credentials (optional override at runtime)
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials/service-account.json

# Copy credentials (you can mount this securely in production)
COPY ./credentials/service-account.json /app/credentials/service-account.json

# Default command (can be overridden)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

