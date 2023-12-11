from contextlib import contextmanager


@contextmanager
def sample_context():
    # __enter__ 역할
    print("Entering the context")

    # 컨텍스트 내용
    yield "Hello, context!"

    # __exit__ 역할
    print("Exiting the context")


if __name__ == "__main__":
    with sample_context() as message:
        print("Inside the context")
        print(f"{message=}")

    print("Outside the context")

# Entering the context
# Inside the context
# message='Hello, context!'
# Exiting the context
# Outside the context
