from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate

def create_category(
    db: Session,
    category_data: CategoryCreate,
    image_url: str | None = None
) -> Category:


    category = Category(
        name=category_data.name,
        parent_id=category_data.parent_id,
        image_url=image_url,
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category




def get_category(
    db: Session,
    category_id: int
) -> Category | None:

    return db.get(Category, category_id)


def get_top_level_categories(
    db: Session,
) -> list[Category]:

    return db.query(Category).filter(Category.parent_id.is_(None)).all()

def set_category_image(
    db: Session,
    category: Category,
    image_url: str
) -> Category:


    category.image_url = image_url
    db.commit()
    db.refresh(category)

    return category