from redis.asyncio import ConnectionPool as AsyncConnectionPool
from redis.asyncio import Redis as AsyncRedis


# 1. Redis 클라이언트 생성, 연결 테스트 및 종료
async def create_client():
    client = AsyncRedis()
    ping_result = await client.ping()
    assert ping_result is True

    aclose_result = await client.aclose()
    assert aclose_result is None


# 2. 커넥션 풀을 사용하여 Redis 클라이언트 생성 및 종료
async def create_client_using_connection_pool():
    pool = AsyncConnectionPool.from_url("redis://localhost:6379/0")
    client = AsyncRedis.from_pool(pool)
    await client.aclose()


# 3. 커넥션 풀에서 여러 Redis 클라이언트 생성 및 종료
async def create_multi_client_using_connection_pool():
    pool = AsyncConnectionPool.from_url("redis://localhost")
    client1 = AsyncRedis(connection_pool=pool)
    client2 = AsyncRedis(connection_pool=pool)
    await client1.aclose()
    await client2.aclose()
    await pool.aclose()


# 4. Redis 3버전 프로토콜 을 사용
async def create_client_using_protocol_3():
    client = AsyncRedis(protocol=3)
    await client.aclose()
    await client.ping()
