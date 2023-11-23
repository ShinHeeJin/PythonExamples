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
