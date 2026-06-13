from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def ar_route():
    return {"message": "AR route"}
