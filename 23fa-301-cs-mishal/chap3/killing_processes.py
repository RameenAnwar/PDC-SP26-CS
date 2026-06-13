# IMPORT STATEMENTS COMMENT
# Import multiprocessing to create and manage separate processes
# Provides Process class for process creation and control methods (start, terminate, join)
import multiprocessing

# Import time module to add delays/sleep intervals
# Used to simulate work and demonstrate process timing
import time

# FUNCTION: foo
# Purpose: A simple function that runs in a separate process
# Prints numbers 0-9 with 1-second delays between each
def foo():
    # Print message indicating function has started
    print('Starting function')
    
    # Loop 10 times (i = 0, 1, 2, ..., 9)
    for i in range(0, 10):
        # Print current number with arrow and newline
        # -->0, -->1, -->2, etc.
        print('-->%d\n' % i)
        
        # Pause execution for 1 second
        # This makes the function run for about 10 seconds total
        # Allows us to see process state changes in real-time
        time.sleep(1)
    
    # Print message when function completes
    # This line may NEVER execute if process is terminated early!
    print('Finished function')

# MAIN EXECUTION BLOCK
# This code only runs when script is executed directly (not imported)
if __name__ == '__main__':
    
    # Create a Process object that will run the foo() function
    # target=foo means this process will execute foo() when started
    # At this point, process is NOT running - just an object in memory
    p = multiprocessing.Process(target=foo)
    
    # Print process state BEFORE starting
    # p.is_alive() returns False because process hasn't started yet
    # Shows: Process object exists but no system process created
    print('Process before execution:', p, p.is_alive())
    
    # Start the process
    # This creates a NEW system process and begins executing foo()
    # The main program continues running simultaneously (doesn't wait)
    p.start()
    
    # Print process state AFTER starting but BEFORE termination
    # p.is_alive() should return True (process is running)
    # The foo() function is now printing numbers in the background
    print('Process running:', p, p.is_alive())
    
    # TERMINATE the process immediately
    # Sends SIGTERM signal on Unix or TerminateProcess on Windows
    # This forcefully stops the process WITHOUT cleaning up
    # The foo() function stops immediately - may not complete its loop
    p.terminate()
    
    # Print process state AFTER termination
    # p.is_alive() might still show True briefly (process is terminating)
    # The OS needs a moment to actually kill the process
    print('Process terminated:', p, p.is_alive())
    
    # Wait for the terminated process to completely finish
    # join() blocks until the process actually exits
    # This is important to clean up resources and get exit code
    # Without join(), process might become a zombie process
    p.join()
    
    # Print process state AFTER joining
    # p.is_alive() should now definitely return False
    # Process has been completely cleaned up by the OS
    print('Process joined:', p, p.is_alive())
    
    # Print the process's exit code
    # exitcode meanings:
    #   0 = normal completion (process finished on its own)
    #   1 = error exit
    #   Negative number = terminated by signal (-15 SIGTERM for terminate())
    #   None = process hasn't exited yet
    print('Process exit code:', p.exitcode)



# summary:
# This program demonstrates process lifecycle management - creating, starting, forcibly terminating, and cleaning up a process.
# Process Lifecycle Demonstrated:

# Step 1: Create Process Object     → Process NOT running (is_alive = False)
# Step 2: p.start()                 → Process RUNNING (is_alive = True)
#                                   → foo() starts printing numbers
# Step 3: p.terminate()             → Process KILLED immediately
#                                   → foo() stops mid-execution
# Step 4: p.join()                  → Wait for cleanup
# Step 5: Check exit code           → Shows negative number (killed by signal)


#output
# Process before execution: <Process name='Process-1' parent=4768 initial> False
# Process running: <Process name='Process-1' pid=10528 parent=4768 started> True
# Process terminated: <Process name='Process-1' pid=10528 parent=4768 started> True
# Process joined: <Process name='Process-1' pid=10528 parent=4768 stopped exitcode=-SIGTERM> False
# Process exit code: -15