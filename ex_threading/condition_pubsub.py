import random
import threading
import time


class Publisher(threading.Thread):
    def __init__(self, integers: list, condition: threading.Condition, **kwargs):
        super().__init__(**kwargs)
        self.condition = condition
        self.integers = integers

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()
            print(f"Condition Acquired by Publisher : {self.name}")
            self.integers.append(integer)
            print(f"Publisher {self.name} appending to array: {integer}")
            self.condition.notify()  # Wake up one or more threads waiting on this condition, if any.
            print(f"Condition Released by Publisher : {self.name}")
            self.condition.release()
            time.sleep(1)


class Subscriber(threading.Thread):
    def __init__(self, integers: list, condition: threading.Condition, **kwargs):
        super().__init__(**kwargs)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            print(f"Condition Acquired by Consumer: {self.name}")
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print(f"{integer} Popped from list by Consumer: {self.name}")
                    break
                print(f"Condition wait by {self.name}")
                self.condition.wait()
            print(f"Consumer {self.name} Releasing Condition")
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()

    pub1 = Publisher(integers, condition, name="pub1")
    pub1.start()

    sub1 = Subscriber(integers, condition, name="sub1")
    sub2 = Subscriber(integers, condition, name="sub2")
    sub1.start()
    sub2.start()

    pub1.join()
    sub1.join()
    sub2.join()


if __name__ == "__main__":
    main()
