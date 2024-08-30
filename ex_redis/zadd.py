import redis

client = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)

queue_name = "sorted_set_key"
client.zadd(name=queue_name, mapping={"task1": 1, "task2": 2})
client.zadd(name=queue_name, mapping={"task3": 4})
client.zadd(name=queue_name, mapping={"task0": 1})
client.zadd(name=queue_name, mapping={"task": 0})

assert client.zrange(name=queue_name, start=0, end=1) == ["task", "task0"]
assert client.zrevrangebyscore(name=queue_name, max=2, min=1, withscores=True) == [
    ("task2", 2.0),
    ("task1", 1.0),
    ("task0", 1.0),
]

assert client.delete(queue_name) == 1
