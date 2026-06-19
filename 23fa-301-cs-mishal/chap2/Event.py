# Import logging module to show thread messages
import logging

# Import threading module for creating threads
import threading

# Import time module to add delays
import time

# Import random module to generate random numbers
import random

# Format for log output: time, thread name, level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'

# Set up logging with INFO level and custom format
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared list where produced items will be stored
items = []

# Create an Event object for synchronization between producer and consumer
event = threading.Event()


# Consumer class inheriting from Thread
class Consumer(threading.Thread):
    
    # Constructor of Consumer class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Code that runs when the consumer thread starts
    def run(self):
        # Keep consuming forever
        while True:
            # Wait 2 seconds before trying to consume
            time.sleep(2)
            
            # Wait until producer gives signal that item is available
            event.wait()
            
            # Remove one item from the shared list
            item = items.pop()
            
            # Print which item was consumed and by which thread
            logging.info('Consumer notify: {} popped by {}'\
                         .format(item, self.name))


# Producer class inheriting from Thread
class Producer(threading.Thread):
    
    # Constructor of Producer class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Code that runs when the producer thread starts
    def run(self):
        # Produce 5 items
        for i in range(5):
            # Wait 2 seconds before producing
            time.sleep(2)
            
            # Generate a random integer between 0 and 100
            item = random.randint(0, 100)
            
            # Add the produced item to the shared list
            items.append(item)
            
            # Print which item was produced and by which thread
            logging.info('Producer notify: item {} appended by {}'\
                         .format(item, self.name))
            
            # Signal the consumer that an item is available
            event.set()
            
            # Reset the event signal
            event.clear()


# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    
    # Create producer thread
    t1 = Producer()
    
    # Create consumer thread
    t2 = Consumer()

    # Start producer thread
    t1.start()
    
    # Start consumer thread
    t2.start()

    # Wait for producer thread to finish
    t1.join()
    
    # Wait for consumer thread to finish
    t2.join()

   # This code demonstrates the Producer–Consumer problem using multithreading and Event synchronization in Python.
   #  A shared list items acts as a buffer where the Producer thread generates random integers and adds them to the list,
   #  while the Consumer thread waits for a signal and then removes items from the list. The Event object is used as a signal:
   #  the producer calls event.set() to notify the consumer that an item is available, and the consumer uses event.wait() to pause until that signal is received.
   #  This example shows how threads can coordinate with each other using events while working on shared data.


#    #output
#    2026-04-04 19:19:50,477 Thread-1          INFO     Producer notify: item 44 appended by Thread-1
# 2026-04-04 19:19:50,478 Thread-2          INFO     Consumer notify: 44 popped by Thread-2
# 2026-04-04 19:19:52,478 Thread-1          INFO     Producer notify: item 90 appended by Thread-1
# 2026-04-04 19:19:52,479 Thread-2          INFO     Consumer notify: 90 popped by Thread-2
# 2026-04-04 19:19:54,480 Thread-1          INFO     Producer notify: item 44 appended by Thread-1
# 2026-04-04 19:19:54,481 Thread-2          INFO     Consumer notify: 44 popped by Thread-2
# 2026-04-04 19:19:56,481 Thread-1          INFO     Producer notify: item 93 appended by Thread-1
# 2026-04-04 19:19:56,482 Thread-2          INFO     Consumer notify: 93 popped by Thread-2
# 2026-04-04 19:19:58,482 Thread-1          INFO     Producer notify: item 78 appended by Thread-1
# 2026-04-04 19:19:58,483 Thread-2          INFO     Consumer notify: 78 popped by Thread-2