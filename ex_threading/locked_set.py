"""
스레드 세이프한 형식을 갖춘 코드는 여러 스레드에서 동시에 호출되어도 안전하게 작동하며, 예상치 못한 결과나 버그가 발생하지 않는다.
"""

from threading import Lock


class LockedSet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = Lock()

    def add(self, elem: object) -> None:
        with self._lock:
            super().add(elem)

    def remove(self, elem: object) -> None:
        with self._lock:
            super().remove(elem)

    def __contains__(self, elem: object) -> bool:
        with self._lock:
            return super().__contains__(elem)


def test_locked_set_add():
    locked_set = LockedSet([1, 2, 3, 4])
    locked_set.add(5)
    assert locked_set == {1, 2, 3, 4, 5}
    assert locked_set == LockedSet([1, 2, 3, 4, 5])
