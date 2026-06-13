# Import all functions from do_something.py (contains the random list generator)
from do_something import *
# Import time module to measure execution duration
import time
# Import threading module to run tasks in threads (parallel execution within one process)
import threading

# Ensure this code runs only when executed directly (not imported)
if __name__ == "__main__":
       # Start recording time 
    start_time = time.time()
      # Number of random numbers each thread will generate
    size = 10000000
      # Number of threads we have to run in parallel
    threads = 10  
     # List to store all thread objects so we can start and join them later
    jobs = []
   # now Creating multiple threads
    for i in range(0, threads):
         # Each thread has its own separate output list
        out_list = list()
          # Create a new thread used for running do_something with arguments size and out_list
        thread = threading.Thread(target=do_something(size, out_list))
         # now add the thread to the jobs list
        jobs.append(thread)
     
    # Start all threads one by one   
    for j in jobs:
        j.start()

# now we Wait for all threads to finish
    for j in jobs:
        j.join()
# after all list processing is complete we print acknolegement msg
    print ("List processing complete.")
     # Record end time 
    end_time = time.time()
    #print the time taken by all threads
    print("multithreading time=", end_time - start_time)
	

# output  
# List processing complete.
# multithreading time= 9.366768836975098

#This code demonstrates using multithreading in Python to run a function (do_something) that generates large lists of random numbers in parallel within a single process. 
# It creates a specified number of threads, each with its own separate list, and starts them almost simultaneously.
#  The program waits for all threads to complete using join() before printing a completion message. 
# The time module is used to record the start and end times to measure how long the multithreading execution takes.
#  here it illustrates thread creation, parallel execution within one process, and timing of concurrent tasks.