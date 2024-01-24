import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

# Logger 생성
logger = logging.getLogger("test")

# StreamHandler 생성 및 추가
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.info("This message will be logged and printed to the console.")
# This message will be logged and printed to the console.
# INFO:test:This message will be logged and printed to the console.
