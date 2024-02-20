import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

# Logger 생성
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# StreamHandler 생성 및 추가
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)


file_handler = logging.FileHandler("dummy.log")
logger.addHandler(file_handler)

logger.info("This message will be logged and printed to the console and writed to dummy.log")
