from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id:int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"