import random
import threading
import time


def executedThread(i):
    print(f"Current Thread : {threading.current_thread()}")
    # # Current Thread : <Thread(Thread-10 (executedThread), started 123145542021120)>

    print(f"Thread {i} started")
    time.sleep(random.randint(1, 10))
    print(f"Thread {i} finished")


for i in range(10):
    thread = threading.Thread(target=executedThread, args=(i,))
    thread.start()
    print(f"Active Threads : {threading.enumerate()}")
    # [<_MainThread(MainThread, started 140704300631808)>, <Thread(Thread-1 (executedThread), started 123145390915584)>]

    print(f"Active Thread Count : {threading.active_count()}")  # 2
