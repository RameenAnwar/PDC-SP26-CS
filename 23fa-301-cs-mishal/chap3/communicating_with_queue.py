# IMPORT STATEMENTS COMMENT
# Import multiprocessing to create separate processes that can run concurrently
# and to use Queue() for thread/process-safe data sharing between processes
import multiprocessing

# Import random module to generate random numbers (used by producer to create random items)
import random

# Import time module to add delays/sleep intervals
# This simulates real work and demonstrates concurrent execution
import time

# CLASS: producer
# Purpose: Creates random numbers and puts them into a shared queue
# Inherits from multiprocessing.Process to run as a separate process
class producer(multiprocessing.Process):
    
    # CONSTRUCTOR METHOD - called when producer object is created
    # Parameters: self (the object instance), queue (shared queue between processes)
    def __init__(self, queue):
        # Call the parent class (multiprocessing.Process) constructor
        # This initializes the Process object properly (sets up name, daemon flag, etc.)
        # Without this, the Process wouldn't be properly initialized
        multiprocessing.Process.__init__(self)
        
        # Store the queue as an instance variable (self.queue)
        # This queue is shared between producer and consumer processes
        # .put() adds items, .get() removes items, .qsize() checks size
        self.queue = queue

    # RUN METHOD - executed when .start() is called on the process
    # This method contains the actual work the process will do
    def run(self):
        # Loop 10 times to produce 10 items
        for i in range(10):
            # Generate a random integer between 0 and 256 (inclusive)
            # random.randint(a,b) returns a random number N where a <= N <= b
            item = random.randint(0, 256)
            
            # Put (add) the random item into the shared queue
            # Queue is thread/process-safe - handles locking automatically
            # If queue is full, this would block (but our queue is unbounded)
            self.queue.put(item)
            
            # Print confirmation message showing:
            # - The item value that was added
            # - The name of this process (automatically assigned or custom)
            # %s and %d are format specifiers: %d for integer, %s for string
            print("Process Producer : item %d appended to queue %s"
                  % (item, self.name))
            
            # Sleep for 1 second to simulate work/production delay
            # This allows consumer to catch up and demonstrates concurrency
            # Without this, producer might fill queue too quickly
            time.sleep(1)
            
            # Print the current size (number of items) of the queue
            # .qsize() returns approximate size (may not be exact due to concurrency)
            # %s is used because qsize() returns an integer but we'll format it as string
            print("The size of queue is %s"
                  % self.queue.qsize())

# CLASS: consumer
# Purpose: Takes (consumes) items from the shared queue and processes them
# Inherits from multiprocessing.Process to run as a separate process
class consumer(multiprocessing.Process):
    
    # CONSTRUCTOR METHOD - called when consumer object is created
    # Parameters: self, queue (the same shared queue from producer)
    def __init__(self, queue):
        # Initialize the parent Process class first
        # Essential for proper process setup
        multiprocessing.Process.__init__(self)
        
        # Store the shared queue as an instance variable
        # This queue is the SAME object as in producer (shared memory)
        self.queue = queue

    # RUN METHOD - executed when consumer process starts
    # Continuously consumes items until queue is empty
    def run(self):
        # Infinite loop - keeps checking for items
        while True:
            # Check if the queue is empty
            # .empty() returns True if queue has no items, False otherwise
            # Note: In concurrent environments, this can be unreliable
            # (queue might become non-empty right after checking)
            if (self.queue.empty()):
                # If queue is empty, print message and break out of loop
                # This ends the consumer process
                print("the queue is empty")
                break
            else:
                # Queue has at least one item, so consume it
                # Sleep for 2 seconds BEFORE getting item
                # This simulates processing time/consumer being busy
                # Demonstrates that producer can keep working while consumer sleeps
                time.sleep(2)
                
                # Get (remove and return) an item from the queue
                # FIFO order (First-In-First-Out) - oldest item first
                # If queue is empty, this would block forever (but we checked .empty())
                item = self.queue.get()
                
                # Print consumption message showing:
                # - The item value that was removed
                # - The name of this consumer process
                # Note: Line continuation with backslash (\) allows multi-line string
                print('Process Consumer : item %d popped \
                        from by %s \n'
                      % (item, self.name))
                
                # Sleep for 1 second after processing
                # Simulates post-processing work
                # Total consumer delay: 2 sec before + 1 sec after = 3 sec per item
                time.sleep(1)

# MAIN EXECUTION BLOCK
# This code only runs if script is executed directly (not imported as module)
if __name__ == '__main__':
    
    # Create a Queue object for interprocess communication
    # Queue() is special - it can be shared between processes
    # Uses pipes and locks internally for thread/process safety
    # Items are pickled (serialized) when sent between processes
    queue = multiprocessing.Queue()
    
    # Create producer process object, passing the shared queue
    # At this point, no process has started yet - just object creation
    process_producer = producer(queue)
    
    # Create consumer process object, passing the SAME shared queue
    # Both processes will use this queue to communicate
    process_consumer = consumer(queue)
    
    # Start the producer process
    # This calls the .run() method in a NEW system process
    # Producer begins generating random numbers and putting them in queue
    process_producer.start()
    
    # Start the consumer process
    # This calls the .run() method in ANOTHER new system process
    # Consumer begins checking queue and consuming items
    process_consumer.start()
    
    # Wait for producer process to complete
    # .join() blocks (pauses) the main process until producer finishes
    # Producer finishes after its 10 items are produced (about 10+ seconds)
    # Without join, main process might exit early and kill child processes
    process_producer.join()
    
    # Wait for consumer process to complete
    # Consumer finishes when queue becomes empty
    # This ensures both processes finish before main program ends
    process_consumer.join()
    
    # When both joins complete, program exits
    # At this point, all items are produced and consumed


#This code demonstrates the Producer-Consumer pattern using Python's multiprocessing. Two separate processes work concurrently:

# Producer Process: Generates 10 random numbers (0-256) and adds them to a shared queue

# Consumer Process: Removes numbers from the same queue and "consumes" them (prints them)

# Queue:         	Shared memory buffer that connects producer and consumer
# Producer class:	Creates data and puts it in the queue
# Consumer class:	Takes data from the queue and processes it
# join():       	Makes main program wait for both processes to finish

# Why Use Queue Instead of Pipe?
# Queue is simpler for multiple producers/consumers
# Queue handles synchronization automatically
# Pipe is better for two-way communication between two processes
# Queue uses Pipe internally but adds locking mechanisms


# Main Process (PID: 1000)
#     │
#     ├─ Creates shared Queue (empty initially)
#     │
#     ├─ Creates producer object
#     ├─ Creates consumer object
#     │
#     ├─ producer.start() ────────┐
#     │                          │
#     │                     [NEW PROCESS - Producer]
#     │                     Runs producer.run()
#     │                     For i = 0 to 9:
#     │                         - Generate random number
#     │                         - queue.put(item)
#     │                         - Print "appended"
#     │                         - Sleep 1 sec
#     │                         - Print queue size
#     │
#     ├─ consumer.start() ────────┤
#     │                          │
#     │                     [NEW PROCESS - Consumer]  ←──┐
#     │                     Runs consumer.run()         │
#     │                     While True:                 │
#     │                         - Check queue.empty()   │
#     │                         - Sleep 2 sec          │
#     │                         - queue.get() ←─────────┘
#     │                         - Print "popped"
#     │                         - Sleep 1 sec
#     │
#     ├─ producer.join() (wait for producer to finish)
#     │
#     └─ consumer.join() (wait for consumer to finish)

