import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...schemas.message import MessageCreate, MessageOut
from ...crud.message import create_message
from ...core.security import get_current_user, TokenData
from ...core.redis_client import redis_client, STREAM_NAME

router = APIRouter()

# Temporary role map for demo/testing; replace with actual user-service call
MOCK_USER_ROLES = {
    # Replace with real UUIDs in your environment
    "uuid-of-teacher": "teacher",
    "uuid-of-student": "student"
}


def get_role_for_user(user_id: str) -> str:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://user-service/api/v1/users/{user_id}")
        return resp.json().get("role")


@router.post("/", response_model=MessageOut)
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    sender_role = current_user.role
    receiver_role = get_role_for_user(str(message.receiver_id))

    allowed_pairs = {("student", "teacher"), ("teacher", "student")}
    if (sender_role, receiver_role) not in allowed_pairs:
        raise HTTPException(status_code=403, detail="Role-based access denied")

    saved_msg = create_message(db, message)

    redis_client.xadd(STREAM_NAME, {
        "sender_id": str(saved_msg.sender_id),
        "receiver_id": str(saved_msg.receiver_id),
        "content": saved_msg.content,
        "timestamp": str(saved_msg.timestamp)
    })

    return saved_msg
