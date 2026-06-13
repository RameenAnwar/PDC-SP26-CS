import multiprocessing
import time

# Function that prints numbers 0-4 for background process and 5-9 for the other
def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'background_process':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    # Daemon = True means this process will be killed when main program exits
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = True  # Won't finish if main program ends early

    # Daemon = False means program waits for this process to complete
    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = False  # Program will wait for this process
    
    background_process.start()  # Start daemon process
    NO_background_process.start()  # Start non-daemon process