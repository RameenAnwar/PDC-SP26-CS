"""
Chapter 2 – Topic 5: Thread Synchronization with a Lock
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  A Lock (mutex) ensures only one thread at a time can execute a
  protected (critical) section of code.

HOW IT WORKS:
  - acquire() → thread gains the lock; others that call acquire() block.
  - release() → lock is freed; one blocked thread wakes up and acquires it.
  - If acquire(blocking=False) is used, it returns True/False immediately
    instead of blocking.

CAUTION:
  - A regular Lock is NON-REENTRANT: a thread that already holds the
    lock will deadlock if it tries to acquire it again.
  - Always pair every acquire() with a release(); use try/finally or
    the `with` statement to guarantee this even on exceptions.

PROS:
  - Simple and effective for protecting critical sections.
CONS:
  - Can cause deadlocks if misused.
  - Sequential execution inside the lock reduces parallelism.
"""

import threading
import time
import os
from threading import Thread
from random import randint


# One lock shared by all thread instances
threadLock = threading.Lock()


class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # --- acquire lock → enter critical section ---
        threadLock.acquire()
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> {self.name} over")
        # --- release lock → leave critical section ---
        threadLock.release()


def main():
    start_time = time.time()

    threads = [
        MyThreadClass(f"Thread#{i}", randint(1, 3))
        for i in range(1, 6)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("End")
    print(f"--- {time.time() - start_time:.2f} seconds ---")

    # ── Bonus: safer pattern using `with` (auto-releases on exception) ────────
    print("\n--- Using `with` statement (recommended) ---")
    counter = 0
    safe_lock = threading.Lock()

    def increment():
        nonlocal counter
        for _ in range(100_000):
            with safe_lock:       # acquires on entry, releases on exit
                counter += 1

    threads2 = [Thread(target=increment) for _ in range(4)]
    for t in threads2:
        t.start()
    for t in threads2:
        t.join()

    print(f"Final counter (expected 400000): {counter}")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 5: Thread Synchronization with a Lock")
    print("=" * 55)
    main()
