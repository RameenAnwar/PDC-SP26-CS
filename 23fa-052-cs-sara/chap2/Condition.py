import logging
import threading
import time

# Just setup for showing messages with time stamps
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# The shared box where items are kept (starts empty)
items = []

# A calling bell to wake each other up
condition = threading.Condition()


class Consumer(threading.Thread):
    """The person who TAKES items"""
    
    def consume(self):
        with condition:  # Pick up the phone
            
            if len(items) == 0:  # If box is empty
                logging.info('no items to consume')  # Say "nothing to take"
                condition.wait()  # Sleep and wait for items
            
            items.pop()  # Take 1 item
            logging.info('consumed 1 item')  # Say "took 1 item"
            
            condition.notify()  # Wake up the maker
    
    def run(self):
        for i in range(20):  # Try 20 times
            time.sleep(2)    # Wait 2 seconds between each try
            self.consume()   # Take an item


class Producer(threading.Thread):
    """The person who MAKES items"""
    
    def produce(self):
        with condition:  # Pick up the phone
            
            if len(items) == 10:  # If box is full (10 items max)
                logging.info('items produced {}. Stopped'.format(len(items)))  # Say "box full"
                condition.wait()  # Sleep and wait for space
            
            items.append(1)  # Add 1 item
            logging.info('total items {}'.format(len(items)))  # Say how many items now
            
            condition.notify()  # Wake up the taker
    
    def run(self):
        for i in range(20):   # Make 20 items
            time.sleep(0.5)   # Takes 0.5 seconds to make each
            self.produce()    # Make and add to box


def main():
    # Create both persons
    producer = Producer(name='Producer')  # The maker
    consumer = Consumer(name='Consumer')  # The taker
    
    # Start them working
    producer.start()
    consumer.start()
    
    # Wait for both to finish
    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()