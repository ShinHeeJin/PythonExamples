from dataclasses import asdict, dataclass, fields

import redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from redis.exceptions import ResponseError


@dataclass
class Person:
    id: int
    name: str
    age: int

    @classmethod
    def from_doc(cls, doc):
        data = {}
        for _field in fields(cls):
            value = doc[_field.name]
            if _field.name == "id" and ":" in value:
                value = value.split(":")[-1]
            data[_field.name] = _field.type(value)
        return cls(**data)


person1 = Person(**{"id": 1, "name": "kim hong min", "age": 30})
person2 = Person(**{"id": 2, "name": "park hang min", "age": 25})


client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
client.flushdb()

INDEX_NAME = "person_index"
search = client.ft(INDEX_NAME)
try:
    search.info()
except ResponseError as error:
    if str(error) == "Unknown index name":
        search.create_index(
            fields=[TextField("id"), TextField("name")],
            definition=IndexDefinition(prefix=["person:"], index_type=IndexType.HASH),
        )
    else:
        raise error

client.hset(name="person:1", mapping=asdict(person1))
client.hset(name="person:2", mapping=asdict(person2))

results = search.search(Query("@name:*min*"))
person = Person.from_doc(results.docs[0])
person  # Person(id=1, name='kim hong min', age=30)
