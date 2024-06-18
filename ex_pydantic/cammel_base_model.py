import json

import pytest
from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class CammelBaseModel(BaseModel):
    class Config:
        populate_by_name = True
        alias_generator = to_camel

    def model_dump(self, by_alias=True):
        return super().model_dump(by_alias=by_alias)


class Person(CammelBaseModel):
    person_id: str
    person_name: str
    person_age: int


# initialize
james = Person(**{"personId": "001", "personName": "james", "personAge": 30})
tomas = Person(person_id="002", person_name="tomas", person_age=28)

persons = [james, tomas]
assert (
    persons.__str__()
    == "[Person(person_id='001', person_name='james', person_age=30), Person(person_id='002', person_name='tomas', person_age=28)]"
)

# serialize typError
with pytest.raises(TypeError, match="Object of type Person is not JSON serializable"):
    json.dumps(persons)


# custom json encoder
def pydantic_encoder(obj):
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    raise TypeError


json.dumps(persons, default=pydantic_encoder)
