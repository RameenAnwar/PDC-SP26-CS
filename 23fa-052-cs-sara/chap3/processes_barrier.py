import multiprocessing
from multiprocessing import Barrier, Lock, Process  # Tools for sync
from time import time  # To get time
from datetime import datetime  # To show time nicely

# FUNCTION WITH BARRIER (processes wait for each other)
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name  # Get process name
    
    # BARRIER: Stop here until other process also arrives
    synchronizer.wait()  # Wait for friend process
    
    now = time()  # Get current time after waiting
    
    # LOCK: Only one process can print at a time
    with serializer:
        # Show process name and time
        print("process %s ----> %s" \
              %(name, datetime.fromtimestamp(now)))

# FUNCTION WITHOUT BARRIER (processes run freely)
def test_without_barrier():
    name = multiprocessing.current_process().name  # Get process name
    now = time()  # Get time immediately (no waiting)
    print("process %s ----> %s" \
          %(name ,datetime.fromtimestamp(now)))  # Print

# MAIN PROGRAM
if __name__ == '__main__':
    # Barrier needs 2 processes to wait for each other
    synchronizer = Barrier(2)
    
    # Lock stops printing problems (mixing of text)
    serializer = Lock()
    
    # Process 1: WITH barrier (will wait)
    Process(name='p1 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    
    # Process 2: WITH barrier (will wait)
    Process(name='p2 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    
    # Process 3: WITHOUT barrier (runs free)
    Process(name='p3 - test_without_barrier'\
            ,target=test_without_barrier).start()
    
    # Process 4: WITHOUT barrier (runs free)
    Process(name='p4 - test_without_barrier'\
            ,target=test_without_barrier).start()