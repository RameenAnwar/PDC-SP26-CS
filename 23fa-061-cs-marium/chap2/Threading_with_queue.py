"""Thread synchronization using Queue"""

from threading import Thread  # To create threads
from queue import Queue  # Thread-safe queue
import time  # For delays
import random  # To generate random items

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue  # Shared queue for producer and consumers

    def run(self):
        for i in range(5):  # Produce 5 items
            item = random.randint(0, 256)  # Generate random item
            self.queue.put(item)  # Add item to queue
            print('Producer notify : item N°%d appended to queue by %s\n'\
                  % (item, self.name))
            time.sleep(1)  # Wait 1 second before producing next item

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue  # Shared queue to consume from

    def run(self):
        while True:  # Keep consuming indefinitely
            item = self.queue.get()  # Get item from queue
            print('Consumer notify : %d popped from queue by %s'\
                  % (item, self.name))
            self.queue.task_done()  # Signal that the task is done

if __name__ == '__main__':
    queue = Queue()  # Create a shared queue

    # Create threads
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    # Start threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()