from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from pythonProject.custormer.entities.BaseEntities import BaseEntity


class User(BaseEntity):
    __tablename__ = 'users'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    orders = relationship("Order", back_populates="user")