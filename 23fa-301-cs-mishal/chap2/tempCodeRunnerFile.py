# Thread synchronization example using Queue
from threading import Thread  # Import Thread class to create threads
from queue import Queue      # Import Queue class to handle thread-safe queues
import time                  # Import time module to add delays
import random                # Import random module to generate random numbers

# Producer class that generates items and puts them in the queue
class Producer(Thread):

    # Constructor takes the shared queue as input
    def __init__(self, queue):
        Thread.__init__(self)  # Initialize parent Thread class
        self.queue = queue     # Store reference to shared queue

    # Code executed when thread starts
    def run(self):
        for i in range(5):  # Produce 5 items
            item = random.randint(0, 256)  # Generate random number
            self.queue.put(item)           # Add item to the queue
            print('Producer notify : item N°%d appended to queue by %s\n'\
                  % (item, self.name))   # Notify which item was added by which thread
            time.sleep(1)                 # Wait 1 second before producing next item

# Consumer class that takes items from the queue
class Consumer(Thread):

    # Constructor takes the shared queue as input
    def __init__(self, queue):
        Thread.__init__(self)  # Initialize parent Thread class
        self.queue = queue     # Store reference to shared queue

    # Code executed when thread starts
    def run(self):
        while True:  # Continuously consume items
            item = self.queue.get()  # Remove item from queue (waits if empty)
            print('Consumer notify : %d popped from queue by %s'\
                  % (item, self.name))  # Notify which item was popped by which thread
            self.queue.task_done()     # Mark the task as done

# Main section to create and run threads
if __name__ == '__main__':
    queue = Queue()  # Create a shared queue

    # Create threads: 1 producer and 3 consumers
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()