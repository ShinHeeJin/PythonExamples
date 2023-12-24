import random
import time
from threading import RLock, Thread, current_thread


def get_current_thread_name():
    return f"'{current_thread().name}'"


class Philosopher(Thread):
    def __init__(self, name: str, leftfork: RLock, rightfork: RLock):
        Thread.__init__(self, name=name)
        self.leftfork = leftfork
        self.rightfork = rightfork

    def run(self):
        print(f"{get_current_thread_name()} has started thinking")
        while True:
            time.sleep(random.randint(1, 5))
            print(f"{get_current_thread_name()} has finished thinking")
            self.leftfork.acquire()
            time.sleep(random.randint(1, 5))

            try:
                print(f"{get_current_thread_name()} has acquired the left fork")
                self.rightfork.acquire()
                try:
                    print(f"{get_current_thread_name()} has attained both forks, currently eating")
                finally:
                    self.rightfork.release()
                    print(f"{get_current_thread_name()} has released the right fork")

            finally:
                self.leftfork.release()
                print(f"{get_current_thread_name()} has released the left fork")


fork1 = RLock()
fork2 = RLock()
fork3 = RLock()
fork4 = RLock()
fork5 = RLock()

philosopher1 = Philosopher("Kant", fork1, fork2)
philosopher2 = Philosopher("Aristotle", fork2, fork3)
philosopher3 = Philosopher("Spinoza", fork3, fork4)
philosopher4 = Philosopher("Marx", fork4, fork5)
philosopher5 = Philosopher("Russell", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()

"""
'Kant' has started thinking
'Aristotle' has started thinking
'Marx' has started thinking
'Spinoza' has started thinking
'Russell' has started thinking
'Russell' has finished thinking
'Aristotle' has finished thinking
'Spinoza' has finished thinking
'Marx' has finished thinking
'Russell' has acquired the left fork
'Russell' has attained both forks, currently eating
'Russell' has released the right fork
'Russell' has released the left fork
'Marx' has acquired the left fork
'Marx' has attained both forks, currently eating
'Marx' has released the right fork
'Marx' has released the left fork
'Kant' has finished thinking
'Marx' has finished thinking
'Aristotle' has acquired the left fork
'Marx' has acquired the left fork
'Marx' has attained both forks, currently eating
'Marx' has released the right fork
'Marx' has released the left fork
'Marx' has finished thinking
'Spinoza' has acquired the left fork
'Russell' has finished thinking
'Marx' has acquired the left fork
'Kant' has acquired the left fork
'Russell' has acquired the left fork
"""
