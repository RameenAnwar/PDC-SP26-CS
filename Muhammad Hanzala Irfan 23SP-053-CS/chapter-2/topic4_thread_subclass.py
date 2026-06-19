"""
Chapter 2 – Topic 4: How to Use a Thread in a Subclass
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  When thread behaviour is complex, subclass threading.Thread and
  override run(). The subclass can store its own state in __init__
  and the thread logic lives neatly inside run().

RULES:
  1. Call Thread.__init__(self) inside your __init__.
  2. Override run() – this is what executes when start() is called.
  3. Never call run() directly; always use start() so the thread
     is created by the OS and run() executes in that new thread.

PROS vs functional approach:
  - Encapsulates state (name, duration, results, …) inside the object.
  - Easier to extend or reuse thread behaviour via further subclassing.

CONS:
  - Slightly more verbose than passing a plain function to Thread().
"""

import time
import os
from random import randint
from threading import Thread


class MyThreadClass(Thread):
    """A custom thread that prints start/end messages and sleeps for 'duration'."""

    def __init__(self, name, duration):
        Thread.__init__(self)        # must call parent __init__
        self.name = name
        self.duration = duration

    def run(self):
        """Override run(): executed inside the new OS thread."""
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> {self.name} over")


def main():
    start_time = time.time()

    # Create nine thread instances
    threads = [
        MyThreadClass(f"Thread#{i}", randint(1, 5))
        for i in range(1, 10)
    ]

    # Start all threads (non-blocking)
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("End")
    print(f"--- {time.time() - start_time:.2f} seconds ---")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 4: How to Use a Thread in a Subclass")
    print("=" * 55)
    main()
