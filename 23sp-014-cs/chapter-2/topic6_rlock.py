"""
Chapter 2 – Topic 6: Thread Synchronization with an RLock
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  An RLock (Reentrant Lock) is a synchronisation primitive that the
  SAME thread can acquire multiple times without deadlocking itself.

HOW IT WORKS:
  - The RLock tracks which thread owns it and how many times it has
    been acquired (acquisition count).
  - The owning thread can call acquire() again freely → count increases.
  - Each acquire() must be matched by a release() → count decreases.
  - Only when the count reaches 0 is the lock truly freed for other threads.

DIFFERENCES from Lock:
  Lock                              RLock
  ──────────────────────────────    ──────────────────────────────────
  Acquired at most once             Can be acquired N times (same thread)
  Any thread can release it         Only the owning thread can release it
  Less overhead                     Slight extra overhead (owner tracking)

USE CASE:
  Recursive functions or nested method calls that all need the same lock.
  Example below: Box.add() calls Box.execute(), both protected by the same RLock.
"""

import threading
import time
import random
from threading import Thread


class Box:
    """
    A shared box that tracks total items.
    add() and remove() both call execute(), which also acquires the
    same RLock → only possible with RLock, not a plain Lock.
    """

    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:                    # 2nd acquire by same thread – OK!
            self.total_items += value

    def add(self):
        with self.lock:                    # 1st acquire
            self.execute(1)

    def remove(self):
        with self.lock:                    # 1st acquire
            self.execute(-1)


def adder(box, items):
    print(f"N° {items} items to ADD")
    while items:
        box.add()
        time.sleep(0.5)
        items -= 1
        print(f"ADDED one item --> {items} items left to ADD")


def remover(box, items):
    print(f"N° {items} items to REMOVE")
    while items:
        box.remove()
        time.sleep(0.5)
        items -= 1
        print(f"REMOVED one item --> {items} items left to REMOVE")


def main():
    box = Box()
    t1 = Thread(target=adder,   args=(box, random.randint(8, 12)))
    t2 = Thread(target=remover, args=(box, random.randint(3, 6)))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"\nFinal total_items in box: {box.total_items}")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 6: Thread Synchronization with an RLock")
    print("=" * 55)
    main()
