from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def admin_route():
    return {"message": "Admin route"}
