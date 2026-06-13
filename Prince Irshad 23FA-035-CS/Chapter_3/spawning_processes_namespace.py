import multiprocessing
# Import the function from an external file (myFunc.py) to keep the main script clean
from myFunc import myFunc

if __name__ == '__main__':
    # Loop to spawn 6 processes
    for i in range(6):
        # Create a process targeting the imported function and pass 'i' as argument
        process = multiprocessing.Process(target=myFunc, args=(i,))
        # Start the process
        process.start()
        # Wait for the process to complete before the next iteration
        process.join()