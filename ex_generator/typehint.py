from typing import Generator


def echo_round() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return "OK"


if __name__ == "__main__":
    generator = echo_round()
    next(generator)
    generator.send(1.0)
    generator.send(2.0)
    generator.send(3.0)

    try:
        generator.send(None)
    except StopIteration as e:
        print(e.value)
