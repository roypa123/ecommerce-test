from typing import Optional

from sqlalchemy import ForeignKey, Numeric, String , Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    title:Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    price:Mapped[float] = mapped_column(
        Numeric(10,2),
        nullable=False
    )

    image_url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship("Category")