"""
파이썬에서 쓰레드를 실행하기 위해서는, threading 모듈의 threading.Thread() 함수를 호출하여 Thread 객체를 얻은 후
Thread 객체의 start() 메서드를 호출하면 된다. 서브쓰레드는 함수 혹은 메서드를 실행하는데, 일반적인 구현방식으로
(1) 쓰레드가 실행할 함수 혹은 메서드를 작성하거나 또는
(2) threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식 등이 있다.
"""

import threading


def my_sum(a, b):
    count = 0
    for i in range(a, b + 1):
        count += i
    return count


def main():
    thread = threading.Thread(target=my_sum, args=(1, 10))
    print("Sub Thread start")
    thread.start()


if __name__ == "__main__":
    main()
    print("Main Thread")
