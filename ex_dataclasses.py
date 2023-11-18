from dataclasses import dataclass, field
from dataclasses import dataclass, field, asdict, astuple
from datetime import date


@dataclass
class MyData:
    x: int = -1
    y: int = 0
    z: int = field(init=False)
    points: list = field(default_factory=list)

    def __post_init__(self):
        self.z = self.x + self.y

    def sum(self):
        return self.x + self.y


data = MyData()
assert data.sum() == -1
assert asdict(data) == {"x": -1, "y": 0, "z": -1, "points": []}
assert data.z == -1
assert astuple(data) == (-1, 0, -1, [])
data.points.append(1)
assert data.points == [1]

# --------------------------------------------------------------------

from dataclasses import dataclass
from dataclasses import FrozenInstanceError


@dataclass(frozen=True, unsafe_hash=True)
class User:
    id: int
    name: str
    birth: date
    master: bool = False


user = User(1, "test", date.today(), True)
user2 = User(2, "test2", date.today(), False)
user3 = User(2, "test2", date.today(), False)

try:
    user.id = 2
except FrozenInstanceError as e:
    assert str(e) == "cannot assign to field 'id'"

assert user != user2
assert user2 == user3

# --------------------------------------------------------------------

from dataclasses import dataclass, field


class MyException(Exception):
    pass


@dataclass
class UnitOfWork:
    work_id: int
    events: list = field(default_factory=list)
    close: bool = False

    def execute(self):
        try:
            print(f"execute! => work_id : {self.work_id}")
            raise MyException(f"Error in {self.__class__.__name__}")
        except MyException as e:
            self.events.append(e)


try:
    uow = UnitOfWork(1, [])
    uow.execute()
    assert uow.close == False
finally:
    uow.close = True

# UnitOfWork(work_id=1, events=[MyException('Error in UnitOfWork')], close=True)
assert uow.close == True
assert len(uow.events) == 1

# --------------------------------------------------------------------

from dataclasses import dataclass, field


@dataclass
class MyCollector:
    data: list = field(default_factory=list)

    def __post_init__(self):
        for idx in range(5):
            self.data.append(idx)

    def collect(self):
        while self.data:
            yield self.data.pop(0)


collector = MyCollector()
assert list(collector.collect()) == [0, 1, 2, 3, 4]


# --------------------------------------------------------------------


@dataclass
class Parent:
    id: int
    name: str
    static_childs = []
    childs: list = field(default_factory=list)


parent = Parent(id=1, name="test")
parent2 = Parent(id=2, name="test2")

assert parent.childs == parent.static_childs
parent.childs.append(1)
parent.static_childs.append(1)

assert parent2.static_childs == [1]
assert parent2.childs == []
