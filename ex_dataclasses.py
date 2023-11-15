from dataclasses import dataclass, field, asdict, astuple
from dataclasses import FrozenInstanceError
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
from dataclasses import dataclass, field


class MyException(Exception):
    pass


@dataclass
class UnitOfWork:
    work_id: int
    events: list = field(default_factory=list)
    close: bool = False

    def __post_init__(self):
        self.close = True

    def execute(self):
        try:
            print(f"execute! => work_id : {self.work_id}")
            raise MyException(f"Error in {self.__class__.__name__}")
        except MyException as e:
            self.events.append(e)


try:
    uow = UnitOfWork(1, [])
    uow.execute()
finally:
    uow.close = True

# UnitOfWork(work_id=1, events=[MyException('Error in UnitOfWork')], close=True)
print(uow)
