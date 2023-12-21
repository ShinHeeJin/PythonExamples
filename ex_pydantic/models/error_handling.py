from typing import List

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    list_of_ints: List[int]
    a_float: float


data = dict(
    list_of_ints=["1", 2, "bad"],
    a_float="not a float",
)


def test_model_validation_error_and_erros_data():
    try:
        Model(**data)
    except ValidationError as e:
        assert e.errors() == [
            {
                "type": "int_parsing",
                "loc": ("list_of_ints", 2),
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "bad",
                "url": "https://errors.pydantic.dev/2.5/v/int_parsing",
            },
            {
                "type": "float_parsing",
                "loc": ("a_float",),
                "msg": "Input should be a valid number, unable to parse string as a number",
                "input": "not a float",
                "url": "https://errors.pydantic.dev/2.5/v/float_parsing",
            },
        ]
