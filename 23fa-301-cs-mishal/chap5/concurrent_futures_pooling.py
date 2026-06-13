# Import the concurrent.futures module for thread/process pool executors
import concurrent.futures
# Import time for performance measurement
import time

# Create a list of numbers from 1 to 10
number_list = list(range(1, 11))

def count(number):
    """Simulate a heavy computation by looping 10 million times."""
    i = 0                     # initialise i to avoid "possibly unbound" warning
    for i in range(0, 10000000):
        i += 1                # increment i (the loop runs 10 million times)
    return i * number         # after the loop, i = 10,000,000; multiply by input

def evaluate(item):
    """Call count() and print the result for a given item."""
    result_item = count(item)          # compute heavy function
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    # ---------- Sequential Execution ----------
    start_time = time.perf_counter()         # start high‑resolution timer
    for item in number_list:                 # process each item one by one
        evaluate(item)                       # (blocks until each finishes)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # ---------- Thread Pool Execution ----------
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Create a pool of 5 worker threads
        for item in number_list:
            # Submit each evaluate() call to the pool – runs concurrently
            executor.submit(evaluate, item)
    # The 'with' block waits for all submitted tasks to finish
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # ---------- Process Pool Execution ----------
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        # Create a pool of 5 separate processes (bypasses GIL)
        for item in number_list:
            executor.submit(evaluate, item)
    # The 'with' block waits for all processes to complete
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    #ouptut
# Item 3, result 30000000
# Item 4, result 40000000
# Item 5, result 50000000
# Item 6, result 60000000
# Item 7, result 70000000
# Item 8, result 80000000
# Item 9, result 90000000
# Item 10, result 100000000
# Sequential Execution in 5.471477299928665 seconds
# Item 1, result 10000000
# Item 2, result 20000000
# Item 4, result 40000000
# Item 5, result 50000000
# Item 3, result 30000000
# Item 6, result 60000000
# Item 7, result 70000000
# Item 8, result 80000000
# Item 9, result 90000000
# Item 10, result 100000000
# Thread Pool Execution in 6.580071399919689 seconds
# Item 1, result 10000000
# Item 2, result 20000000
# Item 3, result 30000000
# Item 4, result 40000000
# Item 5, result 50000000
# Item 6, result 60000000
# Item 7, result 70000000
# Item 8, result 80000000
# Item 9, result 90000000
# Item 10, result 100000000