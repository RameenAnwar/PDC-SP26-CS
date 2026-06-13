import multiprocessing
import time

def foo():
    # Get the name of the process
    name = multiprocessing.current_process().name
    print("Starting %s \n" %name)
    # If this is the background_process, print 0 to 4
    if name == 'background_process':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    # If this is the normal process, print 5 to 9
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print("Exiting %s \n" %name)
    
if __name__ == '__main__':
    # Create the first process
    background_process = multiprocessing.Process\
         (name='background_process',\
          target=foo)
    # CHANGE HERE: Set to False. Now it is a normal process, NOT a daemon.
    background_process.daemon = False

    # Create the second process
    NO_background_process = multiprocessing.Process\
            (name='NO_background_process',\
             target=foo)
    
    # Keep it as a normal non-daemon process
    NO_background_process.daemon = False
    
    # Start both processes. Since none are daemons, the system will wait for them to finish.
    background_process.start()
    NO_background_process.start()