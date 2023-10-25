from sqlalchemy import Column, MetaData, Integer, String, ForeignKey
from app.tasks.models import Task
from app.database import Base

metadata = MetaData()


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    task = Column(Integer, ForeignKey("task.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
