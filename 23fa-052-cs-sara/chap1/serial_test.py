# Import time module to measure execution time
import time

# Import function from do_something file
from do_something import *


# Ensure this runs only when file is executed directly
if __name__ == "__main__":

    # Record start time
    start_time = time.time()

    # Number of random values to generate each time
    size = 10000000   

    # Number of times the function will run (serially)
    n_exec = 10

    # Loop runs one by one (no parallelism)
    for i in range(0, n_exec):

        # Create a new empty list each time
        out_list = list()

        # Call function normally (no threads, no processes)
        do_something(size, out_list)


    # Print completion message
    print("List processing complete.")

    # Record end time
    end_time = time.time()

    # Print total execution time
    print("serial time=", end_time - start_time)