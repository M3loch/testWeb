from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from models import test
from db import engine

# async def main():
#     async with engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(res.first())

async_session = async_sessionmaker(engine)

class CRUD:
    
    async def get_all():
        async with async_session() as session:
            query = select(test)
            result = await session.execute(query)
            array = result.scalars().all()
            print(array)
    
    async def get_by_id(id):
        async with engine.connect() as session:
            result = session.get(test, id)
            print(result)

    async def add(val : int):

        async with async_session() as session:

            new_value = test(value = val)
            session.add(new_value)
            await session.commit()

    async def set_value(id:int, value:int):
        async with async_session as session:
            store = await session.get

