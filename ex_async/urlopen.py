import time
from urllib.request import Request, urlopen


def main():
    urls = [
        "https://www.google.co.kr/search?q=" + i
        for i in ["apple", "pear", "grape", "pineapple", "orange", "strawberry"]
    ]

    begin = time.time()
    result = []
    for url in urls:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})  # UA가 없으면 403 발생
        response = urlopen(request)
        page = response.read()
        result.append(len(page))

    print(result)
    end = time.time()
    print(f"excuted time : {end - begin: .3f}")


if __name__ == "__main__":
    main()
