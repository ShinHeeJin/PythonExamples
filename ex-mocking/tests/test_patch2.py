from unittest import mock

import pytest

from mocking.myfunc import myfunc

# 여러가지 patching 방법


def test_main_func1():
    assert myfunc() == "original return value"


@pytest.fixture(autouse=True)
def custom():
    with mock.patch("mocking.myfunc.myfunc", return_value="mocked return values"):
        yield


def test_main_func2():
    from mocking.myfunc import myfunc

    assert myfunc() == "mocked return values"


def test_main_func3():
    from mocking.myfunc import myfunc

    with mock.patch("mocking.myfunc.myfunc", return_value="mocked return values"):
        assert myfunc() == "mocked return values"


@mock.patch("mocking.myfunc.myfunc", return_value="mocked return values")
def test_main_func4(mock_func):
    assert mock_func() == "mocked return values"
    mock_func.assert_called_once_with()


def test_main_func5():
    with mock.patch("mocking.myfunc.myfunc") as mock_myfunc:
        from mocking.myfunc import myfunc

        assert myfunc is mock_myfunc

        result = mock_myfunc(1, 2)
        assert isinstance(result, mock.MagicMock)
        mock_myfunc.assert_called_once()
        mock_myfunc.assert_called_once_with(1, 2)
        assert mock_myfunc.call_args == mock.call(1, 2)
