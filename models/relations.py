from sqlalchemy import Table, Column, ForeignKey

from .base import Base


plant_category = Table(
    'plant_category',
    Base.metadata,
    Column('plant_id', ForeignKey('plant.id')),
    Column('category_id', ForeignKey('category.id')),
)