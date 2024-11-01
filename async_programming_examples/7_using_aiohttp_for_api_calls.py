import aiohttp
import asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Data from {url}: {data}")
            return data

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
    ]
    tasks = [fetch_json(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

asyncio.run(main())