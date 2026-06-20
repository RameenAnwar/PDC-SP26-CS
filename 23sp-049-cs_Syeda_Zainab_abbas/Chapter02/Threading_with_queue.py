# Threading_with_queue.py
# Thread synchronisation using a thread-safe QUEUE. The Queue handles all locking
# internally, so it is the safest/cleanest way to pass data between threads.
# One Producer puts items in; three Consumers take them out concurrently.

from threading import Thread
from queue import Queue
import time
import random

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)      # put() is thread-safe
            print('Producer notify : item N°%d appended to queue by %s\n' % (item, self.name))
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            item = self.queue.get()   # get() blocks until an item is available
            print('Consumer notify : %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()    # mark this item as processed

if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join();  t2.join();  t3.join();  t4.join()
