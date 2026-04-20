import multiprocessing  # For creating and managing processes
import time             # For adding delays

# FUNCTION that will run in a separate process
def foo():
    print ('Starting function')
    for i in range(0,10):  # Loop 10 times (0 to 9)
        print('-->%d\n' %i)  # Print current number
        time.sleep(1)         # Wait 1 second between prints
    print ('Finished function')

# MAIN PROGRAM
if __name__ == '__main__':
    # Create a process that will run the foo() function
    p = multiprocessing.Process(target=foo)
    
    # Check process status BEFORE starting
    print ('Process before execution:', p, p.is_alive())
    # is_alive() returns False because process hasn't started yet
    
    # START the process
    p.start()
    print ('Process running:', p, p.is_alive())
    # is_alive() returns True because process is now running
    
    # TERMINATE (kill) the process immediately
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    # is_alive() returns False because process was killed
    
    # WAIT for process to fully finish (cleanup)
    p.join()
    print ('Process joined:', p, p.is_alive())
    # is_alive() still returns False
    
    # CHECK the exit code (shows how process ended)
    print ('Process exit code:', p.exitcode)