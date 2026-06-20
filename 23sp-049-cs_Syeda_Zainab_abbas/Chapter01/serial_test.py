# serial_test.py
# SERIAL (single-threaded) version. Runs the workload 10 times one-after-another
# on a single core, then prints how long it took. This is our baseline.

import time                       # used to measure execution time
from do_something import *        # import the do_something() helper

if __name__ == "__main__":        # run only when executed directly, not on import
    start_time = time.time()      # record the start timestamp
    size = 10000000               # how many random numbers per run (10 million)
    n_exec = 10                   # number of times we repeat the workload

    # Run the workload sequentially: each iteration must finish before the next.
    for i in range(0, n_exec):
        out_list = list()         # fresh empty list each iteration
        do_something(size, out_list)

    print("List processing complete.")
    end_time = time.time()        # record the end timestamp
    # Total wall-clock time = end - start (serial is usually the slowest here)
    print("serial time=", end_time - start_time)
