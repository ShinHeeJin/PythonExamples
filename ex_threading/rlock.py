import threading
import time


class myWorker:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock()

    def modifyA(self):
        with self.rlock:
            print(f"Modifying A : RLock Acquired: {self.rlock._is_owned()}")
            print(f"{self.rlock}")  # <locked _thread.RLock object owner=140704365504256 count=2 at 0x109ae0780>
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.rlock:
            print(f"Modifying B : RLock Acquired: {self.rlock._is_owned()}")
            print(f"{self.rlock}")  # <locked _thread.RLock object owner=140704365504256 count=2 at 0x109ae0780>
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.rlock:
            print("Rlock acquired, modifying A and B")
            print(f"{self.rlock}")  # <locked _thread.RLock object owner=140704365504256 count=1 at 0x109ae0780>
            self.modifyA()
            print(f"{self.rlock}")  # <locked _thread.RLock object owner=140704365504256 count=1 at 0x109ae0780>
            self.modifyB()
        print(f"{self.rlock}")  # <unlocked _thread.RLock object owner=0 count=0 at 0x109ae0780>


workerA = myWorker()
workerA.modifyBoth()

"""
Rlock acquired, modifying A and B
<locked _thread.RLock object owner=140704365504256 count=1 at 0x109ae0780>
Modifying A : RLock Acquired: True
<locked _thread.RLock object owner=140704365504256 count=2 at 0x109ae0780>
<locked _thread.RLock object owner=140704365504256 count=1 at 0x109ae0780>
Modifying B : RLock Acquired: True
<locked _thread.RLock object owner=140704365504256 count=2 at 0x109ae0780>
<unlocked _thread.RLock object owner=0 count=0 at 0x109ae0780>
"""
