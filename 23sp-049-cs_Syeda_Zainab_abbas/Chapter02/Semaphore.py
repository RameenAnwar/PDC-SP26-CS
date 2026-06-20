# Semaphore.py
# A SEMAPHORE used as a producer/consumer signal. It starts at 0, so the consumer
# blocks on acquire() until the producer calls release() - guaranteeing the consumer
# only reads the item AFTER the producer has created it.

import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)    # counter starts at 0 -> acquire() will block
item = 0

def consumer():
    logging.info('Consumer is waiting')
    semaphore.acquire()               # blocks until producer releases the semaphore
    logging.info('Consumer notify: item number {}'.format(item))

def producer():
    global item
    time.sleep(3)                     # take some time to "produce"
    item = random.randint(0, 1000)
    logging.info('Producer notify: item number {}'.format(item))
    semaphore.release()               # signal the waiting consumer

def main():
    for i in range(10):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start(); t2.start()
        t1.join();  t2.join()

if __name__ == "__main__":
    main()
