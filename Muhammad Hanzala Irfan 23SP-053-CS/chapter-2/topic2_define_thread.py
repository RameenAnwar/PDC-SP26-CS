"""
Chapter 2 – Topic 2: How to Define a Thread
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  The simplest way to use a thread is to instantiate threading.Thread
  with a target function and optional arguments, then call start().

THREAD CLASS SIGNATURE:
  threading.Thread(
      group=None,   # reserved for future use, always None
      target=None,  # callable to run in the thread
      name=None,    # thread name; defaults to "Thread-N"
      args=(),      # tuple of positional args passed to target
      kwargs={}     # dict of keyword args passed to target
  )

KEY METHODS:
  start()  – schedules the thread for execution (non-blocking)
  join()   – caller blocks until this thread finishes
  is_alive() – returns True if the thread is still running
"""

import threading


def my_func(thread_number):
    """Simple target function that prints which thread called it."""
    print(f"my_func called by thread N°{thread_number}")


def main():
    threads = []

    # Step 1 – create Thread objects with a target function and arguments
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)

    # Step 2 – start all threads (non-blocking; control returns immediately)
    for t in threads:
        t.start()

    # Step 3 – join: wait for every thread to finish before continuing
    for t in threads:
        t.join()

    print("All threads finished.")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 2: How to Define a Thread")
    print("=" * 55)
    main()
