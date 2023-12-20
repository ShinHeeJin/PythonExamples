import asyncio


async def add(a, b):
    print(f"add: {a} + {b}")
    await asyncio.sleep(1.0)
    return a + b


async def print_add(a, b):
    """
    await은 네이티브 코루틴 에서만 사용할 수 있다. ( python3.5 부터 사용가능 )
    await 뒤에 코루틴, 퓨처, 태크스 객체를 지정하면 해당 객체가 끝날때 까지 기다린 뒤 결과를 반환한다.
    """
    result = await add(a, b)
    print(f"print_add: {a} + {b} = {result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_add(1, 2))
    loop.close()
