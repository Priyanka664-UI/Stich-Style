from fastapi import Depends, HTTPException, status, Header
import jwt
from typing import Optional, List
from app.config.settings import settings

def get_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")
    return authorization.split(" ")[1]

def verify_token(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def require_role(*roles: str):
    def role_dependency(user: dict = Depends(verify_token)):
        if "role" not in user or user["role"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="You don't have permission to access this resource"
            )
        return user
    return role_dependency
