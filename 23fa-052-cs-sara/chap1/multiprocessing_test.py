# Import everything from do_something file (function we defined earlier)
from do_something import *

# Import time module to measure execution time
import time

# Import multiprocessing module to run tasks in parallel
import multiprocessing


# This ensures the code runs only when this file is executed directly
if __name__ == "__main__":

    # Record start time
    start_time = time.time()

    # Number of random values each process will generate
    size = 10000000   

    # Number of processes to run in parallel
    procs = 10   

    # List to store process objects
    jobs = []

    # Create processes
    for i in range(0, procs):

        # Create an empty list for each process
        out_list = list()

        # Create a process that runs do_something function
        # target = function to execute
        # args = arguments passed to the function
        process = multiprocessing.Process(
            target=do_something,
            args=(size, out_list)
        )

        # Add process to jobs list
        jobs.append(process)


    # Start all processes (run in parallel)
    for j in jobs:
        j.start()


    # Wait for all processes to finish
    for j in jobs:
        j.join()


    # Print completion message
    print("List processing complete.")

    # Record end time
    end_time = time.time()

    # Print total execution time
    print("multiprocesses time=", end_time - start_time)