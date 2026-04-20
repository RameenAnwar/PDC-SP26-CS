# Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing  # For creating process pool

# FUNCTION that squares a number
def function_square(data):
    result = data * data  # Multiply number by itself (square)
    return result         # Return the squared value

# MAIN PROGRAM
if __name__ == '__main__':
    # Create a list of numbers from 0 to 99
    inputs = list(range(0, 100))  # [0, 1, 2, 3, ..., 99]
    
    # Create a pool of 4 worker processes (4 parallel workers)
    pool = multiprocessing.Pool(processes=4)
    
    # Apply function_square to ALL inputs in parallel using the pool
    # pool.map() distributes work across 4 processes automatically
    pool_outputs = pool.map(function_square, inputs)
    
    # Clean up: No more tasks will be added
    pool.close()
    
    # Wait for all processes to finish their work
    pool.join()
    
    # Print all results (squares of 0 to 99)
    print ('Pool    :', pool_outputs)