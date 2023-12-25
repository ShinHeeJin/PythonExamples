"""
세마포어란 요청 및 릴리스 호출이 있을때 마다 증감되는 카운터다. 카운터는 음수가 될 수 없다.
세마포어를 통해 코드를 블로킹하면 카운터는 2가된다.
"""
import random
import threading
import time


class TicketSeller(threading.Thread):
    ticketsSold = 0

    def __init__(self, semaphore: threading.Semaphore, **kwargs):
        super().__init__(**kwargs)
        self.semaphore = semaphore
        print(f"Ticket Seller {self.name} Started work")

    def run(self):
        running = True
        while running:
            self.random_delay()
            self.semaphore.acquire()
            if ticketsAvailable <= 0:
                running = False
            else:
                self.sell()
            self.semaphore.release()
        print(f"Ticket Seller {self.name} Sold {self.ticketsSold} tickets in total")

    def random_delay(self):
        time.sleep(random.randint(0, 4) / 4)

    def sell(self):
        global ticketsAvailable
        self.ticketsSold += 1
        ticketsAvailable -= 1
        print(f"{self.name} Sold One ({ticketsAvailable} left)")


semaphore = threading.Semaphore()
ticketsAvailable = 20

sellers: list[TicketSeller] = []
for i in range(4):
    seller = TicketSeller(semaphore, name=f"{i} seller")
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()
