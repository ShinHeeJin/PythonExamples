# ref : https://tech.madup.com/python-asyncio-intro/
import asyncio
from time import perf_counter

import aiohttp
import requests

headers = {"User-Agent": "Mozilla/5.0"}


async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            result = await response.text()
            return len(result)


async def sync_get_content(url):
    response = requests.get(url, headers=headers)
    return len(response.text)


async def get_contents():
    coroutines = [
        sync_get_content(url)
        for url in [
            "https://www.google.co.kr/search?q=" + i
            for i in ["apple", "pear", "grape", "pineapple", "orange", "strawberry"]
        ]
    ]
    result = await asyncio.gather(*coroutines)
    assert len(result) == 6
    print(result)


stime = perf_counter()
asyncio.run(get_contents())

print(perf_counter() - stime)
