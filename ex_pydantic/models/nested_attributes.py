from pydantic import BaseModel, ConfigDict


class PetClazz:
    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species


class PersonClazz:
    def __init__(self, *, name: str, age: float = None, pets: list[PetClazz]):
        self.name = name
        self.age = age
        self.pets = pets


class Pet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    species: str


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: float = None
    pets: list[Pet]


bones = PetClazz(name="Bones", species="dog")
orion = PetClazz(name="orion", species="cat")
anna = PersonClazz(name="Anna", age=20, pets=[bones, orion])

anna_model = Person.model_validate(anna)
print(anna_model)  # name='Anna' age=20.0 pets=[Pet(name='Bones', species='dog'), Pet(name='orion', species='cat')]
assert anna_model.model_dump() == {
    "name": "Anna",
    "age": 20.0,
    "pets": [{"name": "Bones", "species": "dog"}, {"name": "orion", "species": "cat"}],
}
assert [pet.model_dump() for pet in anna_model.pets] == [
    {"name": "Bones", "species": "dog"},
    {"name": "orion", "species": "cat"},
]
