from typing import Optional

from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None

class CategoryResponse(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] =None
    image_url: Optional[str] =None
    children: list["CategoryResponse"] = []

    model_config = ConfigDict(from_attributes=True)

CategoryResponse.model_rebuild()