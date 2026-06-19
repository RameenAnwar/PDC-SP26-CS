import logging
import threading
import time

# Logging format to show time, thread name, log level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resource (buffer) between Producer and Consumer
items = []

# Condition object used for synchronization (lock + wait/notify)
condition = threading.Condition()


# 🔹 Consumer Thread Class
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        # Initialize thread with given name or arguments
        super().__init__(*args, **kwargs)

    def consume(self):
        # Acquire the condition lock before accessing shared data
        with condition:

            # If no items are available, wait until producer notifies
            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()

            # Remove an item from the shared list
            items.pop()
            logging.info('consumed 1 item')

            # Notify producer that space is now available
            condition.notify()

    def run(self):
        # Run consume() multiple times
        for i in range(20):
            time.sleep(2)  # Simulate slow consumption
            self.consume()


# 🔹 Producer Thread Class
class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        # Initialize thread
        super().__init__(*args, **kwargs)

    def produce(self):
        # Acquire the condition lock before modifying shared data
        with condition:

            # If buffer is full (limit = 10), wait until consumer consumes
            if len(items) == 10:
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()

            # Add an item to the shared list
            items.append(1)
            logging.info('total items {}'.format(len(items)))

            # Notify consumer that a new item is available
            condition.notify()

    def run(self):
        # Run produce() multiple times
        for i in range(20):
            time.sleep(0.5)  # Simulate fast production
            self.produce()


# 🔹 Main function to start threads
def main():
    # Create producer and consumer threads
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    # Start both threads
    producer.start()
    consumer.start()

    # Wait for both threads to finish execution
    producer.join()
    consumer.join()


# Entry point of the program
if __name__ == "__main__":
    main()