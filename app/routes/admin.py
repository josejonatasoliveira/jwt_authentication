from fastapi import APIRouter, Depends, HTTPException

from app.models.models import User
from app.security.dependencies import get_current_user

admin_router = APIRouter()


@admin_router.get("/admin")
def get_admin_data(user: User = Depends(get_current_user)):
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="You don't have permission to access this resource")
    return {"message": "Welcome, Admin!"}
