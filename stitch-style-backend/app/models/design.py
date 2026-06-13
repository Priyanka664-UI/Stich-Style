from pydantic import BaseModel
from typing import List, Optional

class DesignBase(BaseModel):
    title: str
    description: str
    category: str
    images: List[str]
    price: float

class DesignResponse(DesignBase):
    id: str
    created_by: str
