from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .relations import plant_category
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plant import Plant


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()

    plants: Mapped[list["Plant"]] = relationship(secondary=plant_category)