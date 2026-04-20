# Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing  # For creating processes

# FUNCTION that will run in each process
def myFunc(i):
    # Print which process number is running
    print ('calling myFunc from process n°: %s' %i)
    
    # Loop from 0 to i-1
    for j in range (0,i):
        # Print current loop number
        print('output from myFunc is :%s' %j)
    return  # Function ends

# MAIN PROGRAM
if __name__ == '__main__':
    # Loop 6 times (i = 0, 1, 2, 3, 4, 5)
    for i in range(6):
        # Create a process that runs myFunc with value i
        process = multiprocessing.Process(target=myFunc, args=(i,))
        
        # Start the process
        process.start()
        
        # WAIT for this process to finish before starting next one
        process.join()