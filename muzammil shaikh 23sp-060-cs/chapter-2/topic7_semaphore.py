"""
Chapter 2 – Topic 7: Thread Synchronization with Semaphores
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  A Semaphore is an OS-managed counter that controls how many threads
  can access a shared resource simultaneously.

HOW IT WORKS:
  acquire() → decrements the counter.
               If counter == 0, the calling thread BLOCKS until another
               thread calls release().
  release() → increments the counter, waking one blocked thread (if any).

COMMON PATTERNS:
  Semaphore(0)  – "event" semaphore: producer signals consumer.
                  Consumer blocks at acquire() until producer calls release().
  Semaphore(N)  – limits concurrent access to N threads (e.g. connection pool).
  Semaphore(1)  – equivalent to a mutex (same as Lock, but any thread can release).

INVENTED BY:
  Edsger W. Dijkstra – one of the oldest synchronisation primitives in CS.

RISKS:
  - Forgetting to call release() can starve waiting threads.
  - Circular waits between semaphores cause deadlocks.

SPECIAL CASE – BoundedSemaphore:
  threading.BoundedSemaphore(N) raises ValueError if release() is called
  more times than acquire(), preventing accidental counter inflation.
"""

import logging
import threading
import time
import random

LOG_FORMAT = "%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore(0) → counter starts at 0, so consumer blocks immediately
semaphore = threading.Semaphore(0)
item = 0


def consumer():
    """Waits (blocks) until the producer signals that an item is ready."""
    logging.info("Consumer is waiting")
    semaphore.acquire()                  # blocks until counter > 0
    logging.info(f"Consumer notify: item number {item}")


def producer():
    """Sleeps, creates an item, then signals the consumer."""
    global item
    time.sleep(2)
    item = random.randint(0, 1000)
    logging.info(f"Producer notify: item number {item}")
    semaphore.release()                  # increments counter → unblocks consumer


def demo_event_semaphore():
    """Run 5 producer-consumer pairs using a Semaphore(0) as an event signal."""
    print("\n--- Semaphore(0) as event signal (5 pairs) ---")
    threads = []
    for _ in range(5):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        threads.extend([t1, t2])
        t1.start()
        t2.start()
    for t in threads:
        t.join()


def demo_bounded_semaphore():
    """Semaphore(3) → at most 3 threads inside the critical section at once."""
    print("\n--- BoundedSemaphore(3): connection-pool simulation ---")
    pool = threading.BoundedSemaphore(3)

    def use_connection(name):
        pool.acquire()
        logging.info(f"{name} acquired connection")
        time.sleep(random.uniform(0.5, 1.5))
        logging.info(f"{name} released connection")
        pool.release()

    workers = [
        threading.Thread(name=f"Worker-{i}", target=use_connection, args=(f"Worker-{i}",))
        for i in range(7)
    ]
    for w in workers:
        w.start()
    for w in workers:
        w.join()


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 7: Thread Synchronization with Semaphores")
    print("=" * 55)
    demo_event_semaphore()
    demo_bounded_semaphore()
