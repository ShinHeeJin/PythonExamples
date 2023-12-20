"""
async with로 동작하는 클래스를 만들기 위해
__aenter__와 __aexit__ 메서드를 구현한다.
"""

import asyncio


class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def __aenter__(self):
        print(f"{self}'s __aenter__")
        await asyncio.sleep(1)
        return self.a + self.b

    async def __aexit__(self, exc_type, exc_value, traceback):
        print(f"{self}'s __aexit__")
        pass


async def main():
    async with AsyncAdd(1, 2) as result:
        assert result == 3
        print(f"result : {result}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
