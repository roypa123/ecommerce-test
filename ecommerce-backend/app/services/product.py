from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(
    db: Session,
    product_data: ProductCreate,
    image_url: str | None = None
) -> Product:

    product = Product(
        title=product_data.title,
        description=product_data.description,
        price=product_data.price,
        category_id=product_data.category_id,
        image_url=image_url,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(
    db: Session,
    product_id: int
) -> Product | None:

    return db.get(Product, product_id)

def get_product_by_category(
    db: Session,
    category_id: int
) -> list[Product]:

    return db.query(Product).filter(Product.category_id == category_id).all()

