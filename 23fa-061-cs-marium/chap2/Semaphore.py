import logging  # For showing messages with time, thread info, and level
import threading  # To use threads and semaphores
import time  # For delays
import random  # To generate random numbers

# Logging format to show time, thread name, level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)  # Semaphore initialized to 0
item = 0  # Shared item between producer and consumer

def consumer():
    logging.info('Consumer is waiting')  # Show that consumer is waiting
    semaphore.acquire()  # Wait until producer releases semaphore
    logging.info('Consumer notify: item number {}'.format(item))  # Show consumed item

def producer():
    global item
    time.sleep(3)  # Wait for 3 seconds before producing
    item = random.randint(0, 1000)  # Produce a random item
    logging.info('Producer notify: item number {}'.format(item))  # Show produced item
    semaphore.release()  # Release semaphore to notify consumer

def main():
    for i in range(10):  # Run 10 iterations
        t1 = threading.Thread(target=consumer)  # Create consumer thread
        t2 = threading.Thread(target=producer)  # Create producer thread

        t1.start()  # Start consumer
        t2.start()  # Start producer

        t1.join()  # Wait for consumer to finish
        t2.join()  # Wait for producer to finish

if __name__ == "__main__":
    main()  # Run the main function