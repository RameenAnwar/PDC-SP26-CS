# Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

# Function that returns the square of a given number
def function_square(data):
    result = data*data
    return result


if __name__ == '__main__':
    inputs = list(range(0,100))  # Create list of numbers from 0 to 99
    pool = multiprocessing.Pool(processes=4)  # Create a pool with 4 worker processes
    pool_outputs = pool.map(function_square, inputs)  # Apply square function to all inputs in parallel

    pool.close()  # Stop accepting new tasks to the pool
    pool.join()   # Wait for all worker processes to finish
    print ('Pool    :', pool_outputs)  # Print the list of squared results