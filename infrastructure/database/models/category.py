from .base import Base, created_at
from .mixins.int_id_pk import IntIdPkMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(Base, IntIdPkMixin):
    name: Mapped[str] = mapped_column(unique=True)
    icon: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[created_at]

    product = relationship("Product", back_populates='category')