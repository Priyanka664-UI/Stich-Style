from fastapi import APIRouter, Depends
from app.api.controllers.auth import register_user, login_user
from app.models.user import UserCreate, UserLogin
from app.config.database import get_database

router = APIRouter()

@router.post("/register")
async def register_route(user_data: UserCreate, db=Depends(get_database)):
    return await register_user(user_data, db)

@router.post("/login")
async def login_route(login_data: UserLogin, db=Depends(get_database)):
    return await login_user(login_data, db)
