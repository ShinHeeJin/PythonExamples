import logging

# logging.Filter를 상속받아 filter 메소드를 구현한다.
# filter 메소드가 True를 반환하는 경우에만 로그를 기록한다.


class RecordFilter(logging.Filter):
    def filter(self, record):
        return "!!!" in record.msg


logger = logging.getLogger(__name__)
logger.addFilter(RecordFilter())

logger.warning("warning !!!")  # logged
logger.warning("warning")  # unlogged
