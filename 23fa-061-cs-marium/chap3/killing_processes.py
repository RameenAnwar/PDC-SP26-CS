import multiprocessing
import time

# Function that prints numbers 0-9 with 1 second delay
def foo():
    print ('Starting function')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)  # Create a new process for foo()
    print ('Process before execution:', p, p.is_alive())  # Should be False
    p.start()  # Start the process - foo() begins running
    print ('Process running:', p, p.is_alive())  # Should be True now
    p.terminate()  # Forcefully kill the process mid-execution
    print ('Process terminated:', p, p.is_alive())  # Process is dying
    p.join()  # Wait for process to fully clean up
    print ('Process joined:', p, p.is_alive())  # Should be False
    print ('Process exit code:', p.exitcode)  # Negative number means terminated