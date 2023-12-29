import threading
import time


def my_thread(my_event: threading.Event):
    while not my_event.is_set():
        print("Waiting for Event to be set")
        time.sleep(1)
    print("my_event has been set")


def main():
    """
    이벤트는 동시적으로 실행되는 여러 스레드 사이의 간단한 통신 형태에 유용
    isSet() : 이벤트 세팅여부
    set() : 이벤트 세팅
    clear() : 이벤트 객체 리셋
    wait() : 내부 플래그가 참이 될 때까지 블로킹
    """
    my_event = threading.Event()  # 모든 자식 객체를 지니는
    thread = threading.Thread(target=my_thread, args=(my_event,))
    thread.start()
    time.sleep(5)

    my_event.set()  # 자식스레드 종료


if __name__ == "__main__":
    main()

    # Waiting for Event to be set
    # Waiting for Event to be set
    # Waiting for Event to be set
    # Waiting for Event to be set
    # Waiting for Event to be set
    # my_event has been set
