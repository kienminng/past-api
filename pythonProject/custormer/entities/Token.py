from sqlalchemy import Column, Integer

from pythonProject.custormer.entities.BaseEntities import BaseEntity


class Token(BaseEntity):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)

