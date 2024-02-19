import pytest
from redis.asyncio.client import Redis as AsyncRedis
from redis.client import Redis as SyncRedis

pytest_plugins = ("pytest_asyncio",)


def test_sync_redis_set_and_get(redis_client: SyncRedis):
    # given
    redis_client.set("test_key", 1)

    # when
    result = redis_client.get("test_key")

    # then
    assert result == "1"


@pytest.mark.asyncio
async def test_insert_task_async(async_redis_client: AsyncRedis):
    # given
    await async_redis_client.set("test_key", 1)

    result = await async_redis_client.get("test_key")

    # then
    assert result == "1"
