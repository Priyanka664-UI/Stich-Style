from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def tailor_route():
    return {"message": "Tailor route"}
