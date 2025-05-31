from app.core.redis_client import redis_client, STREAM_NAME
from app.core.firestore_client import firestore_client
from uuid import uuid4

def get_chat_id(sender_id: str, receiver_id: str) -> str:
    return "-".join(sorted([sender_id, receiver_id]))

def sync_messages():
    last_id = "0-0"
    while True:
        messages = redis_client.xread({STREAM_NAME: last_id}, block=5000, count=10)
        for stream, entries in messages:
            for msg_id, data in entries:
                last_id = msg_id

                sender_id = data["sender_id"]
                receiver_id = data["receiver_id"]
                chat_id = get_chat_id(sender_id, receiver_id)

                doc_ref = firestore_client.collection("messages").document(chat_id).collection("entries").document(str(uuid4()))
                doc_ref.set({
                    "sender_id": sender_id,
                    "receiver_id": receiver_id,
                    "content": data["content"],
                    "timestamp": data["timestamp"]
                })
                print(f"Pushed to Firestore: {data}")

