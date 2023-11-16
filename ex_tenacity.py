# github : https://github.com/jd/tenacity

from tenacity import (
    after_log,
    before_log,
    before_sleep_log,
    retry_if_exception_type,
    retry_if_not_exception_type,
    retry_if_result,
    retry,
    stop_after_attempt,
    stop_after_delay,
    wait_exponential,
    wait_fixed,
    wait_random,
    Retrying,
    RetryError,
)
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyError(Exception):
    pass


@retry(
    stop=(stop_after_attempt(max_attempt_number=5) | stop_after_delay(20)),
    wait=wait_fixed(wait=5) + wait_random(min=0, max=5),
    reraise=True,
    before=before_log(logger, logging.DEBUG),
)
def func():
    print("func executed")
    raise MyError("my error in func ")


def func2(arg):
    print(f"func2 executed, arg : {arg}")
    raise MyError("my error in func2")


if __name__ == "__main__":
    # case 1
    func.retry_with(stop=stop_after_attempt(4))()  # 런타임에서 옵션 변경

    # case 2
    retryer = Retrying(stop=stop_after_attempt(3), reraise=True)
    retryer(func2, "test arg")

    # case 3
    try:
        for attemp in Retrying(stop=stop_after_attempt(3)):
            with attemp:
                raise MyError("my error in code block")
    except RetryError:
        pass
