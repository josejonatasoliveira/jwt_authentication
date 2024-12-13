from sqlalchemy.orm import Session

from app.models.models import User
from app.models.schemas import UserCreate
from app.security.dependencies import get_password_hash


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        role=user.role,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
