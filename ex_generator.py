from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class MyObject:
    id: int


class MyRepository:
    def __init__(self, my_objects):
        self._my_objects = set(my_objects)

    def add(self, my_object):
        self._my_objects.add(my_object)

    def get(self, id):
        return next((o for o in self._my_objects if o.id == id), None)


objects = [MyObject(1), MyObject(2), MyObject(3)]
repository = MyRepository(objects)
repository.add(MyObject(4))
assert repository.get(2).id == 2
assert repository.get(5) is None

# --------------------------


def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i


def number_generator_by_yield_from():
    x = [1, 2, 3]
    yield from x


# ---------------------------


def generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def three_generator():
    yield from generator(3)


for i in three_generator():
    print(i)
