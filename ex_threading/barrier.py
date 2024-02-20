import random
import threading
import time
from typing import Final

"""
- 베리어는 컨디션 및 세마포어의 복잡한 조합으로 문제를 해결
- 모든 스레드내의 작업이 스레드 그룹에 의해 생서되었는지 보장한다.
- 아래 예제에서 베리어를 활용해 모든 스레드가 원하는 실행 포인트에 도달하기 까지 해당 스레드의 실행을 맏는다.
"""


class myThread(threading.Thread):
    def __init__(self, barrier: threading.Barrier):
        super().__init__()
        self.barrier = barrier  # 배리어가 해제되기 전, 배어에서 대기하는 스레드의 갯수

    def run(self):
        print(f"Thread {threading.current_thread()} working on something")
        time.sleep(random.randint(1, 10))
        print(f"Thread {threading.current_thread()} is joinning {self.barrier.n_waiting}")
        self.barrier.wait()  # 4개의 스레드가 모두 대기한다.

        print("Barrier has been lifted, continuing with work")


PARTIES: Final[int] = 3
barrier = threading.Barrier(parties=PARTIES)
threads = []

for i in range(PARTIES):
    thread = myThread(barrier)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
