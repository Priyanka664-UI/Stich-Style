from pydantic import BaseModel
from typing import Optional

class TailorBase(BaseModel):
    user_id: str
    shop_name: str
    experience_years: int
    rating: float = 0.0

class TailorResponse(TailorBase):
    id: str
