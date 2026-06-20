# communicating_with_queue.py
# Inter-process communication (IPC) using a multiprocessing.Queue. The producer
# process puts random items in; the consumer process reads them until the queue
# is empty. The Queue safely passes data between SEPARATE processes.

import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)              # add item to the shared queue
            print("Process Producer : item %d appended to queue %s" % (item, self.name))
            time.sleep(1)
            print("The size of queue is %s" % self.queue.qsize())

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            if self.queue.empty():            # stop once nothing is left
                print("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()       # remove item from the queue
                print('Process Consumer : item %d popped from by %s \n' % (item, self.name))
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
