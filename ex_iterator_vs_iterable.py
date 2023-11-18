iterable = [1, 2, 3]
iterator = iterable.__iter__()
assert next(iterator) == 1
assert next(iterator) == 2
assert next(iterator) == 3


iterator = iter("abc")
assert next(iterator) == "a"
assert next(iterator) == "b"
assert next(iterator) == "c"


import random

__function = lambda: random.randint(0, 10)
__sentinel = 2
iterator = iter(__function, __sentinel)
assert __sentinel not in [i for i in iterator]


from typing import Iterable, Iterator, Sequence

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
