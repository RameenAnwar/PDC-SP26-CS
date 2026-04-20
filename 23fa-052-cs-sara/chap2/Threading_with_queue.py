"""Thread synchronisation with queue"""
# Queue automatically handles locking - no need for manual locks!

from threading import Thread  # For creating threads
from queue import Queue       # For thread-safe queue (automatic locking)
import time                   # For delays
import random                 # For random numbers


class Producer(Thread):
    """Producer - adds items to the queue"""
    
    def __init__(self, queue):
        Thread.__init__(self)  # Initialize the Thread parent class
        self.queue = queue     # Store the shared queue

    def run(self):
        """Producer makes 5 items"""
        for i in range(5):     # Make 5 items
            item = random.randint(0, 256)  # Create random item (0-256)
            self.queue.put(item)  # Add item to queue (thread-safe!)
            print('Producer notify : item N°%d appended to queue by %s\n'\
                  % (item, self.name))
            time.sleep(1)  # Take 1 second to make next item


class Consumer(Thread):
    """Consumer - removes items from the queue"""
    
    def __init__(self, queue):
        Thread.__init__(self)  # Initialize the Thread parent class
        self.queue = queue     # Store the shared queue

    def run(self):
        """Consumer runs forever taking items"""
        while True:  # Keep running (never stops!)
            item = self.queue.get()  # Take item from queue (waits if empty)
            print('Consumer notify : %d popped from queue by %s'\
                  % (item, self.name))
            self.queue.task_done()  # Tell queue this item is processed


if __name__ == '__main__':
    # Create a shared queue (automatically thread-safe!)
    queue = Queue()  # No size limit (can grow forever)

    # Create 1 producer and 3 consumers
    t1 = Producer(queue)  # 1 producer (makes items)
    t2 = Consumer(queue)  # Consumer 1 (takes items)
    t3 = Consumer(queue)  # Consumer 2 (takes items)
    t4 = Consumer(queue)  # Consumer 3 (takes items)

    # Start all threads
    t1.start()  # Producer starts making
    t2.start()  # Consumer 1 starts waiting
    t3.start()  # Consumer 2 starts waiting
    t4.start()  # Consumer 3 starts waiting

    # Wait for threads to finish
    t1.join()   # Wait for producer to finish (5 items)
    t2.join()   # Wait for consumer 1 (but never finishes!)
    t3.join()   # Wait for consumer 2 (never finishes)
    t4.join()   # Wait for consumer 3 (never finishes)