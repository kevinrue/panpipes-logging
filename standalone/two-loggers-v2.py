# can two loggers write to the same file?

import logging

handler1 = logging.FileHandler("1.log")
logger1 = logging.getLogger("logger1")
logger1.setLevel(logging.INFO)
logger1.addHandler(handler1)

handler2 = logging.FileHandler("2.log")
logger2 = logging.getLogger("logger2")
logger2.setLevel(logging.INFO)
logger2.addHandler(handler2)

logger1.debug("Log test using L.debug")
logger1.info("Log test using L.info") # this is written 1.log
print("Log test using print")

logger2.debug("Log test using L2.debug") # this is written 2.log
logger2.info("Log test using L2.info")

# the two log files contain the correct information
