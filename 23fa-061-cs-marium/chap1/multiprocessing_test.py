from do_something import *     # Import function from another file
import time                    # Import time module to measure execution time
import multiprocessing         # Import multiprocessing module


# Main block (runs only when file is executed directly)
if __name__ == "__main__":
    start_time = time.time()     # Record start time

    size = 10000000     # Number of iterations for each process
    procs = 10          # Total number of processes to run
    jobs = []           # List to store process objects

    # Create processes
    for i in range(0, procs):
        out_list = list()     # Create empty list for each process

        # Create a new process with target function
        process = multiprocessing.Process(
            target=do_something, args=(size, out_list)
        )

        jobs.append(process)     # Add process to list

    # Start all processes
    for j in jobs:
        j.start()

    # Wait for all processes to finish
    for j in jobs:
        j.join()

    print("List processing complete.")     # Print completion message

    end_time = time.time()     # Record end time
    print("multiprocesses time=", end_time - start_time)     # Print total time taken
