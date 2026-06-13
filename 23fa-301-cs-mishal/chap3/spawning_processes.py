#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

# FUNCTION: myFunc
# Prints process number and then counts from 0 to i-1
def myFunc(i):
    print('calling myFunc from process n°: %s' % i)
    # Loop runs 'i' times (if i=3, prints 0,1,2)
    for j in range(0, i):
        print('output from myFunc is :%s' % j)
    return

if __name__ == '__main__':
    # Create and run 6 processes (i = 0,1,2,3,4,5)
    for i in range(6):
        # Create process with myFunc, passing current i as argument
        process = multiprocessing.Process(target=myFunc, args=(i,))
        
        # Start the process
        process.start()
        
        # KEY CONCEPT: join() inside loop = SEQUENTIAL execution
        # Main program WAITS here for process to finish before next iteration
        # Result: Processes run ONE AFTER ANOTHER (not parallel!)
        process.join()

# ============================================================================
# SUMMARY:
# ============================================================================
# WHAT IT DOES:
#   Creates 6 processes. Each prints its ID number and counts to (i-1)
#
# EXAMPLE OUTPUT (for i=3):
#   calling myFunc from process n°: 3
#   output from myFunc is :0
#   output from myFunc is :1
#   output from myFunc is :2
#
# SEQUENTIAL EXECUTION PATTERN:
#   Process 0 (i=0) → prints nothing (range 0 to -1) → finishes
#   Process 1 (i=1) → prints 0 → finishes  
#   Process 2 (i=2) → prints 0,1 → finishes
#   Process 3 (i=3) → prints 0,1,2 → finishes
#   Process 4 (i=4) → prints 0,1,2,3 → finishes
#   Process 5 (i=5) → prints 0,1,2,3,4 → finishes
#
# CRITICAL OBSERVATION:
#   join() inside loop = NO parallel execution!
#   Each process COMPLETES before next one STARTS
#   Total time = Sum of all 6 process times
#
# TO RUN IN PARALLEL (fix):
#   processes = []
#   for i in range(6):
#       p = multiprocessing.Process(target=myFunc, args=(i,))
#       p.start()
#       processes.append(p)
#   for p in processes:
#       p.join()  # Wait for ALL after starting all
# ============================================================================

# output

# calling myFunc from process n°: 0
# calling myFunc from process n°: 1
# output from myFunc is :0
# calling myFunc from process n°: 2
# output from myFunc is :0
# output from myFunc is :1
# calling myFunc from process n°: 3
# output from myFunc is :0
# output from myFunc is :1
# output from myFunc is :2
# calling myFunc from process n°: 4
# output from myFunc is :0
# output from myFunc is :1
# output from myFunc is :2
# output from myFunc is :3
# calling myFunc from process n°: 5
# output from myFunc is :0
# output from myFunc is :1
# output from myFunc is :2
# output from myFunc is :3
# output from myFunc is :4