import logging
import traceback

# 1. logging.exception
"""
ERROR:root:Exception occured
Traceback (most recent call last):
  File "D:test.py", line 2, in <module>
    0 / 0
ZeroDivisionError: division by zero
"""
try:
    0 / 0
except Exception:
    logging.exception("Exception occured")

# 1.1 logging.error(msg, exc_info=True)
"""
ERROR:root:Exception occured
"""
try:
    0 / 0
except Exception:
    logging.error("Exception occured", exc_info=True)

# 2. logging.error
"""
ERROR:root:Exception occured
"""
try:
    0 / 0
except Exception:
    logging.error("Exception occured")

# 3. logging.error(e)

"""
ERROR:root:division by zero
"""
try:
    0 / 0
except Exception as e:
    logging.error(e)


# 4. print(e)
"""
division by zero
"""
try:
    0 / 0
except Exception as e:
    print(e)


# 5. trace.format_exec()
"""
ERROR:root:Traceback (most recent call last):
  File "D:test.py", line 4, in <module>
    0 / 0
ZeroDivisionError: division by zero
"""
try:
    0 / 0
except Exception:
    error_msg = traceback.format_exc()
    logging.error(error_msg)
