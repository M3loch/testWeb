from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from config import settings

metadata = MetaData()

print(settings.DATABASE_URL())

engine = create_engine(
    url=settings.DATABASE_URL
)

counter_table = Table(
    'counter',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('count', Integer)
)