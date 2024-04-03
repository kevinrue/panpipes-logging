import sys

import logging

handler_stdout = logging.StreamHandler(sys.stdout)
logger_stdout = logging.getLogger("stdout")
logger_stdout.setLevel(logging.INFO)
logger_stdout.addHandler(handler_stdout)

handler_pipeline_log = logging.FileHandler("pipeline.log")
logger_pipeline = logging.getLogger("pipeline")
logger_pipeline.setLevel(logging.INFO)
logger_pipeline.addHandler(handler_pipeline_log)

logger_stdout.debug("Log test using logger_stdout.debug")
logger_stdout.info("Log test using logger_stdout.info")
print("Log test using print")

logger_pipeline.debug("Log test using logger_pipeline.debug")
logger_pipeline.info("Log test using logger_pipeline.info")

# TODO: pass 'results/test.txt' from pipeline_logging.py to script.py
with(open("results/test.txt", "w")) as f:
    print(f.write("Hello, world!"))
