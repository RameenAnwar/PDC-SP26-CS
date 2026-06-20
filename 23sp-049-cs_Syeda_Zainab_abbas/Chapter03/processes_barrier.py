# processes_barrier.py
# A BARRIER for PROCESSES. p1 and p2 wait at the barrier and are released together,
# so they print near-identical timestamps. p3 and p4 have no barrier, so they print
# as soon as they start. A Lock (serializer) keeps the prints from getting jumbled.

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()             # wait for the other barrier process
    now = time()
    with serializer:                # lock so only one process prints at a time
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)       # barrier for exactly 2 processes
    serializer = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
