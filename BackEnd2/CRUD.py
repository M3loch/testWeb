from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from models import test
from db import engine

from schemas import TestGetDTO, TestPostDTO

async_session = async_sessionmaker(engine)

class CRUD:

    async def get_all():
        async with async_session() as session:
            query = select(test)
            result = await session.execute(query)
            array = [TestGetDTO.model_validate(row, from_attributes=True) for row in result.scalars().all()]
            return array    


    async def get_by_id(id):
        async with async_session() as session:
            result = await session.get(test, id)
            return result.value

    async def add(val : int):
        new_id = None
        async with async_session() as session:

            new_value = test(value = val)
            session.add(new_value)        
            await session.flush()
            new_id = new_value.id
            await session.commit()

        return new_id
            

    async def set_value(id:int, value:int):
        async with async_session() as session:
            obj = await session.get(test, id)
            obj.value = value
            await session.commit()
        return True
    
    async def delete(id: int):
        async with async_session() as session:
            obj = await session.get(test, id)
            if obj:
                await session.delete(obj)
                await session.commit()
                return True
            return False
            