import random
import threading
import time


def executedThread(i):
    print(f"Thread {i} started")
    time.sleep(random.randint(1, 10))
    print(f"Thread {i} finished")


for i in range(10):
    thread = threading.Thread(target=executedThread, args=(i,))
    thread.start()
    print(f"Active Threads : {threading.enumerate()}")
    print(f"Active Thread Count : {threading.active_count()}")
