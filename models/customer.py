from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order

class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()

    orders: Mapped[list["Order"]] = relationship(back_populates='customer')