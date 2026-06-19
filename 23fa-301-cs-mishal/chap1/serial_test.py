# Import time module to measure execution duration
import time
# Import all functions from do_something.py (contains the random list generator)
from do_something import *
# Ensure this code runs only when executed directly (not imported)
if __name__ == "__main__":
    # Start recording time
    start_time = time.time()
    # Num of random numbers each execution will generate
    size = 10000000   
     # Num of times the function will run sequentially
    n_exec = 10
      # Run the function multiple times one by one 
    for i in range(0, n_exec):
        # Each execution has its own separate output list
        out_list = list()
          # Call the function do_something with size and out_list
        do_something(size, out_list)
       
 # Print acknowledgment message after all list processing is complete
    print ("List processing complete.")
    # Record end time 
    end_time = time.time()
       # Print the total time taken for serial execution
    print("serial time=", end_time - start_time)

# output
# List processing complete.
# serial time= 8.755433320999146

#This code demonstrates serial execution of the do_something function, where it generates large lists of random numbers multiple times one after another.
#  Each run uses its own separate list. The time module is used to measure how long all executions take in total. 
# This example highlights the difference between running tasks sequentially versus using threads or processes, 
# showing that serial execution takes longer for large, repetitive tasks since nothing runs in parallel.