import threading
import time

import requests


class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        self.resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(self.resp.text), "chars")

    def get_resp(self):
        return self.resp


def main():
    t = HtmlGetter("http://google.com")
    t.start()
    t.join()
    resp = t.get_resp()
    print(f"{resp.status_code=}")


if __name__ == "__main__":
    main()
