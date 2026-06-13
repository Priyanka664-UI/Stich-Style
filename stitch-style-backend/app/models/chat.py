from pydantic import BaseModel
from datetime import datetime

class ChatMessageBase(BaseModel):
    sender_id: str
    receiver_id: str
    message: str

class ChatMessageResponse(ChatMessageBase):
    id: str
    timestamp: datetime
