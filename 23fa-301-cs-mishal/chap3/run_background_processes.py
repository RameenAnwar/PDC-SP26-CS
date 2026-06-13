import multiprocessing
import time

# KEY CONCEPT: Function behavior changes based on process name
def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    
    # KEY CONCEPT: Process name determines which numbers to print
    if name == 'background_process':  # Daemon process path
        for i in range(0,5):  # Prints 0,1,2,3,4
            print('---> %d \n' %i)
        time.sleep(1)
    else:  # Non-daemon process path (NO_background_process)
        for i in range(5,10):  # Prints 5,6,7,8,9
            print('---> %d \n' %i)
        time.sleep(1)
    
    print("Exiting %s \n" %name)  # Daemon may never reach this line

if __name__ == '__main__':
    # KEY CONCEPT 1: DAEMON PROCESS (daemon = True)
    # - Runs in background, killed immediately when main exits
    # - No cleanup, may not complete execution
    background_process = multiprocessing.Process(
                         name='background_process',
                         target=foo)
    background_process.daemon = True  # <-- Auto-kill on main exit

    # KEY CONCEPT 2: NON-DAEMON PROCESS (daemon = False)
    # - Normal process, continues even if main exits
    # - Will complete all work
    NO_background_process = multiprocessing.Process(
                            name='NO_background_process',
                            target=foo)
    NO_background_process.daemon = False  # Default behavior

    # Both processes start simultaneously (parallel execution)
    background_process.start()
    NO_background_process.start()
    
    # KEY CONCEPT 3: NO join() calls
    # - Main program exits immediately after starting processes
    # - Daemon process gets KILLED immediately
    # - Non-daemon becomes orphaned but continues running

# ============================================================================
# SUMMARY:
# ============================================================================
# - Daemon (True):  Prints 0-4 → KILLED before finishing (no "Exiting" message)
# - Non-daemon (False): Prints 5-9 → COMPLETES fully ("Exiting" message prints)
# - Missing join() causes main to exit early, killing daemon process
# ============================================================================

# output
# Starting NO_background_process 

# ---> 5

# ---> 6

# ---> 7

# ---> 8

# ---> 9

# Exiting NO_background_process 
