from functools import lru_cache

import pytest


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
