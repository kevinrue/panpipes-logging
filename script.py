import sys

import logging
L = logging.getLogger()
L.setLevel(logging.INFO)
log_handler = logging.StreamHandler(sys.stdout)
L.addHandler(log_handler)

L.debug("Log test using L.debug")
L.info("Log test using L.info")
# L.message("Log test using L.message")
print("Log test using print")