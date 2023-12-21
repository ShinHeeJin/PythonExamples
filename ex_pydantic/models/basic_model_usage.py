from pydantic import BaseModel


# Basic model usage
class User(BaseModel):
    id: int
    name: str = "Jane Doe"


user = User(id=123)
assert user.id == 123
assert isinstance(user.name, str)
assert user.model_dump() == {"id": 123, "name": "Jane Doe"}
assert user.model_fields_set == {"id"}

# Nested models


class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple: str = "x"
    banana: str = "y"


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


spam = Spam(foo={"count": 4}, bars=[{"apple": "x1"}, {"apple": "x2"}])
print(spam)  # foo=Foo(count=4, size=None) bars=[Bar(apple='x1', banana='y'), Bar(apple='x2', banana='y')]
print(spam.foo)  # count=4 size=None
print(spam.bars)  # [Bar(apple='x1', banana='y'), Bar(apple='x2', banana='y')]
assert spam.model_dump() == {
    "foo": {"count": 4, "size": None},
    "bars": [{"apple": "x1", "banana": "y"}, {"apple": "x2", "banana": "y"}],
}
