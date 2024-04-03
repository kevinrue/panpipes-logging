import logging
import sys

from cgatcore.experiment import MultiLineFormatter

# Set up a logger that write to standard output
# This will be redirected to the task log file by the pipeline
handler_stdout = logging.StreamHandler(sys.stdout)
logger_stdout = logging.getLogger("stdout")
logger_stdout.setLevel(logging.INFO)
logger_stdout.addHandler(handler_stdout)

# Set up a logger that writes to the pipeline.log file
handler_pipeline_log = logging.FileHandler("pipeline.log")
handler_pipeline_log.setFormatter(
            MultiLineFormatter(
                "%(asctime)s %(levelname)s "
                "log %(module)s "
                "- %(message)s"))
logger_pipeline = logging.getLogger("pipeline")
# logger_pipeline = logging.getLogger("cgatcore.pipeline")
logger_pipeline.setLevel(logging.INFO)
logger_pipeline.addHandler(handler_pipeline_log)

logger_stdout.debug("Log test using logger_stdout.debug")
logger_stdout.info("Log test using logger_stdout.info")
print("Log test using print")

logger_pipeline.debug("Log test using logger_pipeline.debug")
logger_pipeline.info("Log test using logger_pipeline.info")
logger_pipeline.info("script.py logging to file 'logs/test.out'") #  This is the logging message we care about

# TODO: pass 'results/test.txt' from pipeline_logging.py to script.py
with(open("results/test.txt", "w")) as f:
    print(f.write("Hello, world!"))
