import asyncio

import nest_asyncio

nest_asyncio.apply()


class TestAync:

    def __init__(self):
        pass

    def subscribed(self, topic: str):

        def decorator(callback):

            async def wrapper(message):
                await asyncio.sleep(1.0)
                result = await callback(message)
                return result

            return wrapper

        return decorator


class TestAdaptorAsync:
    def __init__(self, client: TestAync):
        self.client = client
        self.subscribed = client.subscribed


client = TestAync()
adaptor = TestAdaptorAsync(client)


@adaptor.subscribed("test")
async def test(message):
    print("test executed")
    return message


async def main():
    await test(message=1)


if __name__ == "__main__":
    asyncio.run(main())
