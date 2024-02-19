import asyncio
import sys

import pytest
import pytest_asyncio
from redis import Redis as SyncRedis
from redis.asyncio import Redis as AnsycRedis


@pytest.fixture(scope="function")
def redis_client():
    redis_client = SyncRedis(db=0, decode_responses=True)
    redis_client.flushdb()

    yield redis_client
    redis_client.flushdb()


@pytest_asyncio.fixture(scope="function")
async def async_redis_client():
    async_redis_client = AnsycRedis(db=0, decode_responses=True)
    await async_redis_client.flushdb()

    yield async_redis_client
    await async_redis_client.flushdb()


@pytest.fixture(scope="session")
def event_loop_policy():

    policy = asyncio.DefaultEventLoopPolicy()
    if sys.platform == "win32":
        policy = asyncio.WindowsSelectorEventLoopPolicy()
    return policy
