from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user, get_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    response_model=UserResponse
)
def create(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user_data)

@router.get(
    "/{user_id}",
    response_model=UserResponse

)
def get(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

