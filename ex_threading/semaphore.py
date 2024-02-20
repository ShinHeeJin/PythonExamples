import random
import threading
import time

"""
여러개의 프로세스/스레드가 공유자원에 동시에 접근하는 것을 제한하기위한 정수
P(Produce) 연산은 세마포어 값을 감소시키며 공유자원을 점유한다.
V(Consume) 연산은 세마포어 값을 증가시키며 공유자원을 해제한다.

이제 세마포어(0,1)의 경우 최대 한개의 스레그가 접근가능하며
카운팅 세마포어의 경우 최대 n개의 스레드가 접근 가능한 세마포어이다.

보통 공유자원 접근 수를 조절하고, 작업간의 실행순서 동기화가 필요한경우 사용된다.

cf. 뮤텍스 vs 이진 세마포어
ex. 아래 예제에서는 tickets_available 변수에 동시접근을 제한한다.
ref. https://www.youtube.com/watch?v=NL9JQh5bbZ8
"""


class TicketSeller(threading.Thread):
    tickets_sold = 0

    def __init__(self, semaphore: threading.Semaphore, **kwargs):
        super().__init__(**kwargs)
        self.semaphore = semaphore
        print(f"Ticket Seller {self.name} Started work")

    def run(self):
        global tickets_available
        while tickets_available > 0:
            self.random_delay()
            with self.semaphore:  # 감소 : self.semaphore.acquired() -> self._value -= 1
                if tickets_available > 0:
                    self.sell()
            # 증가 : self.semaphore.release(n) -> self._value += n ( default n=1 )
        print(f"Ticket Seller {self.name} Sold {self.tickets_sold} tickets in total")

    def random_delay(self):
        time.sleep(random.randint(0, 4) / 4)

    def sell(self):
        global tickets_available
        self.tickets_sold += 1
        tickets_available -= 1
        print(f"{self.name} Sold One ({tickets_available} left)")


semaphore = threading.Semaphore()
tickets_available = 20

sellers: list[TicketSeller] = []
for i in range(4):
    seller = TicketSeller(semaphore, name=f"{i} seller")
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()
