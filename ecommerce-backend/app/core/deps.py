from fastapi import Depends , Header, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.security import ALGORITHM, SECRET_KEY
from app.database import get_db
from app.models.user import User
from app.services.user import get_user

def get_current_user(
    authorization: str = Header(...),
    db: Session = Depends(get_db)  
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    if not authorization.startswith("Bearer "):
        raise credentials_exception

    token = authorization.removeprefix("Bearer ")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise credentials_exception
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(db, int(user_id))
    if user is None:
        raise credentials_exception


    return user