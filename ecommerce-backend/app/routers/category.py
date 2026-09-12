


from fastapi import APIRouter,Depends, File, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import Optional


from app.core.storage import upload_image
from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category import create_category, get_category, get_top_level_categories, set_category_image

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post(
    "/",
    response_model=CategoryResponse
)
def create(
    name: str = Form(...),
    parent_id: Optional[int] = Form(None),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    if parent_id is not None:
        parent = get_category(db, parent_id)
        if parent is None:
            raise HTTPException(
                status_code=404,
                detail="Parent category not found"
            )
    image_url = upload_image(file, folder="categories") if file else None

    category_data = CategoryCreate(name=name, parent_id=parent_id)
    return create_category(db, category_data, image_url)

@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def list_categories(
    db: Session = Depends(get_db)
):
    return get_top_level_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get(
    category_id: int,
    db: Session = Depends(get_db)

):
    category = get_category(db, category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category

@router.post(
    "/{category_id}/image",
    response_model=CategoryResponse
)
def upload_category_image(
    category_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    category = get_category(db, category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )
    image_url = upload_image(file, folder="categories")
    return set_category_image(db, category, image_url)