"""
Chapter 2 – Topic 1: What is a Thread?
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  A thread is an independent execution flow that can run in parallel and
  concurrently with other threads inside the same process.

COMPOSITION:
  Each thread consists of three elements:
    - Program counter
    - Registers
    - Stack

THREAD STATES:
  Ready   → thread is created and waiting to be scheduled
  Running → thread is currently executing
  Blocked → thread is waiting for a condition; returns to Ready once resolved

SHARED RESOURCES (within the same process):
  - Data (variables, memory)
  - OS resources (file handles, sockets, etc.)

ADVANTAGES over processes:
  - Lighter weight (cheaper to create and destroy)
  - Faster context switching
  - Shared memory makes inter-thread communication fast

RISKS:
  - Race conditions (unsynchronised access to shared data)
  - Deadlocks (threads waiting on each other indefinitely)

PYTHON MODULE:
  Python manages threads with the built-in `threading` module.
  Main components:
    threading.Thread      – create and manage threads
    threading.Lock        – mutual-exclusion lock
    threading.RLock       – reentrant lock
    threading.Semaphore   – counting semaphore
    threading.Condition   – condition variable (wait/notify)
    threading.Event       – simple boolean flag signalling
    threading.Barrier     – phase barrier for groups of threads
    queue.Queue           – thread-safe FIFO data structure
"""

import threading
import time


def show_thread_states():
    """
    Demonstrate the three thread states:
      Ready   – thread object created but not yet started
      Running – after start() is called
      Blocked – while sleeping / waiting (simulated with time.sleep)
    """

    results = []

    def worker(name, sleep_secs):
        # RUNNING state
        results.append(f"{name}: entered RUNNING state")
        # BLOCKED state (waiting for I/O, sleep, lock, etc.)
        time.sleep(sleep_secs)
        results.append(f"{name}: returned from BLOCKED state → RUNNING again")

    # READY state – thread object exists but is not yet scheduled
    t1 = threading.Thread(name="Thread-A", target=worker, args=("Thread-A", 1))
    t2 = threading.Thread(name="Thread-B", target=worker, args=("Thread-B", 2))

    print("Threads created → READY state")

    t1.start()   # → RUNNING
    t2.start()   # → RUNNING

    t1.join()
    t2.join()

    for msg in results:
        print(msg)


def show_thread_info():
    """Print basic information about the main thread and a spawned thread."""

    def worker():
        t = threading.current_thread()
        print(f"  Worker thread  | name: {t.name} | daemon: {t.daemon} | id: {t.ident}")

    main = threading.main_thread()
    print(f"  Main   thread  | name: {main.name} | daemon: {main.daemon} | id: {main.ident}")

    t = threading.Thread(name="MyWorker", target=worker)
    t.start()
    t.join()

    print(f"\n  Active thread count: {threading.active_count()}")
    print(f"  All threads: {[th.name for th in threading.enumerate()]}")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 1: What is a Thread?")
    print("=" * 55)

    print("\n--- Thread State Demo ---")
    show_thread_states()

    print("\n--- Thread Info Demo ---")
    show_thread_info()
