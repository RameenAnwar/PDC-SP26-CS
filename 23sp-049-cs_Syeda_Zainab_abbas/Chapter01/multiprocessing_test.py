# multiprocessing_test.py
# MULTIPROCESSING version. Creates 10 separate processes (each with its own
# Python interpreter and memory). This bypasses the GIL, so CPU-bound work
# can truly run in parallel across multiple cores.

from do_something import *
import time
import multiprocessing            # Python's process-based parallelism module

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    procs = 10                     # number of processes to spawn
    jobs = []

    # Create the process objects (target = function, args = its arguments).
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    # Start all processes (they begin running in parallel).
    for j in jobs:
        j.start()

    # Wait for all processes to complete.
    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
