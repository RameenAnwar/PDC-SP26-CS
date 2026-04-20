import multiprocessing  # For running multiple processes
import random           # For generating random numbers
import time             # For adding delays

# PRODUCER CLASS - Creates/produces data
class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)  # Initialize parent class
        self.queue = queue  # Store the queue

    def run(self) :
        for i in range(10):  # Loop 10 times
            item = random.randint(0, 256)  # Generate random number between 0-256
            self.queue.put(item)  # Add item to queue
            print ("Process Producer : item %d appended to queue %s"\
                   % (item, self.name))  # Show which item was added
            time.sleep(1)  # Wait 1 second
            print ("The size of queue is %s"\
                   % self.queue.qsize())  # Show current queue size

# CONSUMER CLASS - Consumes/uses data       
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)  # Initialize parent class
        self.queue = queue  # Store the queue

    def run(self):
        while True:  # Run forever
            if (self.queue.empty()):  # Check if queue is empty
                print("the queue is empty")
                break  # Exit loop
            else :  # If queue has items
                time.sleep(2)  # Wait 2 seconds
                item = self.queue.get()  # Remove item from queue
                print ('Process Consumer : item %d popped \
                        from by %s \n'\
                       % (item, self.name))  # Show which item was removed
                time.sleep(1)  # Wait 1 second

# MAIN PROGRAM - Starts here
if __name__ == '__main__':
        queue = multiprocessing.Queue()  # Create a queue
        process_producer = producer(queue)  # Create producer process
        process_consumer = consumer(queue)  # Create consumer process
        process_producer.start()  # Start producer
        process_consumer.start()  # Start consumer
        process_producer.join()   # Wait for producer to finish
        process_consumer.join()   # Wait for consumer to finish