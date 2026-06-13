import logging  # For showing messages in the console
import threading  # To use threads
import time  # For delays and sleeping

# Set logging format to show time, thread name, level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []  # Shared list for producer and consumer
condition = threading.Condition()  # Condition to control access to the shared list


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:  # Acquire lock before accessing shared list
            if len(items) == 0:  # If no items, wait for producer
                logging.info('no items to consume')
                condition.wait()

            items.pop()  # Remove one item from the list
            logging.info('consumed 1 item')

            condition.notify()  # Notify producer that an item was consumed

    def run(self):
        for i in range(20):  # Consume 20 times
            time.sleep(2)  # Wait 2 seconds between consumption
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:  # Acquire lock before modifying shared list
            if len(items) == 10:  # If list is full, wait for consumer
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)  # Add one item to the list
            logging.info('total items {}'.format(len(items)))

            condition.notify()  # Notify consumer that a new item is available

    def run(self):
        for i in range(20):  # Produce 20 times
            time.sleep(0.5)  # Wait 0.5 seconds between production
            self.produce()


def main():
    producer = Producer(name='Producer')  # Create producer thread
    consumer = Consumer(name='Consumer')  # Create consumer thread

    producer.start()  # Start producer thread
    consumer.start()  # Start consumer thread

    producer.join()  # Wait until producer finishes
    consumer.join()  # Wait until consumer finishes


if __name__ == "__main__":
    main()  # Run the main function