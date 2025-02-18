from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from custormer.entities.BaseEntities import BaseEntity
from custormer.entities.Product import Product, order_product_association


class Order(BaseEntity):
    __tablename__ = 'orders'

    order_by_User = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="orders")
    products = relationship("Product", secondary=order_product_association)

