from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class counter(Base):
    __tablename__ = 'counter'
    
    id : Mapped[int] = mapped_column(primary_key=True)
    counter : Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} : {self.counter}"
    
    