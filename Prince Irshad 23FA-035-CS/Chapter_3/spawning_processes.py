#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    # Print a message indicating which process is running
    print('calling myFunc from process n°: %s' %i)
    # Run a simple loop
    for j in range(0,i):
        print('output from myFunc is :%s' %j)
    return

if __name__ == '__main__':
    # Loop to spawn (create) 6 separate processes
    for i in range(6):
        # Create a new process and pass the current loop number 'i' as an argument
        process = multiprocessing.Process(target=myFunc, args=(i,))
        # Start the spawned process
        process.start()
        # Immediately wait for it to finish before starting the next one
        process.join()