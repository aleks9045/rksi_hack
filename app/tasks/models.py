from sqlalchemy import Column, MetaData, Integer, String, DATE, ForeignKey
from app.database import Base

metadata = MetaData()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    more_info = Column(String, nullable=True)
    files = Column(String, nullable=True)
    begin = Column(DATE, nullable=False)
    end = Column(DATE, nullable=False)
    when_end = Column(DATE, nullable=True)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    users = Column(String, ForeignKey('user.email', ondelete='CASCADE'), nullable=False)
