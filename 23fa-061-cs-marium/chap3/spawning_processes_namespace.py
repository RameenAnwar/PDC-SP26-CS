import multiprocessing
from myFunc import myFunc  # Import the myFunc function from an external file

if __name__ == '__main__':
    # Create, start, and wait for 6 processes to run sequentially
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))  # Create process with argument i
        process.start()  # Start the process
        process.join()  # Wait for this process to finish before creating next one