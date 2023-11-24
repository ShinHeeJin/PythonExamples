from functools import partial


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
