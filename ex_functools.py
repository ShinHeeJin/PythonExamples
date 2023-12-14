from functools import lru_cache, partial

import pytest

# partial


def test_first():
    def myfunc(a, b, c):
        return a + b + c

    new_func = partial(myfunc, a=1, b=2)
    assert new_func(c=1) == 4
    assert new_func(a=1, b=1, c=1) == 3
    assert new_func(a=1, c=1) == 4


def test_seconds():
    def power(base, exp):
        return base**exp

    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    assert square(2) == 4
    assert cube(2) == 8


# ------------------------------------------

# lru_cache


@lru_cache(maxsize=128)
def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


@pytest.mark.timeout(1)
def test_fibonacci_func_excutiontime_is_shortened_by_lru_cache():
    """
    lru_cache를 사용하여 재귀함수의 결과를 캐싱한다. 1초내 실행가능
    """
    result = fibo(100)
    assert result == 354224848179261915075
