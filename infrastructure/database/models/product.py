from .base import Base, created_at
from .mixins.int_id_pk import IntIdPkMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Product(Base, IntIdPkMixin):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    quantity: Mapped[int] = mapped_column(default=5)
    price: Mapped[float]
    in_stock: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[created_at]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category = relationship("Category", back_populates='product')