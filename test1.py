import asyncio

async def test():
    print("111")
    await asyncio.sleep(3)

async def test2():
    print("222")
    await asyncio.sleep(3)

async def main():
    task1 = asyncio.create_task(test())
    task2 = asyncio.create_task(test2())
    await task1
    await task2

asyncio.run(main())