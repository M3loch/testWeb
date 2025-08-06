from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class test(Base):
    __tablename__ = 'test'
    
    id : Mapped[int] = mapped_column(primary_key=True)
    value : Mapped[int] = mapped_column(nullable=False)
         