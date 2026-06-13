from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def payments_route():
    return {"message": "Payments route"}
