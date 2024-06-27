import time
from threading import Event, Thread

pause_event = Event()
stop_event = Event()


def worker(stop_event: Event, pause_event: Event):
    print("start!!!")
    while not stop_event.is_set():
        if pause_event.is_set():
            print("wait ...")
            pause_event.wait()
        else:
            print("logic executed")
        time.sleep(1)


def main():
    """
    stop_event과 pause_event Event를 활용하여 스레드에 대해서
    일시정지, 재개, 종료 인터페이스를 구현한다.
    """
    thread = Thread(target=worker, args=(stop_event, pause_event))
    thread.start()

    time.sleep(3)
    print("Pause !!!")
    pause_event.set()

    time.sleep(3)
    print("Resume !!!")
    pause_event.clear()

    time.sleep(3)
    print("Pause !!!")
    pause_event.set()

    time.sleep(3)
    print("Stop!!!")
    stop_event.set()

    thread.join()


if __name__ == "__main__":
    main()

# start!!!
# logic executed
# logic executed
# logic executed
# Pause !!!
# wait ...
# wait ...
# wait ...
# Resume !!!
# logic executed
# logic executed
# logic executed
# Pause !!!
# wait ...
# wait ...
# wait ...
# Stop!!!
