from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def content_route():
    return {"message": "Content route"}
