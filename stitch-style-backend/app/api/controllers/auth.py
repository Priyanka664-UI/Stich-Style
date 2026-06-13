from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import UserCreate, UserLogin, UserResponse, UserDB
from app.utils.helpers import format_response, hash_password, verify_password, create_access_token

async def register_user(user_data: UserCreate, db: AsyncSession):
    # Check if user exists
    result = await db.execute(select(UserDB).where(UserDB.email == user_data.email))
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    # Create new user
    new_user = UserDB(
        email=user_data.email,
        full_name=user_data.full_name,
        role=user_data.role,
        password=hash_password(user_data.password)
    )
    
    # Save to database
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return format_response(
        success=True, 
        data=UserResponse.model_validate(new_user).model_dump(), 
        message="User registered successfully"
    )

async def login_user(login_data: UserLogin, db: AsyncSession):
    # Find user by email
    result = await db.execute(select(UserDB).where(UserDB.email == login_data.email))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Verify password
    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Generate JWT
    token_data = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    }
    access_token = create_access_token(data=token_data)
    
    return format_response(
        success=True,
        data={
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": str(user.id),
                "email": user.email,
                "full_name": user.full_name,
                "role": user.role
            }
        },
        message="Login successful"
    )
