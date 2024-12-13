import os

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.models import User

http_bearer = HTTPBearer()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(http_bearer), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token.credentials.replace('Bearer ', ''), SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
