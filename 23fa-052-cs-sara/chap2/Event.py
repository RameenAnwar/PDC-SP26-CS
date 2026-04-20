import logging      # For printing messages
import threading    # For running Producer and Consumer at the same time
import time         # For adding delays
import random       # For generating random numbers

# Setup for pretty message printing
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared box to store items (starts empty)
items = []

# A doorbell to signal Consumer (Event = signal)
event = threading.Event()


class Consumer(threading.Thread):
    """Consumer = Person who TAKES items from box"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        # Keep trying to take items forever
        while True:
            time.sleep(2)           # Wait 2 seconds before each try
            event.wait()            # Wait for doorbell to ring 
            item = items.pop()      # Take item from box
            logging.info('Consumer notify: {} popped by {}'.format(item, self.name))


class Producer(threading.Thread):
    """Producer = Person who MAKES and ADDS items to box"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        # Make exactly 5 items
        for i in range(5):
            time.sleep(2)           # Take 2 seconds to make 1 item
            item = random.randint(0, 100)   # Create random item
            items.append(item)              # Put item in box
            logging.info('Producer notify: item {} appended by {}'.format(item, self.name))
            event.set()             # Ring doorbell! 
            event.clear()           # Reset doorbell (ring only once)


# Start the race
if __name__ == "__main__":
    t1 = Producer()   # Create Producer
    t2 = Consumer()   # Create Consumer

    t1.start()        # Start Producer
    t2.start()        # Start Consumer

    t1.join()         # Wait for Producer to finish
    t2.join()         # Wait for Consumer (but it never finishes!)