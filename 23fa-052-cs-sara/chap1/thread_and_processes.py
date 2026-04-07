import os                 # system module
import time               # time measurement
import threading          # threading support
import multiprocessing    # multiprocessing support
import random             # random number generator

NUM_WORKERS = 10          # number of workers
size = 10000000           # number of iterations
out_list = list()         # list to store results

# function to generate random numbers
def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())


"""
# SERIAL EXECUTION
start_time = time.time()

for _ in range(NUM_WORKERS):
    do_something(size, out_list)

end_time = time.time()

print("Serial time=", end_time - start_time)
"""


# MULTITHREADING
start_time = time.time()
jobs = []

for i in range(NUM_WORKERS):

    # create thread for function
    thread = threading.Thread(target=do_something(size, out_list))

    jobs.append(thread)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

print("Threading done")

end_time = time.time()
print("threading time=", end_time - start_time)


# MULTIPROCESSING
start_time = time.time()
jobs = []

for i in range(NUM_WORKERS):

    # create process for function
    process = multiprocessing.Process(
        target=do_something,
        args=(size, out_list)
    )

    jobs.append(process)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

print("Processing done")

end_time = time.time()
print("processes time=", end_time - start_time)