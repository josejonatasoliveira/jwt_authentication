from fastapi import APIRouter, Depends, HTTPException

from app.models.models import User
from app.security.dependencies import get_current_user

user_router = APIRouter()


@user_router.get("/user")
def get_user(user: User = Depends(get_current_user)):
    if user.role != 'user':
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return {"message": "Welcome, User!"}
