from unittest import mock

import pytest

from ex_mocking.myfunc import myfunc

# 여러가지 patching 방법


def test_main_func1():
    assert myfunc() == "original return value"


@pytest.fixture(autouse=True)
def custom():
    with mock.patch("ex_mocking.myfunc.myfunc", return_value="mocked return values [1]"):
        yield


def test_main_func2():
    from ex_mocking.myfunc import myfunc

    assert myfunc() == "mocked return values [1]"


def test_main_func3():
    from ex_mocking.myfunc import myfunc

    with mock.patch("ex_mocking.myfunc.myfunc", return_value="mocked return values [2]"):
        assert myfunc() == "mocked return values [1]"


@mock.patch("ex_mocking.myfunc.myfunc", return_value="mocked return values [3]")
def test_main_func4(mock_func):
    assert mock_func() == "mocked return values [3]"
    mock_func.assert_called_once_with()


def test_main_func5():
    with mock.patch("ex_mocking.myfunc.myfunc") as mock_myfunc:
        from ex_mocking.myfunc import myfunc

        assert myfunc is mock_myfunc

        result = mock_myfunc(1, 2)
        assert isinstance(result, mock.MagicMock)
        mock_myfunc.assert_called_once()
        mock_myfunc.assert_called_once_with(1, 2)
        assert mock_myfunc.call_args == mock.call(1, 2)
