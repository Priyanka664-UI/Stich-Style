from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def designs_route():
    return {"message": "Designs route"}
