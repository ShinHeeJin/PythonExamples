import threading
import time

import requests


class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), "chars")


def main():
    t = HtmlGetter("http://google.com")
    t.start()


if __name__ == "__main__":
    main()
