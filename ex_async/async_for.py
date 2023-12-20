"""
async for 로 동작하는 클래스를 만들려면 __aiter__와 __anext__ 메서드를 구현한다.
"""

import asyncio


class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        print(f"{self}'s __anext__ excuted !")
        if self.current < self.stop:
            await asyncio.sleep(1)
            r = self.current
            self.current += 1
            return r

        raise StopAsyncIteration


async def async_one():
    return 1


async def main():
    # 1
    async for i in AsyncCounter(3):
        print(i)

    # 2
    a = [i async for i in AsyncCounter(3)]
    assert a == [0, 1, 2]

    # 3
    coroutines = [async_one, async_one, async_one]
    a = [await coroutine() for coroutine in coroutines]
    assert a == [1, 1, 1]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
