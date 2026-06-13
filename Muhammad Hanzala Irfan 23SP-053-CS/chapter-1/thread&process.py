# threadandprocesses.py

import time
import threading
import multiprocessing

def task():
    time.sleep(2)

# Serial Execution
start = time.time()

task()
task()

end = time.time()

print("Serial Time:", end - start)

# Multithreading
start = time.time()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Threading Time:", end - start)

# Multiprocessing
if __name__ == "__main__":

    start = time.time()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("Multiprocessing Time:", end - start)