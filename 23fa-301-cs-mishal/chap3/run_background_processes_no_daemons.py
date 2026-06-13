# IMPORT STATEMENTS
# Import multiprocessing for creating and managing processes
import multiprocessing
# Import time module for sleep functionality (adds delays between prints)
import time

# FUNCTION: foo
# Purpose: Demonstrates process behavior by printing different number ranges
# based on the process name
def foo():
    # Get the name of the current process (set when creating the Process object)
    # This determines which code block will execute
    name = multiprocessing.current_process().name
    
    # Print starting message with process name
    # \n adds a newline for better formatting
    print("Starting %s \n" % name)
    
    # Check if this process is the background_process
    if name == 'background_process':
        # If yes, print numbers 0 through 4
        # Range 0-4 gives 5 numbers (0,1,2,3,4)
        for i in range(0, 5):
            print('---> %d \n' % i)
        # Sleep for 1 second after printing all numbers
        time.sleep(1)
    else:
        # If NOT background_process (must be NO_background_process)
        # Print numbers 5 through 9
        # Range 5-9 gives 5 numbers (5,6,7,8,9)
        for i in range(5, 10):
            print('---> %d \n' % i)
        # Sleep for 1 second after printing all numbers
        time.sleep(1)
    
    # Print exiting message with process name
    print("Exiting %s \n" % name)

# MAIN EXECUTION BLOCK
# Required for multiprocessing to work correctly
if __name__ == '__main__':
    
    # CREATE FIRST PROCESS (background_process)
    # Name: 'background_process' - custom name for identification
    # Target: foo function - this function will execute in the new process
    # Note: The backslash (\) allows line continuation for readability
    background_process = multiprocessing.Process(
                         name='background_process',
                         target=foo)
    
    # Set daemon flag to False (explicitly, though False is default)
    # Daemon = False means this process will continue running even if
    # the main program finishes (main will wait for it)
    # If daemon = True, process would be killed when main exits
    background_process.daemon = False

    # CREATE SECOND PROCESS (NO_background_process)
    # Name: 'NO_background_process' - different name to trigger else block
    # Target: same foo function - will execute the else branch
    NO_background_process = multiprocessing.Process(
                            name='NO_background_process',
                            target=foo)
    
    # Set daemon flag to False explicitly
    # Both processes are non-daemon, so main will wait for both
    NO_background_process.daemon = False
    
    # START FIRST PROCESS
    # This creates a new system process and begins executing foo()
    # background_process will print numbers 0-4
    background_process.start()
    
    # START SECOND PROCESS
    # This creates another new system process executing foo()
    # NO_background_process will print numbers 5-9
    NO_background_process.start()
    
    # NOTE: No join() calls here!
    # The main program will exit immediately after starting both processes
    # But since daemon = False, processes will continue running
    # However, on some systems, main exiting might still terminate children




#     SUMMARY OF THE CODE
# What This Code Does:
# This program creates two separate processes that run the same function foo() but execute different code blocks based on their process name. One process prints numbers 0-4, the other prints numbers 5-9.

# Process Comparison:
# Process	Name	Numbers Printed	Behavior
# background_process	'background_process'	0, 1, 2, 3, 4	Prints first half (0-4)
# NO_background_process	'NO_background_process'	5, 6, 7, 8, 9	Prints second half (5-9)
# Visual Timeline:
# text
# Time ──────────────────────────────────────────────────────────────────→

# background_process:
# [Start] → print 0 → print 1 → print 2 → print 3 → print 4 → sleep 1s → [Exit]

# NO_background_process:
# [Start] → print 5 → print 6 → print 7 → print 8 → print 9 → sleep 1s → [Exit]

# (Both processes run in PARALLEL - numbers may interleave!)

# Key Concepts:
# Concept	                Value	       Meaning
# daemon = False	    Both processes  	Main program will wait for them (though no join() here)
# No join()       	     Missing            Main might exit early, possibly killing processes
# Same function	          foo()	             Different behavior based on process name
# Parallel execution	   Yes	                 Both processes run simultaneously

#output

# Starting background_process 

# ---> 0

# ---> 1

# ---> 2

# ---> 3

# ---> 4

# Starting NO_background_process 

# ---> 5

# ---> 6

# ---> 7

# ---> 8

# ---> 9

# Exiting background_process 

# Exiting NO_background_process 