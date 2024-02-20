import asyncio

from redis.asyncio.client import Redis as AsyncRedis

redis_client = AsyncRedis()
KEY_NAME = "test_async_redis_cnt"


async def async_increment(redis_client, cnt):
    async with await redis_client.pipeline() as pipe:
        for _ in range(cnt):
            pipe.incr(KEY_NAME)
        await pipe.execute()


async def main():
    await redis_client.set(KEY_NAME, 0)
    tasks = [async_increment(redis_client, cnt) for cnt in range(100)]
    await asyncio.gather(*tasks)
    result = await redis_client.pipeline().get(KEY_NAME).execute()
    assert result == [b"4950"]


if __name__ == "__main__":

    asyncio.run(main())
