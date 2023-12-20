# 제너레이터 기반 코루틴과 구분하기 위해 async def로 만든 코루틴을 네이티브 코루틴 이라고 한다.

import asyncio


async def hello():
    print("Hello, world!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()
