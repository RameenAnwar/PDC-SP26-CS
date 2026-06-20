# Event.py
# Producer/Consumer using an EVENT. An Event is a simple flag threads can wait on.
# The producer set()s the event after appending an item, which lets the waiting
# consumer proceed; clear() resets the flag.

import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()             # starts "unset" (False)

class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(2)
            event.wait()              # block until the event is set by the producer
            item = items.pop()
            logging.info('Consumer notify: {} popped by {}'.format(item, self.name))

class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Producer notify: item {} appended by {}'.format(item, self.name))
            event.set()               # signal the consumer that an item is ready
            event.clear()             # reset the flag for the next round

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()
    t1.start(); t2.start()
    t1.join();  t2.join()
