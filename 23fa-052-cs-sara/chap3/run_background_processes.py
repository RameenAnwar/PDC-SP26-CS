import multiprocessing  # For creating processes
import time  # For adding delays

# FUNCTION that will run in both processes
def foo():
    # Get the name of current process
    name = multiprocessing.current_process().name
    
    print ("Starting %s \n" %name)  # Show process started
    
    # If process name is 'background_process'
    if name == 'background_process':
        # Loop from 0 to 4 (5 times)
        for i in range(0,5):
            print('---> %d \n' %i)  # Print numbers 0,1,2,3,4
        time.sleep(1)  # Wait 1 second
    
    # If process name is 'NO_background_process'
    else:
        # Loop from 5 to 9 (5 times)
        for i in range(5,10):
            print('---> %d \n' %i)  # Print numbers 5,6,7,8,9
        time.sleep(1)  # Wait 1 second
    
    print ("Exiting %s \n" %name)  # Show process finished

# MAIN PROGRAM
if __name__ == '__main__':
    # Create FIRST process (background/demon process)
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = True  # DAEMON = will die when main program ends
    
    # Create SECOND process (non-demon process)
    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = False  # NOT a daemon = will complete even if main ends
    
    # Start both processes
    background_process.start()  # Start daemon process
    NO_background_process.start()  # Start non-daemon process