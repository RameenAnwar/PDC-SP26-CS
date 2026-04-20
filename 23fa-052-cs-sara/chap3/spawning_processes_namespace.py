import multiprocessing  # For creating processes
from myFunc import myFunc  # Import myFunc function from another file (myFunc.py)

# MAIN PROGRAM
if __name__ == '__main__':
    # Loop 6 times (i = 0, 1, 2, 3, 4, 5)
    for i in range(6):
        # Create a new process that will run myFunc(i)
        # args=(i,) passes the current value of i to myFunc
        process = multiprocessing.Process(target=myFunc, args=(i,))
        
        # Start the process (begins executing myFunc with value i)
        process.start()
        
        # Wait for this process to COMPLETELY finish before starting next one
        process.join()