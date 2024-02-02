import json
from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BaseClass:
    pass


@dataclass
class Person(BaseClass):
    person_id: str
    person_name: str
    person_age: int


data = {
    "personId": "person_001",
    "personName": "홍길동",
    "personAge": 30,
}
person = Person.from_json(json.dumps(data))  # Person(person_id='person_001', person_name='홍길동', person_age=30)
person.to_json()  # '{"personId": "person_001", "personName": "\\ud64d\\uae38\\ub3d9", "personAge": 30}'
person.to_dict()  # {'personId': 'person_001', 'personName': '홍길동', 'personAge': 30}
