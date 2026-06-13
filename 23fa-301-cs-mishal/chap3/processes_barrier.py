# IMPORT STATEMENTS
# Import multiprocessing for process creation and management
import multiprocessing
# Import Barrier (synchronization primitive) and Lock from multiprocessing
# Barrier: Makes processes wait until a certain number have reached a point
# Lock: Mutual exclusion - only one process can execute a code section at a time
from multiprocessing import Barrier, Lock, Process
# Import time() function to get current timestamp in seconds since epoch (Jan 1, 1970)
from time import time
# Import datetime to convert timestamps to human-readable format
from datetime import datetime


# FUNCTION 1: test_with_barrier
# Purpose: Demonstrates process synchronization using Barrier and Lock
# Barrier makes processes wait for each other, Lock prevents print interference
def test_with_barrier(synchronizer, serializer):
    # Get the name of the current process (e.g., 'p1 - test_with_barrier')
    # This helps identify which process is printing
    name = multiprocessing.current_process().name
    
    # BARRIER WAIT POINT - KEY SYNCHRONIZATION
    # synchronizer.wait() blocks until 2 processes have called wait()
    # Since Barrier(2) was created, both p1 and p2 will wait here
    # The first process that arrives waits for the second to arrive
    # Only when BOTH have called wait(), they continue execution together
    synchronizer.wait()
    
    # Get current timestamp AFTER passing the barrier
    # Since both processes pass the barrier at nearly the same time,
    # their timestamps will be very close (microseconds apart)
    now = time()
    
    # LOCK - ensures only ONE process prints at a time
    # 'with serializer:' acquires the lock automatically
    # Prevents output from being mixed/corrupted between processes
    # Without this, two processes might print simultaneously causing garbled output
    with serializer:
        # Print process name and the current time
        # datetime.fromtimestamp(now) converts seconds to readable format
        # Example: "process p1 - test_with_barrier ----> 2024-01-15 10:30:47.789012"
        print("process %s ----> %s" \
              % (name, datetime.fromtimestamp(now)))

# FUNCTION 2: test_without_barrier
# Purpose: Demonstrates processes running WITHOUT any synchronization
# Processes start and print immediately - no waiting, no coordination
def test_without_barrier():
    # Get the name of the current process
    name = multiprocessing.current_process().name
    
    # Get current timestamp IMMEDIATELY (no waiting for other processes)
    now = time()
    
    # Print directly without any lock
    # Output may be mixed if both processes print simultaneously
    # No guarantee about order or timing
    print("process %s ----> %s" \
          % (name, datetime.fromtimestamp(now)))

# MAIN EXECUTION BLOCK
# Required for multiprocessing to work correctly on all platforms (especially Windows)
if __name__ == '__main__':
    
    # CREATE A BARRIER that waits for exactly 2 processes
    # Both processes must call wait() before any can continue
    # If only 1 process calls wait(), it will wait forever (deadlock)
    # If 3 processes call wait(), 2 will proceed and 1 will wait (barrier resets)
    synchronizer = Barrier(2)
    
    # CREATE A LOCK for mutual exclusion (binary semaphore)
    # Ensures only one process prints at a time
    # Prevents garbled output when multiple processes try to print simultaneously
    serializer = Lock()
    
    # CREATE AND START PROCESS 1 (with barrier)
    # Name: 'p1 - test_with_barrier' - custom name for identification
    # Target: test_with_barrier function to execute
    # Args: passes synchronizer (Barrier) and serializer (Lock) as arguments
    # .start() begins process execution
    Process(name='p1 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    
    # CREATE AND START PROCESS 2 (with barrier)
    # Same function, same arguments as p1
    # This process will synchronize with p1 at the barrier
    # Both will wait for each other before continuing
    Process(name='p2 - test_with_barrier',
            target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    
    # CREATE AND START PROCESS 3 (without barrier)
    # Runs test_without_barrier function - no synchronization
    # Starts immediately and prints immediately
    # No waiting, no locks
    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()
    
    # CREATE AND START PROCESS 4 (without barrier)
    # Also runs test_without_barrier
    # Completely independent from p3
    # May print before, after, or interleaved with p3
    # Order depends on OS process scheduling
    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
    

#     SUMMARY OF THE CODE
# What This Code Does:
# This program demonstrates the difference between synchronized and unsynchronized processes using a Barrier
# (forces processes to wait for each other) and compares it with unsynchronized execution.
# Barrier makes p1 and p2 wait for each other then print at almost the same time, while p3 and p4 run freely 
# without synchronization, showing the difference between coordinated and uncoordinated processes.

# Two Types of Processes:
# Process	Function	Synchronization	Behavior
# p1 & p2	test_with_barrier	Barrier(2) + Lock	Both wait for each other, then print at nearly same time
# p3 & p4	test_without_barrier	None	Start and print immediately, no coordination
# Visual Timeline:
# text
# Time ──────────────────────────────────────────────────────────────────→

# WITH BARRIER (p1 and p2):
# p1: [------waiting for p2------] → [get time] → [print] 
#                                 ↓
# p2: [------waiting for p1------] → [get time] → [print]

# (p1 and p2 print with almost identical timestamps - microseconds apart)

# WITHOUT BARRIER (p3 and p4):
# p3: [get time] → [print] ───────────────────────┐
#                                                 ↓ (timestamps random)
# p4: [get time] → [print] ───────────────────────┘

# (Order of p3 and p4 is unpredictable - could be p3 first, p4 first, or interleaved)



# Key Concepts Explained:
# Concept	Purpose	In This Code
# Barrier(2)	Makes 2 processes wait for each other	p1 and p2 both hit .wait() before continuing
# Lock()	Mutual exclusion - only one process at a time	Prevents p1 and p2 from printing simultaneously (output corruption)
# No sync	Processes run completely independently	p3 and p4 start/print whenever OS schedules them

#output

# process p2 - test_with_barrier ----> 2026-04-18 14:59:48.452368
# process p1 - test_with_barrier ----> 2026-04-18 14:59:48.452368
# process p3 - test_without_barrier ----> 2026-04-18 14:59:48.468747
# process p4 - test_without_barrier ----> 2026-04-18 14:59:48.495894


