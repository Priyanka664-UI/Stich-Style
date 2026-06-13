from pydantic import BaseModel
from typing import Optional, List

class OrderItem(BaseModel):
    design_id: str
    measurements: dict

class OrderBase(BaseModel):
    user_id: str
    tailor_id: Optional[str] = None
    items: List[OrderItem]
    total_amount: float
    status: str = "pending"

class OrderResponse(OrderBase):
    id: str
