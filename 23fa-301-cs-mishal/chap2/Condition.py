# Import logging module to show thread activity clearly
import logging
# Import threading module for Producer and Consumer threads
import threading
# Import time module to add delay between producing and consuming
import time

# Format for logging output: time, thread name, log level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
# Configure logging with INFO level and custom format
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
# Shared list that will hold produced items
items = []
# Create a Condition object for synchronization between Producer and Consumer
# This is used for synchronization between producer and consumer.

# It helps them:
# wait when needed
# notify each other when work can continue


# How it works step by step
# Producer side:
# If list is not full, producer adds item

# Then it says:

# "I added something"

# Consumer side:
# If list is not empty, consumer removes item

# Then it says:

# "I removed something"


condition = threading.Condition()

# Consumer class inheriting from Thread
class Consumer(threading.Thread):
     # Constructor of Consumer class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  # Function to consume an item
    def consume(self):
       # Acquire the condition lock
        with condition:
              # If there are no items, consumer must wait
            if len(items) == 0:
                logging.info('no items to consume')
                # Thread goes to sleep and waits until another thread wakes it up.
                condition.wait()
              # Remove one item from the list
            items.pop()
            logging.info('consumed 1 item')
            # Notify waiting threads after consuming  that “You can continue now.”
            condition.notify()
  # Thread execution starts from here
    def run(self):
         # Consumer will try to consume 20 times
        for i in range(20):
            # Wait 2 seconds before consuming
            time.sleep(2)
            self.consume()

# Producer class inheriting from Thread
class Producer(threading.Thread):
     # Constructor of Producer class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 # Function to produce an item
    def produce(self):
             # Acquire the condition lock
        with condition:
                # If list already has 10(max) items, producer must stop and wait
            if len(items) == 10:
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()
            # Add one item to the list
            items.append(1)
            logging.info('total items {}'.format(len(items)))
            # Notify waiting threads after producing
            condition.notify()
 # Thread execution starts from here
    def run(self):
            # Producer will try to produce 20 times
        for i in range(20):
            # Wait 0.5 seconds before producing
            time.sleep(0.5)
            self.produce()

# Main function
def main():
      # Create Producer thread
    producer = Producer(name='Producer')
     # Create Consumer thread
    consumer = Consumer(name='Consumer')

 # Start both threads
    producer.start()
    consumer.start()
 # Wait for both threads to finish
    producer.join()
    consumer.join()


# Ensure this code runs only when executed directly
if __name__ == "__main__":
    main()


#This code is showing the Producer–Consumer problem.

# There are 2 threads:
# 1) Producer
# Keeps adding items into the shared list items
# Produces 1 item every 0.5 seconds
# If the list already has 10 items, it stops and waits
# 2) Consumer
# Keeps removing items from the shared list items
# Consumes 1 item every 2 seconds
# If the list is empty, it stops and waits



# What happens overall
# Producer is faster (0.5 sec)
# Consumer is slower (2 sec)

# So usually:

# Producer fills the list quickly
# If list becomes full (10 items), producer waits
# Consumer starts removing items slowly
# Then producer is notified and continues again

# This continues until both finish their 20 loops.

#output
#2026-04-04 18:35:01,705 Producer          INFO     total items 4
# 2026-04-04 18:35:02,206 Producer          INFO     total items 5
# 2026-04-04 18:35:02,706 Producer          INFO     total items 6
# 2026-04-04 18:35:03,203 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:03,207 Producer          INFO     total items 6
# 2026-04-04 18:35:03,709 Producer          INFO     total items 7
# 2026-04-04 18:35:04,209 Producer          INFO     total items 8
# 2026-04-04 18:35:04,710 Producer          INFO     total items 9
# 2026-04-04 18:35:05,203 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:05,211 Producer          INFO     total items 9
# 2026-04-04 18:35:05,711 Producer          INFO     total items 10
# 2026-04-04 18:35:06,212 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:07,205 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:07,205 Producer          INFO     total items 10
# 2026-04-04 18:35:07,706 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:09,205 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:09,206 Producer          INFO     total items 10
# 2026-04-04 18:35:09,707 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:11,207 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:11,208 Producer          INFO     total items 10
# 2026-04-04 18:35:11,708 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:13,208 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:13,209 Producer          INFO     total items 10
# 2026-04-04 18:35:13,710 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:15,209 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:15,210 Producer          INFO     total items 10
# 2026-04-04 18:35:15,711 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:17,210 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:17,211 Producer          INFO     total items 10
# 2026-04-04 18:35:17,712 Producer          INFO     items produced 10. Stopped
# 2026-04-04 18:35:19,211 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:19,212 Producer          INFO     total items 10
# 2026-04-04 18:35:21,212 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:23,213 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:25,214 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:27,215 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:29,216 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:31,218 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:33,219 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:35,219 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:37,220 Consumer          INFO     consumed 1 item
# 2026-04-04 18:35:39,221 Consumer          INFO     consumed 1 item