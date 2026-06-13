import multiprocessing
from myFunc import myFunc  # Importing custom function from external file

# KEY CONCEPT: Sequential process execution (NOT parallel)
# Each process must finish before the next one starts due to join() inside loop

if __name__ == '__main__':
    # Loop 6 times - creates 6 processes (i = 0,1,2,3,4,5)
    for i in range(6):
        # Create process with myFunc, passing current i as argument
        process = multiprocessing.Process(target=myFunc, args=(i,))
        
        # Start the process
        process.start()
        
        # KEY CONCEPT: join() called IMMEDIATELY after start
        # This BLOCKS the loop until current process finishes
        # Result: SEQUENTIAL execution, one process at a time
        process.join()

# ============================================================================
# SUMMARY:
# ============================================================================
# WHAT IT DOES:
#   Creates 6 processes that run ONE AFTER ANOTHER (sequentially)
#   
# WHY IT'S SEQUENTIAL (NOT PARALLEL):
#   join() is called inside the loop right after start()
#   Main program waits for process to finish before next iteration
#
# EXECUTION PATTERN:
#   Process 0 starts → waits for completion → Process 1 starts → waits → etc.
#
# TOTAL TIME = Sum of all 6 process execution times (not parallel!)
#
# TO MAKE IT PARALLEL (FIX):
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