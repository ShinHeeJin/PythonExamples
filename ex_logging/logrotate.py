import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# fmt: off

# 1)
#   로그 파일의 용량이 2KB를 넘을 때마다 roll over
#   5개 백업파일을 유지하면서 roll over 한다. app.log.1, app.log.2 ... app.log.5

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for idx in range(10000):
    logger.info(f"{idx}")

# 2.
#   when * interval 단위로 roll over
#   5개 백업파일을 유지하면서 roll over 한다.
handler = TimedRotatingFileHandler("timed_test.log", when="m", interval=1, backupCount=5)  # 매 1분, 5개 파일 백업(5분)
# handler = TimedRotatingFileHandler("timed_test.log", when="s", interval=5, backupCount=5) # 매 5초, 5개 파일 백업(25초)
# handler = TimedRotatingFileHandler("timed_test.log", when="h", interval=2, backupCount=10) # 매 2시간, 5개 파일 백업(10시간)
logger.addHandler(handler)

cnt = 0
while True:
    logger.info(cnt)
    cnt += 1
