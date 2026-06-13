import os  # For operating system related tasks (not used directly here)
import time  # To measure how long the program takes
import threading  # To use threads for multitasking
import multiprocessing  # To use multiple processes
import random  # To generate random numbers
 
NUM_WORKERS = 10  # Number of threads or processes to run
size = 10000000  # Number of random numbers to generate
out_list = list()  # List to store the results

def do_something(count, out_list):
    for i in range(count):  # Repeat count times
        out_list.append(random.random())  # Add a random number to the list

"""
#Serial
start_time = time.time()
for _ in range(NUM_WORKERS):
    do_something(size,out_list)
end_time = time.time()
print("Serial time=", end_time - start_time)
"""

#MultiThreading
start_time = time.time()  # Start time for threading
jobs = []
for i in range(0, NUM_WORKERS):
    thread = threading.Thread(target=do_something(size, out_list))  # Create a thread
    jobs.append(thread)  #