from sqlalchemy import Table, Column, MetaData, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.files.models import File
from app.auth.models import user
from app.database import Base

metadata = MetaData()




class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    more_info = Column(String, nullable=True)
    files = Column(Integer, ForeignKey("file.id", ondelete='CASCADE'), nullable=True)
    # file = relationship("File")
    # files = Column(String, nullable=True)
    begin = Column(TIMESTAMP, nullable=False)
    end = Column(TIMESTAMP, nullable=False)
    status = Column(String, nullable=False)
    when_end = Column(TIMESTAMP, nullable=True)
    priority = Column(Integer, nullable=False)
    weight = Column(String, nullable=True)
    category = Column(String, nullable=True)
    # users = Column(String, nullable=False)
    users = Column(String, ForeignKey(user.c.email, ondelete='CASCADE'), nullable=False)
