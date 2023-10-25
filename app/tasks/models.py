from sqlalchemy import Column, MetaData, Integer, String, TIMESTAMP, ForeignKey
from app.auth.models import user
from app.database import Base

metadata = MetaData()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    more_info = Column(String, nullable=True)
    begin = Column(TIMESTAMP, nullable=False)
    end = Column(TIMESTAMP, nullable=False)
    when_end = Column(TIMESTAMP, nullable=True)
    status = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    weight = Column(String, nullable=True)
    category = Column(String, nullable=False)
    users = Column(String, ForeignKey('user.email', ondelete='CASCADE'), nullable=False)
