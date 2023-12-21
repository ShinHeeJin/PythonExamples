import time
import threading

def single_process_single_thread_sum():
    """
    하나의 프로세스에서 하나의 스레드로 1억까지 더한다.
    """
    increased_num = 0
    start_time = time.time()
    for _ in range(100000000):
        increased_num += 1

    print("--- %s seconds ---" % (time.time() - start_time))

    print("increased_num=",end=""), print(increased_num)
    print("end of single_process_single_thread_sum")

shared_number = 0

def thread_1(number):
    global shared_number
    for _ in range(number):
        shared_number += 1

def thread_2(number):
    global shared_number
    for _ in range(number):
        shared_number += 1

def single_process_two_thead_sum():
    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(50000000,) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,) )
    t2.start()
    threads.append(t2)


    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print(f"{shared_number=}")
    print("end of single_process_two_thead_sum")


if __name__ == "__main__":
    single_process_single_thread_sum()
    single_process_two_thead_sum()
