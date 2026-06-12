from .base import Base
from .customer import Customer
from .order import Order
from .order_line import OrderLine
from .plant import Plant
from .category import Category
from .stock import Stock

# import importlib
# import pkgutil
# for _, module_name, _ in pkgutil.walk_packages(__path__):
#     module = importlib.import_module(f"{__name__}.{module_name}")
#     attrs = [attr for attr in dir(module) if not attr.startswith('_')]
#     globals().update({attr: getattr(module, attr) for attr in attrs})