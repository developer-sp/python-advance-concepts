import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            print(f"Fetched {url}")
            return content

async def main():
    url = "https://www.example.com"
    page_content = await fetch_page(url)
    print(f"Page length: {len(page_content)}")

asyncio.run(main())