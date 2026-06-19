"""
Chapter 2 – Topic 8: Thread Synchronization with a Condition
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  A Condition combines a Lock with wait/notify so threads can coordinate
  based on the STATE of shared data, not just mutual exclusion.

HOW IT WORKS:
  condition.acquire()  – acquires the underlying lock.
  condition.wait()     – releases the lock and blocks until notified;
                         re-acquires the lock before returning.
  condition.notify()   – wakes ONE waiting thread (lock must be held).
  condition.notify_all() – wakes ALL waiting threads.
  condition.release()  – releases the underlying lock.

  The `with condition:` context manager handles acquire/release automatically.

INTERNAL DETAIL:
  If no lock is supplied, Condition creates an RLock internally.

USE CASE – Producer / Consumer:
  Producer  → fills buffer, calls notify() when items are available.
  Consumer  → waits when buffer is empty; wakes when notified.
  Both sides also check the reverse condition (buffer full / buffer empty).

PROS:
  - Fine-grained coordination; avoids busy-waiting.
  - Combines mutual exclusion + signalling in one object.
CONS:
  - More complex to implement correctly than a simple Lock.
  - Spurious wake-ups are possible; always re-check the condition in a loop.
"""

import logging
import threading
import time

LOG_FORMAT = "%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items     = []
condition = threading.Condition()


class Consumer(threading.Thread):
    """Consumes one item at a time; waits when the buffer is empty."""

    def consume(self):
        with condition:
            # Always re-check condition in a loop (spurious wake-ups)
            while len(items) == 0:
                logging.info("No items to consume – waiting")
                condition.wait()           # releases lock; blocks
            items.pop()
            logging.info(f"Consumed 1 item  | buffer size: {len(items)}")
            condition.notify()             # wake producer if it is waiting

    def run(self):
        for _ in range(10):
            time.sleep(1)
            self.consume()


class Producer(threading.Thread):
    """Produces items up to a max of 10; pauses when the buffer is full."""

    def produce(self):
        with condition:
            while len(items) == 10:
                logging.info(f"Buffer full ({len(items)}) – waiting")
                condition.wait()
            items.append(1)
            logging.info(f"Produced 1 item  | buffer size: {len(items)}")
            condition.notify()             # wake consumer if it is waiting

    def run(self):
        for _ in range(20):
            time.sleep(0.3)
            self.produce()


def main():
    producer = Producer(name="Producer")
    consumer = Consumer(name="Consumer")

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Done. Final buffer size:", len(items))


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 8: Thread Synchronization with a Condition")
    print("=" * 55)
    main()
