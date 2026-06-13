from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def users_route():
    return {"message": "Users route"}
