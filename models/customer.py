from .plant import Plant
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order

class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()

    orders: Mapped[list["Order"]] = relationship(back_populates='customer')
    
    def place_order(self, session, items : list[tuple[Plant, int]]):
        from .order import Order
        from .order_line import OrderLine
        from datetime import date

        order = Order(
            order_date=date.today(),
            status=Order.Status.PENDING,
            customer=self
        )
        session.add(order)
        
        for plant, quantity in items:
            line = OrderLine(
                plant=plant,
                order=order,
                quantity=quantity,
                unit_price=plant.base_price
            )
            session.add(line)
        
        return order
