from do_something import *     # Import function from another file
import time                    # Import time module to measure execution time
import threading               # Import threading module


# Main block
if __name__ == "__main__":
    start_time = time.time()     # Record start time

    size = 10000000     # Number of iterations for each thread
    threads = 10        # Total number of threads
    jobs = []           # List to store thread objects

    # Create threads
    for i in range(0, threads):
        out_list = list()     # Create empty list for each thread

        # Create a thread (function will run in parallel)
        thread = threading.Thread(target=do_something(size, out_list))

        jobs.append(thread)     # Add thread to list

    # Start all threads
    for j in jobs:
        j.start()

    # Wait for all threads to complete
    for j in jobs:
        j.join()

    print("List processing complete.")     # Print completion message

    end_time = time.time()     # Record end time
    print("multithreading time=", end_time - start_time)     # Print total time
