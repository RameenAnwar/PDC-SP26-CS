import multiprocessing
import random
import time

# Producer process: generates random numbers and adds to queue
class producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)  # Generate random number
            self.queue.put(item)  # Add to queue
            print("Producer:", item, "added by", self.name)
            time.sleep(1)
            print("Queue size:", self.queue.qsize())


# Consumer process: removes items from queue
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()  # Remove item
                print("Consumer:", item, "removed by", self.name)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    process_producer = producer(queue)
    process_consumer = consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()