import concurrent.futures # Library to easily run tasks at the same time using threads or processes.
import time # Library to track how long the code takes to run.

# Create a list of numbers from 1 to 10.
number_list = list(range(1, 11))


# A function that simulates a very heavy and slow computer task.
def count(number):
    # Loop 10 million times just to make the CPU work hard and take up time.
    for i in range(0, 10_000_000):
        i += 1
        
    # Return the final loop number multiplied by our input number.
    return i * number


# A simple function to run the math task and print the result to the screen.
def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))


# Check if the script is being run directly.
if __name__ == '__main__':

    # --- 1. Sequential Execution (One by one) ---
    # Start the stopwatch.
    start_time = time.perf_counter()

    # Run the evaluate function for each number, waiting for one to finish before starting the next.
    for item in number_list:
        evaluate(item)

    # Stop the stopwatch and print how long the normal sequential method took.
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))


    # --- 2. Thread Pool Execution (Multiple threads) ---
    # Start the stopwatch again.
    start_time = time.perf_counter()

    # Create a team of 5 "threads" (workers sharing the same CPU core).
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Give each worker a number from our list to evaluate in the background.
        futures = [executor.submit(evaluate, item) for item in number_list]
        
        # Wait here until all the thread workers finish their jobs.
        concurrent.futures.wait(futures)

    # Stop the stopwatch and print how long the threading method took.
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))


    # --- 3. Process Pool Execution (Multiple CPU cores) ---
    # Start the stopwatch one last time.
    start_time = time.perf_counter()

    # Create a team of 5 "processes" (completely separate workers running on different CPU cores).
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        # Give each process a number from our list to evaluate in parallel.
        futures = [executor.submit(evaluate, item) for item in number_list]
        
        # Wait here until all the process workers finish their jobs.
        concurrent.futures.wait(futures)

    # Stop the stopwatch and print how long the multi-processing method took.
    # (Because this splits the heavy math across different CPU cores, this is usually the fastest).
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))