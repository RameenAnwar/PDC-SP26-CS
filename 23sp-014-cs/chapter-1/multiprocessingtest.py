# multiprocessingtest.py

import multiprocessing
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=task, args=("Process 1",))
    p2 = multiprocessing.Process(target=task, args=("Process 2",))

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("Total Time:", end - start)