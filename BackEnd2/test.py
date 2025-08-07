from CRUD import CRUD
import asyncio
import time

async def filler():
    tasks = []
    start = time.time() 

    for x in range (10000):
        tasks.append(asyncio.create_task(CRUD.add(x + 1)))
    await asyncio.gather(*tasks)
    tasks = []

    print(time.time()-start)



asyncio.run(filler())

# async def filler():
#     start = time.time() 

#     pool = []
    
#     for x in range (1000):
#         if x < 999:
#             asyncio.create_task(CRUD.add(x + 1))
#         else:
#             await asyncio.create_task(CRUD.add(x + 1))
    
#     print(time.time()-start)


# asyncio.run(filler())
