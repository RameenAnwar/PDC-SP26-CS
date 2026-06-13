# Import logging module to display thread messages
import logging

# Import threading module for creating threads and semaphore
import threading

# Import time module to add delay
import time

# Import random module to generate random item numbers
import random

# Format for logging output: time, thread name, level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'

# Configure logging with INFO level and custom format
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


# Create a semaphore with initial value 0
# This means consumer will wait until producer releases it
semaphore = threading.Semaphore(0)

# Shared variable to store produced item
item = 0


# Consumer function
def consumer():
    # Print that consumer is waiting
    logging.info('Consumer is waiting')
    
    # Acquire semaphore
    # If semaphore value is 0, consumer will block and wait
    semaphore.acquire()
    
    # Print consumed item after producer signals
    logging.info('Consumer notify: item number {}'.format(item))


# Producer function
def producer():
    # Use global item variable so we can modify it
    global item
    
    # Wait 3 seconds before producing
    time.sleep(3)
    
    # Generate a random item number between 0 and 1000
    item = random.randint(0, 1000)
    
    # Print produced item
    logging.info('Producer notify: item number {}'.format(item))
    
    # Release semaphore to signal consumer
    semaphore.release()


# Main function
def main():
    # Run producer-consumer pair 10 times
    for i in range(10):
        
        # Create consumer thread
        t1 = threading.Thread(target=consumer)
        
        # Create producer thread
        t2 = threading.Thread(target=producer)

        # Start consumer thread
        t1.start()
        
        # Start producer thread
        t2.start()

        # Wait for consumer thread to finish
        t1.join()
        
        # Wait for producer thread to finish
        t2.join()


# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    main()

    #This code demonstrates the Producer–Consumer problem using a Semaphore in Python multithreading.
    #  A shared variable item is used to store a produced value, while the Consumer thread waits for permission before accessing it.
    #  The semaphore is initialized to 0, which causes the consumer to block until the Producer thread generates a random item and signals availability using semaphore.release().
    #  The consumer then continues by calling semaphore.acquire() and prints the item. This process is repeated 10 times,
    #  showing how a semaphore can be used to synchronize threads and control access to shared resources.

# output
# 2026-04-04 20:51:17,972 Thread-1 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:20,974 Thread-2 (producer) INFO     Producer notify: item number 912
# 2026-04-04 20:51:20,974 Thread-1 (consumer) INFO     Consumer notify: item number 912
# 2026-04-04 20:51:20,976 Thread-3 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:23,977 Thread-4 (producer) INFO     Producer notify: item number 272
# 2026-04-04 20:51:23,977 Thread-3 (consumer) INFO     Consumer notify: item number 272
# 2026-04-04 20:51:23,979 Thread-5 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:26,979 Thread-6 (producer) INFO     Producer notify: item number 804
# 2026-04-04 20:51:26,980 Thread-5 (consumer) INFO     Consumer notify: item number 804
# 2026-04-04 20:51:26,981 Thread-7 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:29,983 Thread-8 (producer) INFO     Producer notify: item number 51
# 2026-04-04 20:51:29,983 Thread-7 (consumer) INFO     Consumer notify: item number 51
# 2026-04-04 20:51:29,984 Thread-9 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:32,985 Thread-10 (producer) INFO     Producer notify: item number 135
# 2026-04-04 20:51:32,986 Thread-9 (consumer) INFO     Consumer notify: item number 135
# 2026-04-04 20:51:32,986 Thread-11 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:35,988 Thread-12 (producer) INFO     Producer notify: item number 609
# 2026-04-04 20:51:35,988 Thread-11 (consumer) INFO     Consumer notify: item number 609
# 2026-04-04 20:51:35,989 Thread-13 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:38,990 Thread-14 (producer) INFO     Producer notify: item number 29
# 2026-04-04 20:51:38,990 Thread-13 (consumer) INFO     Consumer notify: item number 29
# 2026-04-04 20:51:38,991 Thread-15 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:41,992 Thread-16 (producer) INFO     Producer notify: item number 260
# 2026-04-04 20:51:41,992 Thread-15 (consumer) INFO     Consumer notify: item number 260
# 2026-04-04 20:51:41,993 Thread-17 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:44,994 Thread-18 (producer) INFO     Producer notify: item number 63
# 2026-04-04 20:51:44,995 Thread-17 (consumer) INFO     Consumer notify: item number 63
# 2026-04-04 20:51:44,996 Thread-19 (consumer) INFO     Consumer is waiting
# 2026-04-04 20:51:47,997 Thread-20 (producer) INFO     Producer notify: item number 398
# 2026-04-04 20:51:47,997 Thread-19 (consumer) INFO     Consumer notify: item number 398
