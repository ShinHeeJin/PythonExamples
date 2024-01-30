import time

import redis

# Connection
r = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)
r.flushall()
# r = redis.from_url("redis://127.0.0.1:6379/2", decode_responses=True)
assert r.ping() is True

# set, get, delete
assert r.set("test", 1)
assert r.get("test") == "1"
assert r.delete("test") == 1  # 삭제 건수
assert r.get("test") is None

assert r.set("test", 1)
assert r.set("test", 2)  # 덮어쓰기
assert r.get("test") == "2"

# hash
r.hset("person", "name", "hong")
r.hset("person", "age", 10)
assert r.hgetall("person") == {"name": "hong", "age": "10"}

# set
r.sadd("personSet", "hong")
r.sadd("personSet", "kim")
r.sadd("personSet", "park")
r.sadd("personSet", "park")
r.sadd("personSet", "park")
assert r.smembers("personSet") == {"hong", "kim", "park"}

# sortedset
r.zadd("sorted-test", {"a": 3})
r.zadd("sorted-test", {"b": 2})
r.zadd("sorted-test", {"c": 1})
assert r.zrange("sorted-test", 0, 100) == ["c", "b", "a"]

# list
r.lpush("personList", "hong")
r.lpush("personList", "kim")
r.lpush("personList", "park")
r.rpush("personList", "han")
r.rpush("personList", "choi")
assert r.lrange("personList", 0, 5) == ["park", "kim", "hong", "han", "choi"]

# expire
expired_in = 1
r.set("expired_in", 10, expired_in)
assert r.get("expired_in") == "10"
time.sleep(expired_in)
assert r.get("expired_in") is None

r.set("expired_in", 10)
r.expire("expired_in", expired_in)
