import multiprocessing
import time

# Function that prints different loops based on process name
def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'background_process':
        for i in range(0,5):  # If background_process, print 0 to 4
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):  # If NO_background_process, print 5 to 9
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    # Create first process with name 'background_process' (daemon = False means it won't die when main dies)
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = False  # Program will wait for this process to finish

    # Create second process with name 'NO_background_process'
    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = False  # Program will also wait for this process
    
    background_process.start()  # Start the background process
    NO_background_process.start()  # Start the other process