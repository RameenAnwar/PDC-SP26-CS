import multiprocessing
import random
import time

# Producer class - inherits from Process
# This process will keep adding items to the queue
class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)  # Call parent class constructor
        self.queue = queue  # Store the queue reference

    def run(self) :
        # Produce 10 random items
        for i in range(10):
            item = random.randint(0, 256)  # Generate random number between 0-256
            self.queue.put(item)  # Add item to the shared queue
            print ("Process Producer : item %d appended to queue %s"\
                   % (item,self.name))  # name is automatically given by Process class
            time.sleep(1)  # Wait 1 second before next item
            print ("The size of queue is %s"\
                   % self.queue.qsize())  # Check how many items are waiting in queue
       
# Consumer class - inherits from Process
# This process will remove items from the queue and process them
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)  # Call parent class constructor
        self.queue = queue  # Store the same queue reference

    def run(self):
        # Keep consuming until queue becomes empty
        while True:
            if (self.queue.empty()):  # Check if there are no more items
                print("the queue is empty")
                break  # Exit the loop and end the process
            else :
                time.sleep(2)  # Consumer is slower than producer (2 sec delay)
                item = self.queue.get()  # Remove an item from queue
                print ('Process Consumer : item %d popped \
                        from by %s \n'\
                       % (item, self.name))
                time.sleep(1)  # Another small delay after processing


if __name__ == '__main__':
        # Create a shared Queue that both processes can use
        queue = multiprocessing.Queue()
        
        # Create producer and consumer process objects
        process_producer = producer(queue)
        process_consumer = consumer(queue)
        
        # Start both processes (they will now run in parallel)
        process_producer.start()
        process_consumer.start()
        
        # Wait for both processes to finish before exiting the main program
        process_producer.join()
        process_consumer.join()

