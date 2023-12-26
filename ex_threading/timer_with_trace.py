import sys
import threading
import time


class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if self.killed:
            print("globaltrace exit")
            raise SystemExit()

    def localtrace(self, frame, event, arg):
        if self.killed:
            print("localtrace exit")
            raise SystemExit()

    def kill(self):
        self.killed = True


class MyScheduler:
    seperate_line = "-" * 50

    def __init__(self):
        self.lock = threading.Lock()
        self.function_interval = 0.5
        self.timer_stopped = False
        self.timer_stop = False

    def timer_func(self):
        self.lock.acquire()

        if self.timer_stop:
            self.lock.release()
            self.timer_stop = False
            return

        thread_create_time = time.time()
        main_logic_thread = thread_with_trace(target=self.main_logic, args=([thread_create_time]))
        main_logic_thread.start()
        main_logic_thread.join(timeout=10)

        if not self.timer_stopped:
            threading.Timer(self.function_interval, self.timer_func).start()

        self.lock.release()

    def main_logic(self, started_time):
        print(f"main logic executed: {started_time}, {threading.current_thread().name}")


def main():
    scheduler = MyScheduler()
    scheduler.timer_func()


if __name__ == "__main__":
    main()
    print("Main Thread end")
