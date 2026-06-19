import logging
import threading
import time
import random

# Log format to include time, thread name, log level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'

# Configure logging system
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore initialized with 0:
# This means consumers will BLOCK (wait) until a producer releases it
semaphore = threading.Semaphore(0)

# Shared variable between producer and consumer
item = 0


def consumer():
    # Consumer thread starts and waits for a signal from producer
    logging.info('Consumer is waiting')
    
    # Acquire semaphore:
    # Since initial value is 0, this will block until producer calls release()
    semaphore.acquire()
    
    # Once unblocked, consumer can access the produced item
    logging.info('Consumer notify: item number {}'.format(item))


def producer():
    global item
    
    # Simulate delay in producing an item
    time.sleep(3)
    
    # Generate a random item (simulating production)
    item = random.randint(0, 1000)
    
    # Log produced item
    logging.info('Producer notify: item number {}'.format(item))
    
    # Release semaphore:
    # This increments semaphore count and wakes up one waiting consumer
    semaphore.release()


def main():
    # Run the producer-consumer process 10 times
    for i in range(10):
        
        # Create a consumer thread
        t1 = threading.Thread(target=consumer)
        
        # Create a producer thread
        t2 = threading.Thread(target=producer)

        # Start both threads
        t1.start()
        t2.start()

        # Wait for both threads to complete before next iteration
        t1.join()
        t2.join()


# Entry point of the program
if __name__ == "__main__":
    main()