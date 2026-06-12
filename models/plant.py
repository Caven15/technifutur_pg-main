from .base import Base
from sqlalchemy import String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from .relations import plant_category
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .stock import Stock
    from .category import Category
    from .order_line import OrderLine

class Plant(Base):
    __tablename__ = 'plant'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    base_price: Mapped[Decimal] = mapped_column(DECIMAL(6, 2))

    stocks: Mapped[list["Stock"]] = relationship(back_populates='plant')
    order_lines: Mapped[list["OrderLine"]] = relationship(back_populates='plant')
    categories: Mapped[list["Category"]] = relationship(secondary=plant_category)

