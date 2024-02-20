from threading import Lock


def locked_method(method):
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)

    return newmethod


class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = Lock()

    @locked_method
    def add(self, elem):
        return super().add(elem)

    @locked_method
    def remove(self, elem):
        return super().remove(elem)
