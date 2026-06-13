import logging  # For printing messages with time and thread info
import threading  # To use threads
import time  # For delays
import random  # To generate random numbers

# Set logging format to show time, thread name, level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []  # Shared list for producer and consumer
event = threading.Event()  # Event to notify consumer when item is added


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:  # Keep consuming items continuously
            time.sleep(2)  # Wait for 2 seconds
            event.wait()  # Wait until producer sets the event
            item = items.pop()  # Remove an item from the list
            logging.info('Consumer notify: {} popped by {}'\
                         .format(item, self.name))  # Show which item was consumed

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):  # Produce 5 items
            time.sleep(2)  # Wait 2 seconds between production
            item = random.randint(0, 100)  # Generate a random number
            items.append(item)  # Add item to the shared list
            logging.info('Producer notify: item {} appended by {}'\
                         .format(item, self.name))  # Show which item was added
            event.set()  # Notify consumer
            event.clear()  # Clear event for next item

if __name__ == "__main__":
    t1 = Producer()  # Create producer thread
    t2 = Consumer()  # Create consumer thread

    t1.start()  # Start producer thread
    t2.start()  # Start consumer thread

    t1.join()  # Wait until producer finishes
    t2.join()  # Wait until consumer finishes