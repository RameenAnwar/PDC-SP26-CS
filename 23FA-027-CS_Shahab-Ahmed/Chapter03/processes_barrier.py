import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

# Function where processes wait at a barrier
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    
    synchronizer.wait()  # All processes wait here until required count reached
    
    now = time()
    
    # Lock ensures only one process prints at a time
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


# Function without synchronization
def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    synchronizer = Barrier(2)  # Only 2 processes required to release barrier
    serializer = Lock()        # Prevent mixed output

    # Processes using barrier (will sync)
    Process(name='p1', target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    Process(name='p2', target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    # Processes without barrier (run independently)
    Process(name='p3', target=test_without_barrier).start()
    Process(name='p4', target=test_without_barrier).start()