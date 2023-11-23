import random
from dataclasses import dataclass, field
from typing import Iterable, Iterator, Sequence

iterable = [1, 2, 3]
iterator = iterable.__iter__()
assert next(iterator) == 1
assert next(iterator) == 2
assert next(iterator) == 3


iterator = iter("abc")
assert next(iterator) == "a"
assert next(iterator) == "b"
assert next(iterator) == "c"


__sentinel = 2
iterator = iter(lambda: random.randint(0, 10), __sentinel)
assert __sentinel not in [i for i in iterator]


assert isinstance("123", Iterable)
assert isinstance([1, 2, 3], Iterable)
assert isinstance({1, 2, 3}, Iterable)
assert isinstance((1, 2, 3), Iterable)
assert isinstance({"1": 1, "2": 2, "3": 3}, Iterable)

assert isinstance("123", Sequence)
assert isinstance([1, 2, 3], Sequence)
assert not isinstance({1, 2, 3}, Sequence)
assert isinstance((1, 2, 3), Sequence)
assert not isinstance({"1": 1, "2": 2, "3": 3}, Sequence)

assert isinstance([1, 2, 3].__iter__(), Iterator)

# --------------------------------------------------------------------


@dataclass
class MyIterable:
    start: int
    end: int

    def __iter__(self):
        return MyIterator(self.start, self.end)


@dataclass
class MyIterator:
    start: int
    end: int
    current: int = field(init=False)

    def __post_init__(self):
        self.current = self.start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        self.current += 1
        return self.current - 1


assert [each for each in MyIterable(1, 5)] == [1, 2, 3, 4, 5]

iterator = MyIterable(1, 5).__iter__()
assert next(iterator) == 1
assert next(iterator) == 2
assert next(iterator) == 3
assert next(iterator) == 4
assert next(iterator) == 5
