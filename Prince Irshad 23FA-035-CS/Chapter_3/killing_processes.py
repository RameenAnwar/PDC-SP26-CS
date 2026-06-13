import multiprocessing
import time

def foo():
    print('Starting function')
    # Loop that prints numbers from 0 to 9 with a 1-second delay
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print('Finished function')

if __name__ == '__main__':
    # Create a process that will run the foo() function
    p = multiprocessing.Process(target=foo)
    # Check if the process is alive before starting (Will be False)
    print('Process before execution:', p, p.is_alive())
    # Start the process
    p.start()
    # Check if the process is running now (Will be True)
    print('Process running:', p, p.is_alive())
    # Forcefully kill/stop the process before it finishes its work
    p.terminate()
    # Check again (Might still be True for a split second before OS cleans it)
    print('Process terminated:', p, p.is_alive())
    # Clean up the killed process from memory
    p.join()
    # Check if it is alive after joining (Will be False)
    print('Process joined:', p, p.is_alive())
    # Print the exit code. Negative number means it was killed forcefully
    print('Process exit code:', p.exitcode)