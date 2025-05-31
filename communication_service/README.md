export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account.json
python -m app.workers.redis_to_firestore
python -m app.workers.stream_consumer

