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
