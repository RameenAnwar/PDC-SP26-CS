# multithreading_test.py
# MULTITHREADING version. Creates 10 threads that each run the workload.
# NOTE: Because of Python's GIL (Global Interpreter Lock), CPU-bound work like
# this does NOT actually speed up with threads - threads are best for I/O-bound work.

import time
import threading                  # Python's threading module
from do_something import *

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    threads = 10                  # number of threads to create
    jobs = []                     # list to keep references to all threads

    # Create the thread objects.
    for i in range(0, threads):
        out_list = list()
        # Build a Thread whose target is our helper function.
        thread = threading.Thread(target=do_something(size, out_list))
        jobs.append(thread)

    # Start every thread.
    for j in jobs:
        j.start()

    # join() waits for each thread to finish before moving on.
    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
