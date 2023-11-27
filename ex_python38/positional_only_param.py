# pytest ./positional_only_param.py

import pytest


def test_positional_only_param1():
    def divide(a, b, /):
        """
        a, b -> positional-only
        """
        return a / b

    assert divide(2, 4) == 0.5
    with pytest.raises(TypeError, match="got some positional-only arguments passed as keyword arguments"):
        divide(1, b=2)
        divide(a=1, b=2)


def test_positional_only_param2():
    def func(a, /, *, b=2):
        """
        a -> positional-only
        b -> keyword only
        """
        return {"a": a, "b": b}

    assert func(1, b=3) == {"a": 1, "b": 3}
    assert func(1) == {"a": 1, "b": 2}
    with pytest.raises(TypeError):
        func(1, 2)
        func(a=1, b=2)
        func(b=2, a=1)


def test_positional_only_param3():
    def func(a, b, /, c, d, *, e, f):
        """
        a, b -> positional-only
        c, d -> positional or keyword
        e, f -> keyword only
        """
        return a, b, c, d, e, f

    assert func(10, 30, 40, 50, e=60, f=70) == (10, 30, 40, 50, 60, 70)
    assert func(10, 30, c=40, d=50, e=60, f=70) == (10, 30, 40, 50, 60, 70)
    with pytest.raises(TypeError, match="got some positional-only arguments passed as keyword arguments"):
        func(a=10, b=30, c=40, d=50, e=60, f=70)
