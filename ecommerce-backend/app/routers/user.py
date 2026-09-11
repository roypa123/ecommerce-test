from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, create_refresh_token
from app.database import get_db
from app.schemas.user import Token,UserCreate, UserResponse
from app.services.user import create_user, get_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/signup",
    response_model=Token
)
def signup(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    user = create_user(db, user_data)
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})
    return Token(access_token, refresh_token=refresh_token)





        

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

