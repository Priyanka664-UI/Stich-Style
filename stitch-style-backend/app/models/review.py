from pydantic import BaseModel

class ReviewBase(BaseModel):
    order_id: str
    user_id: str
    tailor_id: str
    rating: int
    comment: str

class ReviewResponse(ReviewBase):
    id: str
