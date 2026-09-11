from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Category(Base):
    __tablename__ = "categories"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )

    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True
    )

    image_url: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True
    )

    parent: Mapped[Optional["Category"]] = relationship(
        "Category",
        remote_side=[id],
        back_populates="children"
    )

    children: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="parent"
    )