from dataclasses import dataclass, field
from enum import Enum
from typing import Union

import redis
from dataclasses_json import LetterCase, config, dataclass_json
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query


class PersonType(str, Enum):
    child = "child"
    adult = "adult"


@dataclass_json(letter_case=LetterCase.CAMEL)
class BaseClass:
    pass


@dataclass
class Person(BaseClass):
    id: str
    name: str
    age: int
    person_type: PersonType = field(metadata=config(encoder=lambda x: x.value, decoder=PersonType))
    address: Union[str, None] = field(default=None)


person1 = Person.from_dict(
    {"id": 1, "name": "kim hong min", "age": 30, "person_type": "adult", "address": "seoul"}
)
person2 = Person.from_dict({"id": 2, "name": "park hang min", "age": 10, "person_type": "child"})

client = redis.Redis(host="localhost", port=6379)
client.flushdb()
search = client.ft("idx:person")

search.create_index(
    (
        TagField("$.id", as_name="id"),
        TagField("$.name", as_name="name"),
        NumericField("$.age", as_name="age"),
        TagField("$.person_type", as_name="person_type"),
        TagField("$.address", as_name="address"),
    ),
    definition=IndexDefinition(prefix=["person:"], index_type=IndexType.JSON),
)
client.json().set("person:1", Path.root_path(), person1.to_dict(encode_json=True))
client.json().set("person:2", Path.root_path(), person2.to_dict(encode_json=True))

assert client.json().get("person:1") == {
    "id": "1",
    "name": "kim hong min",
    "age": 30,
    "personType": "adult",
    "address": "seoul",
}

# query
assert search.search(Query("@name:min")).total == 0
assert search.search(Query("@name:{kim hong min}")).docs[0].id == "person:1"
assert search.search("*").total == 2
