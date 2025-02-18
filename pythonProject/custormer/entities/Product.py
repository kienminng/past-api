from sqlalchemy import Column, String, Integer, DECIMAL, Table, ForeignKey

from pythonProject.custormer.entities.BaseEntities import BaseEntity, Base
from sqlalchemy.orm import declarative_base

class Product(BaseEntity):
    __tablename__ = 'products'

    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(18, 2), nullable=False)

order_product_association = Table(
    'order_details', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('quantity', Integer, nullable=False)
)