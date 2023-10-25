from sqlalchemy import Column, MetaData, Integer, String, TIMESTAMP

from app.database import Base

metadata = MetaData()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    # more_info = []
    begin = Column(TIMESTAMP)
    end = Column(TIMESTAMP)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    weight = Column(String, nullable=False)
    category = Column(String, nullable=False)
    users = [id, id, id]
    # comment
