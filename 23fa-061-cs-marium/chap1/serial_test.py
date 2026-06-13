import time  # Used to measure how long the program takes
from do_something import *  # Import everything from do_something module

if __name__ == "__main__":  # Run this part only if this file is run directly
    start_time = time.time()  # Start time of the program
    size = 10000000   # Set the size for processing
    n_exec = 10  # Number of times to run the function
    for i in range(0, n_exec):  # Repeat the following steps n_exec times
        out_list = list()  # Make an empty list to store results
        do_something(size, out_list)  # Call the function to do some work
       
    print ("List processing complete.")  # Print message when done
    end_time = time.time()  # End time of the program
    print("serial time=", end_time - start_time)  # Show total time taken