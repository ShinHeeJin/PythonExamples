from unittest.mock import MagicMock, Mock

import pytest

# 1. 특정 값 반환 mock 객체
mock = Mock(return_value="test1234")
assert mock() == "test1234"


# 2. side_effect with exception
mock = Mock(side_effect=Exception("my exception!"))
try:
    mock()
except Exception as e:
    assert str(e) == "my exception!"

# 3. side_effect with iterable
mock = Mock(side_effect=(1, 2, 3))
with pytest.raises(StopIteration):
    mock(), mock(), mock(), mock()

# 4. side_effect with function
mock = Mock(side_effect=lambda x: x + 10)
assert mock(10) == 20

# 5.
mock = Mock()
mock.return_value = 1
assert mock() == 1
mock.return_value = 2
assert mock() == 2

# 6.
mock = Mock()
mock.attr = "attr"
assert mock.attr == "attr"
mock.meth.return_value = "meth return value"
assert mock.meth() == "meth return value"

# 7.
mock = Mock()
with pytest.raises(AssertionError, match="Expected 'mock' to have been called."):
    mock.assert_called()
mock()
mock.assert_called()
mock.assert_called_once()
mock()
with pytest.raises(AssertionError, match="Expected 'mock' to have been called once. Called 2 times."):
    mock.assert_called_once()

# 8.
mock = Mock()
mock(a=1, c=2)
mock(a=1, b=2)
mock.assert_called_with(a=1, b=2)
assert mock.call_count == 2
assert mock.call_args.kwargs == {"a": 1, "b": 2}


# 9. 매직메서드 모킹은 직접 할당해야하지만 MacgicMock의 경우 미리 모킹되어 있음
mock = Mock()
print(mock)  # <Mock id='4445989648'>
with pytest.raises(AttributeError, match="'method-wrapper' object has no attribute 'return_value'"):
    mock.__str__.return_value = 1

mock = Mock()
mock.__str__ = Mock(return_value="my mock")
print(mock)  # my mock

mock = MagicMock()
mock.__str__.return_value = "my mock"
print(mock)  # my mock
