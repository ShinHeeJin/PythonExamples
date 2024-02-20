# ref: https://seoyeonhwng.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-asyncio-%EC%82%AC%EC%9A%A9%EB%B2%95-891578b3849c
import asyncio
from time import perf_counter


async def async_add(a, b):
    print(f"async_add executed, a : {a}, b: {b}")
    await asyncio.sleep(2.0)
    return a + b


async def main():
    """
    태스크는 코루틴이 동시에 실행되도록 예약할 때 사용된다.
    create_task에 인자로 코루틴을 넘겨주면 코루틴은 실행되도록 예약되고 Task객체를 반환한다.
    """
    start = perf_counter()
    task1 = asyncio.create_task(async_add(1, 1))
    task2 = asyncio.create_task(async_add(1, 2))
    task3 = asyncio.create_task(async_add(1, 3))
    await task1
    await task2
    await task3

    executed_time = perf_counter() - start
    alpha = 0.1
    assert executed_time < 2 + alpha


async def main_with_gather():
    """
    gather 방식으로 여러 비동기 작업을 동시에 실행하고 결과를 받아온다.
    """
    await asyncio.gather(async_add(1, 1), async_add(1, 2), async_add(1, 3))


if __name__ == "__main__":
    """
    비동기 방식으로 여러 작업을 하기 위해서는 코루틴을 생성하고 태스크로 만들어주거나 asyncio.gather() 함수를 사용해야 한다.
    즉, async def 로 생성한 코루틴을 그대로 await를 하면 동기 실행되고, 태스크로 만들거나 asyncio.gather() 로 호출하면 비동기로 실행되는 것이다.
    """
    print("main exeucted ...")
    asyncio.run(main())
    print("main_with_gather exeucted ...")
    asyncio.run(main_with_gather())
