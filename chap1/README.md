1) Barrier.py
Topic:
   Barrier (Thread synchronization point)

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3 # Number of threads that must wait at the barrier
finish_line = Barrier(num_runners)   # Barrier will block threads until 3 threads call wait()
runners = ['Huey', 'Dewey', 'Louie']  # List of thread names
def runner():
    name = runners.pop()     # Each thread takes one name
    
    sleep(randrange(2, 5))    # Simulate running time
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()    # Wait at barrier until all threads arrive

def main():
    threads = []
    print('START RACE!!!!')
    
    for i in range(num_runners):    # Create and start threads
        t = Thread(target=runner)
        threads.append(t)
        t.start()
    
    for thread in threads:     # Wait for all threads to finish
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()




Execution:
   All threads run independently → reach barrier → wait → continue together when all arrive.

End Use:
   Synchronize multiple threads at a checkpoint.

When & How to Use:
   Use when multiple threads must complete Phase 1 before starting Phase 2.

Advantages:
   Easy synchronization
   Ensures coordination
Disadvantages:
   If one thread fails → others stuck
   Fixed number of threads required
 

2) condition.py
Topic:
   Condition Variable (Producer-Consumer)

import logging
import threading
import time
logging.basicConfig(level=logging.INFO)# Logging format
items = []
condition = threading.Condition()
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def consume(self):
        with condition:
            while len(items) == 0:
                logging.info('No items to consume')
                condition.wait()
            
            items.pop()
            logging.info('Consumed 1 item')
            
            condition.notify()
    
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def produce(self):
        with condition:
            while len(items) == 10:
                logging.info('Items full. Waiting...')
                condition.wait()
            
            items.append(1)
            logging.info(f'Total items {len(items)}')
            
            condition.notify()
    
    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()

def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()

Execution:
   Producer adds items → Consumer removes → wait/notify used for synchronization.

End Use:
   Control access to shared resources.

When & How to Use:
   When multiple threads need coordinated access to shared data.

Advantages:
   Fine-grained control
   Efficient waiting

Disadvantages:
   Complex logic
   Risk of deadlock



3) event.py
Topic:
   Event Signaling

import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO)

items = []
event = threading.Event()

class Consumer(threading.Thread):
    def run(self):
        while True:
            event.wait()  # Wait for signal
            item = items.pop()
            logging.info(f'Consumer received {item}')
            event.clear()  # Reset event

class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info(f'Produced {item}')
            event.set()  # Signal consumer

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


Execution:
   Producer sets event → Consumer waits → executes when signaled.

End Use:
   Signal-based communication.

When to Use:
   When one thread must wait for another’s signal.

Advantages:
   Simple
   Easy signaling

Disadvantages:
   No built-in data protection
   Must manage clearing carefully



4) myThreadclass.py
Topic:
   Basic Thread Class

Execution:
   Creates 9 threads → each sleeps random time → runs parallel.

End Use:
   Parallel task execution.

When to Use:
   Independent background tasks.

Advantages:
   Faster execution (for I/O tasks)
   Simple structure

Disadvantages:
   No synchronization
   Race conditions possible


5) Lock Version
Topic:
   Lock (Mutual Exclusion)

Execution:
   Only one thread runs critical section at a time.

End Use:
   Protect shared data.

When to Use:
   Whenever shared variable is modified.

Advantages:
   Prevents race condition

Disadvantages:
   Slower
   Deadlock possible


6) Lock2 Version
Topic:
   Partial Locking

Execution:
   Lock only protects print → sleep runs in parallel.

End Use:
   Optimize performance.

Advantages:
   Better concurrency

Disadvantages:
   Unsafe if shared data exists


7) RLock.py
Topic:
   Reentrant Lock (RLock)

Execution:
   Same thread can acquire lock multiple times.

End Use:
   Nested locking.

When to Use:
   When one locked method calls another locked method.

Advantages:
   Prevents self-deadlock

Disadvantages:
   Slight overhead


8) Semaphore.py
Topic:
   Semaphore

Execution:
   Consumer waits (acquire) → Producer releases.

End Use:
   Limit access to resource.

When to Use:
   Connection pools, limited resources.

Advantages:
   Controls multiple threads

Disadvantages:
   Complex debugging


9) Thread_defination.py
Topic:
   Basic Thread Function

Execution:
   Thread created → start → immediate join → sequential.

Disadvantage:
   No true parallelism due to immediate join.


10) Thread_determine.py
Topic:
   Thread Naming

End Use:
   Debugging and monitoring threads.


11) Thread_name_and_class_processes.py
Topic:
   Custom Thread Class

End Use:
   Structured thread design in OOP.

12) Threading_with_queue.py
Topic:
   Queue (Thread-safe communication)

Execution:
   Producer → queue.put()
   Consumer → queue.get()

End Use:
   Safe producer-consumer implementation.

When to Use:
   Task scheduling systems.

Advantages:
   No manual lock needed
   Safe

Disadvantages:
   Slight overhead
