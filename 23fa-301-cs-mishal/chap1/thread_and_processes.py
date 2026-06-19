import os
# Import time module to measure execution duration
import time
# Import threading module for running tasks in threads
import threading
# Import multiprocessing module for running tasks in separate processes
import multiprocessing
# Import random module to generate random numbers
import random
 
 # Number of workers  denote  num of (threads/processes) to run in parallel
NUM_WORKERS = 10
# Number of random numbers each execution will generate
size = 10000000
# Shared list to store output (all numbers appended here)
out_list = list()
# Function to generate random numbers and append to out_list
def do_something(count, out_list):
	for i in range(count):
		out_list.append(random.random())

#Serial
# start recordinf time for serial execution
start_time = time.time()
# Run the function multiple times one by one 
for _ in range(NUM_WORKERS):
    do_something(size,out_list)
 #record end time time for serial execution and print total execution time
end_time = time.time()
print("Serial time=", end_time - start_time)


#MultiThreading
# Record start time for threading
start_time = time.time()
# List to store thread objects
jobs = []
# Create threads
for i in range(0, NUM_WORKERS):
     # Create a new thread to run do_something with size and out_list
    thread = threading.Thread(target=do_something(size, out_list))
      # Add thread to jobs list
    jobs.append(thread)
 # Start all threads   
for j in jobs:
    j.start()
 # Wait for all threads to finish   
for j in jobs:
    j.join()
# Print completion message for threading
print ("List processing complete.")
# Record end time and calculate threading duration and print
end_time = time.time()
print("threading time=", end_time - start_time)


#MultiProcesses
# Record start time for multiprocessing
start_time = time.time()

# List to store process objects
jobs = []
# Create processes
for i in range(0, NUM_WORKERS):
      # Create a new process to run do_something with size and out_list
    process = multiprocessing.Process\
              (target=do_something,args=(size,out_list))
    # Add process to jobs list
    jobs.append(process)
# Start all processes
for j in jobs:
    j.start()
# Wait for all processes to finish
for j in jobs:
    j.join()
# Print completion message for multiprocessing
print ("List processing complete.")
# Record end time and calculate multiprocessing duration and print
end_time = time.time()

print("processes time=", end_time - start_time)



#This code demonstrates three ways of running the same task
# Serial execution runs the function one after another in a single process, which takes the longest time.
# Multithreading creates multiple threads within a single process to run the task “simultaneously,”
# Multiprocessing creates multiple processes, each with its own Python interpreter, achieving true parallel execution across CPU cores, significantly reducing runtime for CPU-intensive tasks.
# The time module measures how long each approach takes, while the out_list shows how results are stored. 
# This example illustrates the performance differences between serial, threads, and processes for heavy computation tasks.