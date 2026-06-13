import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    # Get the process name
    name = multiprocessing.current_process().name
    # Wait here until exactly 2 processes reach this point (The Barrier)
    synchronizer.wait()
    # Note the current time after passing the barrier
    now = time()
    # Use Lock so processes don't print over each other at the same time
    with serializer:
        print("process %s ----> %s" \
              %(name,datetime.fromtimestamp(now)))

def test_without_barrier():
    # Get the process name
    name = multiprocessing.current_process().name
    # Note the current time immediately (no waiting)
    now = time()
    # Print the time directly without any locks
    print("process %s ----> %s" \
          %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    # Create a barrier that requires 2 processes to open
    synchronizer = Barrier(2)
    # Create a lock to keep console printing clean
    serializer = Lock()
    
    # Start two processes that use the barrier
    Process(name='p1 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='p2 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
            
    # Start two processes that run freely without the barrier
    Process(name='p3 - test_without_barrier'\
            ,target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier'\
            ,target=test_without_barrier).start()