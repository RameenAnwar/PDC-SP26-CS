"""
Chapter 2 – Topic 11: Thread Communication Using a Queue
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  queue.Queue is a thread-safe FIFO data structure designed specifically
  for passing data between threads.  Internal locking is handled
  automatically – no manual Lock management needed.

KEY METHODS:
  put(item)          – add an item (blocks if maxsize reached)
  get()              – remove & return an item (blocks if queue is empty)
  task_done()        – signal that a previously get()'d item is fully processed
  join()             – block the caller until every item has had task_done() called
  qsize()            – approximate queue size (not reliable for synchronisation)
  empty()            – True if queue is empty (use for info only, not as guard)

put() / get() optional args:
  block=True  (default) – block if full/empty
  block=False           – raise queue.Full / queue.Empty immediately
  timeout=N             – wait at most N seconds, then raise Full/Empty

WHY PREFER QUEUE OVER MANUAL LOCKS?
  - Thread-safe by design; no risk of forgetting a release().
  - Cleaner producer/consumer pattern.
  - Decouples producers from consumers (different counts, speeds).
  - Supports back-pressure via maxsize.

FLOW:
  Producer → put(item)  →  [Queue]  →  get() + task_done() → Consumer
"""

import threading
import time
import random
from threading import Thread
from queue import Queue


# ── Classic Producer / Consumer ───────────────────────────────────────────────

class Producer(Thread):
    """Generates random integers and puts them into the shared queue."""

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for _ in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Producer notify: item N°{item} appended to queue by {self.name}")
            time.sleep(1)


class Consumer(Thread):
    """Retrieves integers from the shared queue and marks each as done."""

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.daemon = True   # exits when the main thread / join() finishes

    def run(self):
        while True:
            item = self.queue.get()        # blocks if queue is empty
            print(f"Consumer notify: {item} popped from queue by {self.name}")
            self.queue.task_done()         # signal that item is fully processed


def demo_basic_queue():
    print("\n--- Basic Producer / Consumer (1 producer, 3 consumers) ---")
    q  = Queue()
    t1 = Producer(q)
    t2 = Consumer(q)
    t3 = Consumer(q)
    t4 = Consumer(q)

    t1.start(); t2.start(); t3.start(); t4.start()

    t1.join()    # wait for producer to finish
    q.join()     # wait until all put items have been task_done()'d


# ── Bounded Queue (back-pressure) ─────────────────────────────────────────────

def demo_bounded_queue():
    """
    maxsize=3 limits the queue to 3 items.
    Producer blocks when full; consumer drains items, unblocking producer.
    """
    print("\n--- Bounded Queue (maxsize=3) ---")
    q = Queue(maxsize=3)

    def slow_consumer():
        while True:
            item = q.get()
            print(f"  Consumed {item} | queue size now: {q.qsize()}")
            time.sleep(0.8)
            q.task_done()

    def fast_producer():
        for i in range(8):
            print(f"  Putting item {i} | queue size: {q.qsize()}")
            q.put(i)              # blocks when queue is full (size == 3)
            print(f"  Put  item {i} done")

    consumer_thread = Thread(target=slow_consumer, daemon=True)
    producer_thread = Thread(target=fast_producer)

    consumer_thread.start()
    producer_thread.start()

    producer_thread.join()
    q.join()


def main():
    demo_basic_queue()
    demo_bounded_queue()
    print("\nAll demos complete.")


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 11: Thread Communication Using a Queue")
    print("=" * 55)
    main()
