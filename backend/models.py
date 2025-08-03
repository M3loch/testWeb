from sqlalchemy import Table, Column, Integer, MetaData

metadata = MetaData()

from database import Base

class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0, nullable=False)
