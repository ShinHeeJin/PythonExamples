import asyncio
import time

# ref: https://www.daleseo.com/python-asyncio/


async def find_users_async(n):
    for i in range(1, n + 1):
        print(f"{n}명 중 {i}번째 조회중..")
        await asyncio.sleep(1)
    print(f"총 {n}명 사용자 비동기 조회 완료!")


async def process_async():
    """
    asyncio.gather() 함수는 비동기 함수들을 병렬로 실행하고 그 결과를 모아주는 역할
    """
    start = time.time()
    corutine1 = find_users_async(3)
    corutine2 = find_users_async(2)
    corutine3 = find_users_async(1)
    print(f"{corutine1=}")
    print(f"{corutine2=}")
    print(f"{corutine3=}")
    result = await asyncio.gather(
        corutine1,
        corutine2,
        corutine3,
    )
    assert result == [None, None, None]
    end = time.time()
    print(f"총 소요시간 : {end - start}")


if __name__ == "__main__":
    corutine = process_async()
    print(f"{corutine=}")
    asyncio.run(corutine)
