from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(
    db:Session,
    user_data: UserCreate
) -> User:

    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(
    db: Session,
    email: str
) -> User | None:

    return db.query(User.email == email).first()


def get_user(
    db: Session,
    user_id: int
) -> User | None:

    return db.get(User, user_id)
