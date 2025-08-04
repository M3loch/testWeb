from db import Base, engine
from models import counter
import asyncio



async def db_init():
    async with engine.begin() as conn:
        
        
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    await engine.dispose()

asyncio.run(db_init())
