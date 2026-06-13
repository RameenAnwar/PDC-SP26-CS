"""
Chapter 2 – Topic 9: Thread Synchronization with an Event
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  An Event is the simplest signalling mechanism between threads.
  It manages a single internal boolean flag.

KEY METHODS:
  event.set()     → sets flag to True  (signals all waiting threads)
  event.clear()   → resets flag to False
  event.wait()    → blocks the calling thread until flag is True
  event.is_set()  → returns the current flag state (True/False)

HOW IT DIFFERS FROM Condition:
  - Event carries only a binary state (True / False).
  - No lock management needed by the caller.
  - All threads waiting on wait() are released when set() is called.
  - Use Condition when you need to pass richer state or wake selectively.

USE CASE – Producer / Consumer:
  1. Producer creates an item, appends it, calls set() → consumer wakes.
  2. Producer immediately calls clear() to reset the flag.
  3. Consumer's wait() unblocks, pops the item, loops back to wait().
"""

import logging
import threading
import time
import random

LOG_FORMAT = "%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Producer(threading.Thread):
    """Creates items, appends them to the list, and signals the consumer."""

    def run(self):
        for _ in range(5):
            time.sleep(1)
            item = random.randint(0, 100)
            items.append(item)
            logging.info(f"Producer notify: item {item} appended by {self.name}")
            event.set()      # signal: new item is available
            event.clear()    # immediately reset so each set() is a fresh signal


class Consumer(threading.Thread):
    """Waits for the event signal, then pops and processes an item."""

    def run(self):
        for _ in range(5):
            time.sleep(1.5)
            event.wait()     # block until producer calls set()
            if items:
                item = items.pop()
                logging.info(f"Consumer notify: {item} popped by {self.name}")


def main():
    producer = Producer(name="Producer")
    consumer = Consumer(name="Consumer")

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Done.")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 9: Thread Synchronization with an Event")
    print("=" * 55)
    main()
