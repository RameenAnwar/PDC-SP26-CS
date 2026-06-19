# Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

# Function that prints process number and loops from 0 to i-1
def myFunc(i):
    print ('calling myFunc from process n°: %s' %i)
    for j in range (0,i):
        print('output from myFunc is :%s' %j)
    return

if __name__ == '__main__':
    # Create 6 processes, each running myFunc() with different argument (0 to 5)
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))  # Create process with i as argument
        process.start()  # Start the process
        process.join()   # Wait for process to finish before next one starts (sequential execution)