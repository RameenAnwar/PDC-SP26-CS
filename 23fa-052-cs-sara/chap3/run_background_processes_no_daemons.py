import multiprocessing
from multiprocessing import Barrier, Lock, Process  # Tools for sync
from time import time  # To get time
from datetime import datetime  # To show time nicely

# FUNCTION WITH BARRIER (processes wait for each other)
def test_with_barrier(synchronizer, serializer):
    # Get the name of current process (like "p1 - test_with_barrier")
    name = multiprocessing.current_process().name
    
    # BARRIER: Stop here until other process also arrives
    # Both p1 and p2 will wait here for each other
    synchronizer.wait()  # Wait for friend process
    
    # Get current time after waiting (both processes get same time)
    now = time()
    
    # LOCK: Only one process can print at a time (no text mixing)
    with serializer:
        # Show process name and current timestamp
        print("process %s ----> %s" \
              %(name, datetime.fromtimestamp(now)))

# FUNCTION WITHOUT BARRIER (processes run freely)
def test_without_barrier():
    # Get the name of current process
    name = multiprocessing.current_process().name
    
    # Get time immediately - NO waiting for anyone
    now = time()
    
    # Print directly without lock (text might mix, but that's okay)
    print("process %s ----> %s" \
          %(name ,datetime.fromtimestamp(now)))

# MAIN PROGRAM - Execution starts here
if __name__ == '__main__':
    # Create a barrier that needs 2 processes to wait for each other
    # Both processes must reach .wait() before continuing
    synchronizer = Barrier(2)
    
    # Create a lock to prevent printing conflicts
    # Without this, outputs from two processes might mix together
    serializer = Lock()
    
    # Process 1: WITH barrier (will wait for process 2)
    Process(name='p1 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    
    # Process 2: WITH barrier (will wait for process 1)
    Process(name='p2 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    
    # Process 3: WITHOUT barrier (runs freely, no waiting)
    Process(name='p3 - test_without_barrier'\
            ,target=test_without_barrier).start()
    
    # Process 4: WITHOUT barrier (runs freely, no waiting)
    Process(name='p4 - test_without_barrier'\
            ,target=test_without_barrier).start()