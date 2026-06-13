
# Purpose: A simple function that demonstrates process execution
# Parameter: i - a number that determines how many times the loop runs
# This function is designed to be run in separate processes
def myFunc(i):
    # Print which process number is calling this function
    # %s is a string format specifier - will be replaced by the value of i
    # This helps identify which process is executing (process 0, 1, 2, etc.)
    print('calling myFunc from process n°: %s' % i)
    
    # Loop from 0 to i-1 (if i=5, loops 0,1,2,3,4)
    # range(0, i) creates a sequence starting at 0, stopping before i
    for j in range(0, i):
        # Print the current loop counter value
        # Shows the work being done by this specific process
        # Each process will print its own sequence of numbers
        print('output from myFunc is :%s' % j)
    
    # Function ends here - no return value (implicitly returns None)
    # The 'return' statement is optional here since nothing is returned
    return

#What This Function Does:
# This function myFunc(i) is a worker function that:

# Announces itself - Prints which process number is executing

# Does counting work - Prints numbers from 0 up to (i-1)

# Returns nothing - Just performs side effects (printing)

