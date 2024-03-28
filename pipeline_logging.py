#! /usr/bin/env python

from ruffus import *
from cgatcore import pipeline as P
import os
import sys

PARAMS = P.get_parameters(
    ["%s/pipeline.yml" % os.path.splitext(__file__)[0],
     "pipeline.yml"])
PARAMS['py_path'] =  os.path.realpath(os.path.dirname(__file__))
# PARAMS = {
#     "py_path": os.path.realpath(os.path.dirname(__file__)),
# }
print(PARAMS)

job_kwargs = {
    "job_condaenv": "cgatcore",
}
print(job_kwargs)


@follows(mkdir("logs"))
@originate("logs/test.log")
def test(outfile):
    """this is to aggregate all the cellranger multi metric_summary files
    it also does some plotting
    """
    errfile = outfile.replace(".log", ".err")

    cmd = """
        python %(py_path)s/script.py
            2> %(errfile)s > %(outfile)s
            """
    job_kwargs["job_threads"] = 1
    P.run(cmd, **job_kwargs)


@follows(test)
#@originate("ruffus.check")
def full():
    """
    All cgat pipelines should end with a full() function which updates,
    if needed, all branches of the pipeline.
    The @follows statement should ensure that all functions are covered,
    either directly or as prerequisites.
    """
    #IOTools.touch_file(file)
    pass

if __name__ == "__main__":
    sys.exit(P.main(sys.argv))