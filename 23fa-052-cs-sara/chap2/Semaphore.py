import logging      # For printing messages
import threading    # For threads and tickets
import time         # For waiting
import random       # For random numbers

# Setup for pretty printing
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Create a ticket machine with 0 tickets to start
semaphore = threading.Semaphore(0)  # No tickets available

# Box to store the item
item = 0


def consumer():
    """Customer who wants an item"""
    logging.info('Consumer is waiting')  # "I'm waiting!"
    
    semaphore.acquire()  # Try to take a ticket (waits if none)
    # ^ This person waits here until producer gives a ticket
    
    logging.info('Consumer notify: item number {}'.format(item))  # "Got my item!"


def producer():
    """Worker who makes items"""
    global item  # Use the shared box
    
    time.sleep(3)  # Take 3 seconds to make the item
    
    item = random.randint(0, 1000)  # Make a random item
    logging.info('Producer notify: item number {}'.format(item))  # "Item is ready!"
    
    semaphore.release()  # Give 1 ticket (wake up consumer)


def main():
    """Do this 10 times"""
    for i in range(10):  # Repeat 10 times
        t1 = threading.Thread(target=consumer)  # Create customer
        t2 = threading.Thread(target=producer)  # Create worker

        t1.start()  # Customer starts waiting
        t2.start()  # Worker starts making

        t1.join()   # Wait for customer
        t2.join()   # Wait for worker


if __name__ == "__main__":
    main()