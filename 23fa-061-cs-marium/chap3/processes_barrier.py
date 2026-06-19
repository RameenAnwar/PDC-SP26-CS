import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

# Function that uses barrier to synchronize processes before printing timestamp
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait until all processes hit this barrier (2 processes needed)
    now = time()
    with serializer:  # Lock ensures only one process prints at a time
        print("process %s ----> %s" \
              %(name,datetime.fromtimestamp(now)))

# Function that prints timestamp immediately without any synchronization
def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" \
          %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)  # Barrier that needs 2 processes to release
    serializer = Lock()  # Lock to prevent print conflicts
    
    # Start two processes that will use the barrier (will print at same time)
    Process(name='p1 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='p2 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    
    # Start two processes that run without barrier (will print whenever they want)
    Process(name='p3 - test_without_barrier'\
            ,target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier'\
            ,target=test_without_barrier).start()