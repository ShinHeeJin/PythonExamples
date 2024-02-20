import asyncio


class Parent:

    def __init__(self, name):
        self.name = name

    @classmethod
    async def create(cls, name):
        assert issubclass(cls, Child)
        instance = cls(name)  # Create the instance of the appropriate class
        instance.first_name = await instance.get_first_name(name)
        return instance

    async def get_first_name(self, name):
        await asyncio.sleep(1)
        return name.split(" ")[0]


class Child(Parent):
    # Parent를 상속받았기 때문에 생성자가 필요없음.

    @classmethod
    async def create(cls, name):
        assert issubclass(cls, Child)
        return await super().create(name)

    async def get_child_first_name(self):
        return self.first_name


async def main():
    name = "Hong gil dong"
    child = await Child.create(name)
    assert isinstance(child, Child)  # Parent가 아닌 Child를 반환받는다.
    await child.get_child_first_name()


if __name__ == "__main__":
    asyncio.run(main())
