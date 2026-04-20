# Import function from file
from do_something import *

# Import time module to measure execution time
import time

# Import threading module
import threading


# Ensure this runs only when file is executed directly
if __name__ == "__main__":

    # Record start time
    start_time = time.time()

    # Number of random values per thread
    size = 10000000

    # Number of threads
    threads = 10  

    # List to store thread objects
    jobs = []

    # Create threads
    for i in range(0, threads):

        # Each thread gets its own list
        out_list = list()

        # Create thread (PASS FUNCTION, don't call it)
        thread = threading.Thread(
            target=do_something,       # function reference
            args=(size, out_list)     # arguments for function
        )

        # Add thread to jobs list
        jobs.append(thread)


    # Start all threads
    for j in jobs:
        j.start()

    # Wait for all threads to complete
    for j in jobs:
        j.join()

    # Print completion message
    print("List processing complete.")

    # Record end time
    end_time = time.time()

    # Print total execution time
    print("multithreading time=", end_time - start_time)