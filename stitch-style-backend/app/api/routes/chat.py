from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def chat_route():
    return {"message": "Chat route"}
