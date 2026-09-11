


from fastapi import APIRouter,Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session


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
    category_data: CategoryCreate,
    db: Session = Depends(get_db)
):
    if category_data.parent_id is not None:
        parent = get_category(db, category_data.parent_id)
        if parent is None:
            raise HTTPException(
                status_code=404,
                detail="Parent category not found"
            )

    return create_category(db, category_data)

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