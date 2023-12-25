import threading
import time

counter = 0

semaphore = threading.BoundedSemaphore(value=10)


def increment_counter(thread_name):
    global counter
    with semaphore:
        print(f"Thread {thread_name} is incrementing the counter")
        time.sleep(1)
        counter += 1
        print(f"Trhead {thread_name} incremented the counter. Current value: {counter}")


threads: list[threading.Thread] = []
for i in range(100):
    thread = threading.Thread(target=increment_counter, args=(i,))
    threads.append(thread)
    thread.start()

thread.join()
for thread in threads:
    thread.join()

print("Final counter value:", counter)
