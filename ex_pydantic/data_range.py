import pytest
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=7)
    age: int = Field(gt=1, le=130)  # 1 < age <= 30


def create_user(id, name, age):
    return User(**{"id": id, "name": name, "age": age})


@pytest.mark.parametrize(
    "id, name, age, is_valid",
    [
        ("100", "tester", "12", True),
        ("100", "t", "12", False),
        ("100", "tester", "131", False),
    ],
)
def test_invalid_name_length(id, name, age, is_valid):
    if not is_valid:
        with pytest.raises(ValidationError):
            create_user(id, name, age)
    else:
        create_user(id, name, age)
