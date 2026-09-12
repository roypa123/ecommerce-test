from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category_id: int

class ProductResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: int

    model_config=ConfigDict(from_attributes=True)