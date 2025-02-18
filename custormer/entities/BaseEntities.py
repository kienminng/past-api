from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)