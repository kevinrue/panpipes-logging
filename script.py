import argparse
import logging
import sys

# Set up a logger that write to standard output
# This will be redirected to the task log file by the pipeline
L = logging.getLogger()
L.setLevel(logging.INFO)
log_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
L.addHandler(log_handler)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--output_file',
                    default='',
                    help='')
parser.set_defaults(verbose=True)
args = parser.parse_args()

L.info(args)

L.debug("Log test using L.debug") # this will not be logged due to its DEBUG level
L.info("Log test using L.info") #  this will be logged to the task log file (because stdout is redirected to the task log file)
print("Print something using print") # this will be logged to the task log file (because stdout is redirected to the task log file) - bad practice to print though!

# Create the expected output file with dummy content
# TODO: pass 'results/test.txt' from pipeline_logging.py to script.py instead of hard coding it
with(open(args.output_file, "w")) as f:
    f.write("Hello, world!")
