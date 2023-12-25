"""
세마포어란 요청 및 릴리스 호출이 있을때 마다 증감되는 카운터다. 카운터는 음수가 될 수 없다.
세마포어를 통해 코드를 블로킹하면 카운터는 2가된다.
"""
import random
import threading
import time


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
            with self.semaphore:
                if tickets_available > 0:
                    self.sell()
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
