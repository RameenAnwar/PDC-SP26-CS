# multithreadingtest.py

import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

# Create threads
t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))

start = time.time()

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

end = time.time()

print("Total Time:", end - start)