import asyncio
import aiohttp

async def fetch(session, name):
    url = f"https://api.bgm.tv/search/subject/{name}?type=2&responseGroup=small"
    async with session.get(url) as response:
        return await response.json()

async def main():
    names = ["刀剑神域", "我推的孩子", "孤独摇滚"]  # 搜索的名称列表
    async with aiohttp.ClientSession() as session:
        tasks = []
        for name in names:
            task = asyncio.ensure_future(fetch(session, name))
            tasks.append(task)
        results = await asyncio.gather(*tasks)

        # 按照请求顺序显示结果
        for name, result in zip(names, results):
            print(f"搜索结果 - {name}: {result}")

asyncio.run(main())
