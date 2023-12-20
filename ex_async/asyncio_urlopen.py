import asyncio
from time import time
from urllib.request import Request, urlopen

urls = [
    "https://www.google.co.kr/search?q=" + i
    for i in ["apple", "pear", "grape", "pineapple", "orange", "strawberry"]
]

# fmt: off
async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    # UA가 없으면 403 에러 발생
    response = await loop.run_in_executor(None, urlopen, request)    # 네이티브 코루틴 안에서 블로킹I/O 함수를 실행하려면 run_in_excutor 함수를 사용하여 다른스레드에서 병렬로 실행시켜야 한다.
    page = await loop.run_in_executor(None, response.read)           # executor:None -> 기본 스레드 풀 사용
    return len(page)
 
async def main():
    """
    ensure_future 함수는 코루틴 또는 퓨처 객체를 인자로 받고 태스크 객체를 반환하다.

    gather 함수는 모든 코루틴 객체가 끝날 때까지 기다린 뒤 결과를 리스트로 반환하다.
    """
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    result = await asyncio.gather(*futures)
    print(result)
 
begin = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print(f'실행 시간: {end-begin:.3f}초')
# 실행 시간: 0.928초
