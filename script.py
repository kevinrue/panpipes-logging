import logging
import sys

from cgatcore.experiment import MultiLineFormatter

# quick and dirty toggle to log to stdout
log_to_stdout = False
log_to_pipeline_log = True

# Set up a logger that write to standard output
# This will be redirected to the task log file by the pipeline
if log_to_stdout:
    handler_stdout = logging.StreamHandler(sys.stdout)
    logger_stdout = logging.getLogger("stdout")
    logger_stdout.setLevel(logging.INFO)
    logger_stdout.addHandler(handler_stdout)

# Set up a logger that writes to the pipeline.log file
if log_to_pipeline_log:
    handler_pipeline_log = logging.FileHandler("pipeline.log") #  point to file
    handler_pipeline_log.setFormatter( # mimic the cgatcore formatter for pipeline.log
                MultiLineFormatter(
                    "%(asctime)s %(levelname)s " # time and log level
                    "log %(module)s " # 'log' replaces the 'app_name' field, which is usually 'main' or the name of the pipeline
                    "- %(message)s")) # actual log message
    logger_pipeline = logging.getLogger("pipeline") # get a dedicated logger for the pipeline (i.e., not the root logger)
    logger_pipeline.setLevel(logging.INFO) # set the logging level
    logger_pipeline.addHandler(handler_pipeline_log) # add the file handler to the logger

if log_to_stdout:
    logger_stdout.debug("Log test using logger_stdout.debug") # this will not be logged due to its DEBUG level
    logger_stdout.info("Log test using logger_stdout.info") #  this will be logged to the task log file (because stdout is redirected to the task log file)
    print("Log test using print") # this will be logged to the task log file (because stdout is redirected to the task log file) - bad practice to print though!

if if log_to_pipeline_log:
    logger_pipeline.debug("Log test using logger_pipeline.debug") # this will not be logged due to its DEBUG level
    logger_pipeline.info("Log test using logger_pipeline.info") # this will be logged to the pipeline.log file
    logger_pipeline.info("script.py logging to file 'logs/test.out'") # this will be logged to the pipeline.log file - this is the logging message we care about!
    # TODO: pass 'logs/test.out' from pipeline_logging.py to script.py instead of hard coding it

# Create the expected output file with dummy content
# TODO: pass 'results/test.txt' from pipeline_logging.py to script.py instead of hard coding it
with(open("results/test.txt", "w")) as f:
    print(f.write("Hello, world!"))
