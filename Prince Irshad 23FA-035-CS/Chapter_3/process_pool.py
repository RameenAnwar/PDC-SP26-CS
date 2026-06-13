#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

# A simple function to calculate the square of a number
def function_square(data):
    result = data*data
    return result

if __name__ == '__main__':
    # Create a list of 100 numbers (from 0 to 99)
    inputs = list(range(0,100))
    # Create a Pool of 4 worker processes to share the workload
    pool = multiprocessing.Pool(processes=4)
    # Apply the function to all items in the list automatically using the 4 workers
    pool_outputs = pool.map(function_square, inputs)

    # Tell the pool that no more tasks will be added
    pool.close() 
    # Wait for all workers to finish their jobs
    pool.join()  
    # Print the final list of results
    print('Pool    :', pool_outputs)