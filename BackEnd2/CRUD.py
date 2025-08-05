from models import counter
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select

class CRUD:

    async def init(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session: 

            session.add(0)

            await session.commit()


    async def get_counter(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session: 
            statment = select(counter).order_by(counter.id)

            result = await session.execute(statment)
            print(result.scalars().all())
            return result.scalars().all()

    async def increase(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session: 
            counter = await self.get_counter(session)

            counter.counter = counter.counter + 1

            await session.commit()

    async def reset(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session: 
            counter = await self.get_counter(session)

            counter.counter = 0

            await session.commit()