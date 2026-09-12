from typing import Optional


from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.core.storage import upload_image
from app.database import get_db
from app.models.user import User
from app.schemas.product import ProductCreate, ProductResponse
from app.services.category import get_category
from app.services.product import create_product, get_product, get_product_by_category

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post(
    "/",
    response_model=ProductResponse
)
def create(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    price: float = Form(...),
    category_id: int = Form(...),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category = get_category(db, category_id)
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    image_url = upload_image(file, folder="products") if file else None

    product_data = ProductCreate(
        title=title,
        description=description,
        price=price,
        category_id=category_id
    )

    return create_product(db, product_data, image_url)


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.get(
    "/category/{category_id}",
    response_model=list[ProductResponse]
)
def list_by_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_product_by_category(db, category_id)