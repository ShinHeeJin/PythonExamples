import os

os.environ.setdefault("REDIS_OM_URL", "redis://:test1234!@!@@localhost:6379/0")

from datetime import datetime
from typing import List

from redis_om import EmbeddedJsonModel, Field, JsonModel

YYYYMMDD_HHMMSSFFF = "%Y-%m-%d %H:%M:%S.%f"


class Car(EmbeddedJsonModel):
    name: str = Field(index=True)
    number: str = Field(index=True)
    created_at: str = Field(default_factory=lambda: datetime.now().strftime(YYYYMMDD_HHMMSSFFF))


class Person(JsonModel):
    name: str = Field(index=True)
    cars: List[Car]
    created_at: str = Field(default_factory=lambda: datetime.now().strftime(YYYYMMDD_HHMMSSFFF))


def main():
    person = Person(name="person1", cars=[Car(name="sorento", number="1234"), Car(name="sonata", number="5678")])
    person.save()

    person.model_dump()
    {
        "pk": "01J00G2C9DM88F6X843QA1Z7QN",
        "name": "person1",
        "cars": [
            {
                "pk": "01J00G2C9D2GCC7YHA7X0YNX6G",
                "name": "sorento",
                "number": "1234",
                "created_at": "2024-06-10 16:16:13.741742",
            },
            {
                "pk": "01J00G2C9DEJ431AKTQPYDE0HB",
                "name": "sonata",
                "number": "5678",
                "created_at": "2024-06-10 16:16:13.741742",
            },
        ],
        "created_at": "2024-06-10 16:16:13.741742",
    }


if __name__ == "__main__":
    main()
