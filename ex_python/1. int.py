import pytest

print(int("AB", 12))  # 131
print(int("10", 10))  # 10
print(int("111", 2))  # 7

with pytest.raises(ValueError):
    print(int("10.0"))
