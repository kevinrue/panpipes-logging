# can two loggers write to the same file?

import logging

L = logging.getLogger()
L.setLevel(logging.INFO)
log_file_handler1 = logging.FileHandler("1.log")
L.addHandler(log_file_handler1)

L2 = logging.getLogger()
L2.setLevel(logging.INFO)
log_file_handler2 = logging.FileHandler("2.log")
L2.addHandler(log_file_handler2)

L.debug("Log test using L.debug")
L.info("Log test using L.info") # this is written to both 1.log and 2.log
print("Log test using print")

L2.debug("Log test using L2.debug") # this is written to both 1.log and 2.log
L2.info("Log test using L2.info")

# the two log files contain the same information (see above)