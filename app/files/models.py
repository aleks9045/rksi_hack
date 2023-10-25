from sqlalchemy import Column, MetaData, Integer, String, Text

from app.database import Base

metadata = MetaData()


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    file_path = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
