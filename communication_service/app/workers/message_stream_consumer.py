from core.redis_client import redis_client, STREAM_NAME

def consume_messages():
    last_id = "0-0"
    while True:
        messages = redis_client.xread({STREAM_NAME: last_id}, block=5000, count=10)
        for stream, entries in messages:
            for msg_id, data in entries:
                last_id = msg_id
                print(f"New message: {data}")
                # Push to WebSocket, email, or store notification

