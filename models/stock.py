from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .plant import Plant


class Stock(Base):
    __tablename__ = 'stock'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column()
    location: Mapped[str] = mapped_column()
    plant_id: Mapped[int] = mapped_column(ForeignKey('plant.id'))
    plant: Mapped["Plant"] = relationship(back_populates='stocks')
