# USING A PROCESS POOL - Chapter 3: Process Based Parallelism
# A Process Pool manages a fixed number of worker processes
# Tasks are distributed automatically among available workers

# Import multiprocessing module for process pool functionality
import multiprocessing

# FUNCTION: function_square
# Purpose: Simple mathematical function that squares a number
# This function will be executed in parallel across multiple processes
def function_square(data):
    # Calculate the square of the input number (data * data)
    result = data * data
    
    # Return the squared result back to the main process
    # The pool.map() method collects all return values
    return result

# MAIN EXECUTION BLOCK
# Required for multiprocessing to work correctly on all platforms (especially Windows)
if __name__ == '__main__':
    
    # Create a list of input numbers from 0 to 99
    # range(0, 100) generates numbers 0,1,2,...,99
    # list() converts the range object into an actual list
    inputs = list(range(0, 100))  # 100 numbers: 0 through 99
    
    # CREATE A PROCESS POOL
    # Pool(processes=4) creates a pool with 4 worker processes
    # These 4 processes will run in parallel (simultaneously)
    # The pool manages task distribution automatically
    pool = multiprocessing.Pool(processes=4)
    
    # MAP FUNCTION TO LIST - THE KEY LINE
    # pool.map() does THREE things:
    #   1. Distributes 'inputs' list across the 4 worker processes
    #   2. Applies 'function_square' to each input in parallel
    #   3. Collects results IN ORDER (same order as inputs)
    # 
    # HOW IT WORKS:
    #   - 100 numbers are split among 4 processes (25 numbers each)
    #   - Each process runs function_square on its chunk
    #   - Results are automatically gathered and returned as a list
    pool_outputs = pool.map(function_square, inputs)
    
    # CLOSE THE POOL
    # pool.close() prevents any more tasks from being submitted
    # Existing tasks will still complete
    # Without close(), join() would wait forever
    pool.close()
    
    # WAIT FOR ALL WORKERS TO FINISH
    # pool.join() blocks the main program until ALL pool processes complete
    # This ensures all 100 squaring operations are done before printing
    pool.join()
    
    # PRINT THE RESULTS
    # pool_outputs is a list containing squares of 0 through 99
    # Format: [0, 1, 4, 9, 16, ..., 9801]
    print('Pool    :', pool_outputs)


# SUMMARY
# What This Code Does:
# Creates a pool of 4 worker processes that simultaneously calculate squares of numbers 0-99 (100 numbers total), then collects and prints all results in order.

# Visual Breakdown:
# text
# INPUT: [0, 1, 2, 3, ..., 99] (100 numbers)
#               │
#     ┌─────────┼─────────┐
#     ↓         ↓         ↓         ↓
# Process 1  Process 2  Process 3  Process 4
# (Numbers 0-24) (25-49) (50-74) (75-99)
#     ↓         ↓         ↓         ↓
#    0²...24²  25²...49²  50²...74²  75²...99²
#     │         │         │         │
#     └─────────┼─────────┼─────────┘
#               ↓
# OUTPUT: [0, 1, 4, 9, 16, ..., 9801] (100 results IN ORDER)


# Key Concepts:
# Component	                   Purpose
# Pool(processes=4)	           Creates 4 worker processes (parallel workers)
# pool.map(function, list)	   Distributes work and collects results automatically
# pool.close()	               Stops accepting new tasks
# pool.join()	               Waits for all workers to finish



# output
# Pool    : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289,
#  324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 
# 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401,
#  2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096,
#  4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241,
#  6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836,
#  9025, 9216, 9409, 9604, 9801]

