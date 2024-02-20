import redis

pool = redis.ConnectionPool(host="localhost", port=6379, db=2, max_connections=4, decode_responses=True)

with redis.StrictRedis(connection_pool=pool) as conn:
    conn.set("test1", "hello world")
    data = conn.get("test1")
    print(data)
    assert data == "hello world"
