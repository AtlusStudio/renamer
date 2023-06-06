import asyncio

async def heavy_task():
    print("1")
    await asyncio.sleep(2)

async def main():
    for _ in range(5):
        await heavy_task()

asyncio.run(main())