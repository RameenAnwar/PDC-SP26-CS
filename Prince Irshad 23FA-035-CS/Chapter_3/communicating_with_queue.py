import multiprocessing
import random
import time

# Producer class creates data and puts it in the queue
class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        # Store the shared queue
        self.queue = queue

    def run(self):
        # Create 10 random items
        for i in range(10):
            # Generate a random number between 0 and 256
            item = random.randint(0, 256)
            # Add the item to the shared queue
            self.queue.put(item) 
            print("Process Producer : item %d appended to queue %s"\
                % (item,self.name))
            # Wait for 1 second
            time.sleep(1)
            # Print how many items are in the queue right now
            print("The size of queue is %s"\
                % self.queue.qsize())

# Consumer class takes data from the queue and processes it
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        # Store the shared queue
        self.queue = queue

    def run(self):
        # Keep running continuously
        while True:
            # Check if there is no data left in the queue
            if (self.queue.empty()):
                print("the queue is empty")
                # Stop the loop if queue is empty
                break
            else:
                # Wait for 2 seconds before taking an item
                time.sleep(2)
                # Take one item out of the queue
                item = self.queue.get()
                print('Process Consumer : item %d popped \
        from by %s \n'\
               % (item, self.name))
                # Wait for 1 second
                time.sleep(1)

if __name__ == '__main__':
    # Create a shared queue
    queue = multiprocessing.Queue()
    # Create producer and consumer objects
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    # Start both processes to run at the same time
    process_producer.start()
    process_consumer.start()
    # Wait for both processes to finish
    process_producer.join()
    process_consumer.join()