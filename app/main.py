from fastapi import FastAPI

from app.routes.admin import admin_router
from app.routes.user import user_router
from app.security.auth import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(admin_router)
