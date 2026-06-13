from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def orders_route():
    return {"message": "Orders route"}
