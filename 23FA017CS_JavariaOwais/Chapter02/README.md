**************************************************************************************************
**Chapter: 02       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## MyThreadClass 
**Note: As we have already discussed threading in chapter #1 in detail, so lets jump towards the code here** 

### Code Interpretation
*Importing Modules*
- threading => for creating and managing threads
- time => for simulating delays and measuring performance
- os => to get the current process ID
- random.randint => to assign random durations for thread execution

*Thread Class Definition*
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        *Executes when thread starts*
        print(f"{self.name} running, process ID: {os.getpid()}")
        time.sleep(self.duration)
        print(f"{self.name} over")
* Thread.__init__(self) initializes the thread.
* run() contains the code executed by the thread.

*Main Execution Block*
if __name__ == "__main__":

*Creating Threads*
thread1 = MyThreadClass("Thread#1", randint(1,10))
- Defines a thread object.
- Assigns a task (run method) to execute.
- Random duration simulates work done by the thread.

*Starting Threads*
thread1.start()
- Begins execution of the thread.
- Threads run concurrently with other threads.

*Thread Synchronization*
thread1.join()
- Ensures the main program waits until all threads complete.
- Prevents the program from finishing before threads are done.

*Performance Measurement*
start_time = time.time()
end_time = time.time()
**(end_time - start_time)**
- Measures total execution time for all threads.

### Advantages of Threading
- Efficient for I/O-bound tasks (file reading/writing).
- Allows concurrent execution within a single process.
- Less memory overhead than multiprocessing (threads share memory).

### Limitations
- Global Interpreter Lock (GIL) prevents true parallel execution of CPU-bound tasks.
- Thread synchronization can be complex (e.g., race conditions, deadlocks).
- Errors in one thread can affect the entire process.

**************************************************************************************************

## Thread Synchronization using Lock in Python
This program demonstrates how to control concurrent thread execution using a Lock to avoid race conditions and ensure safe access to shared resources.

### Thread Lock (Mutex)
A Lock is a synchronization primitive from the `threading` module that ensures only **one thread executes a critical section at a time**.
- Prevents **race conditions**
- Ensures **mutual exclusion**
- Forces threads to execute sequentially inside the critical section

### Code Interpretation
*Importing Modules*
- threading => for creating and managing threads
- time => for simulating delays and measuring performance
- os => to get the current process ID
- random.randint => to assign random durations for thread execution 

*Lock Creation*
threadLock = threading.Lock()
- Creates a global lock object
- Shared among all threads
- Only one thread can hold it at a time

*Thread Class*
class MyThreadClass(Thread):
- Custom thread class inheriting from Thread

*Critical Section*
threadLock.acquire()
- Acquires the lock
- Blocks other threads from entering this section

print("---> " + self.name + " running...")
time.sleep(self.duration)
print("---> " + self.name + " over")
- Code inside lock = critical section
- Only one thread executes this at a time

threadLock.release()
- Releases the lock
- Allows next waiting thread to proceed

*Thread Creation*
thread1 = MyThreadClass("Thread#1", randint(1,10))
- Creates thread with random execution time

*Starting Threads*
thread1.start()
- Begins execution of thread
- Calls the run() method internally

*Thread Synchronization*
thread1.join()
- Ensures main program waits for all threads to complete

*Execution Time Measurement*
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
- Measures total runtime
- Due to lock, execution time = sum of all thread durations

*Key Observation*
- Even though multiple threads are started, output will appear sequentially and NOT parallel, because lock forces threads to execute one-by-one.

### Advantages of Using Lock
- Prevents race conditions
- Ensures data consistency
- Simple synchronization mechanism

### Limitations
- Reduces concurrency (threads wait → slower execution)
- Risk of deadlock if not handled properly
- Poor performance if overused


## ThreadLock2 (Optimized Synchronization)
This version demonstrates **partial (fine-grained) locking**, where the lock is applied only to a small critical section instead of the entire thread execution.
Instead of locking the whole `run()` method, only the **necessary part** is protected.

threadLock.acquire() 
print("---> " + self.name + " running...")  // Critical Section
threadLock.release()

time.sleep(self.duration)   // Enables parallel execution
print("---> " + self.name + " over")    // threads will finish randomly

### Output Difference
// Version 1
Thread#1 running
Thread#1 over
Thread#2 running
Thread#2 over
...
// sequential order

// Versiom 2
Thread#1 running
Thread#2 running
Thread#3 running
...
Thread#2 over
Thread#5 over
Thread#1 over
...
// Parallel execution, no order

### Performance Insight
// Versiom 1
Total time = sum of all thread durations
// Versiom 2
Total time = maximum thread duration

### Conclusion
ThreadLock2 represents a better real-world design approach where locking is minimized to improve performance. 

**************************************************************************************************

## Semaphores 
A Semaphore controls access to shared resources by multiple threads using a counter-based mechanism.This program demonstrates the use of a Semaphore for synchronizing threads using the `Producer-Consumer model`. 

### Semaphore in Python
A Semaphore is a synchronization primitive in Python (from the threading module) used to manage access to shared resources.
- It maintains an internal **counter**
- Threads **decrement (acquire)** the counter to access a resource
- Threads **increment (release)** the counter to signal availability

### Types of Semaphores
* Counting Semaphore: Allows multiple threads to access a resource. Its counter can be greater than 1.
* Binary Semaphore: Counter is either **0 or 1**, similar to lock(mutex).

### Working
acquire() - Decreases counter by 1. If counter = 0 -> thread waits 
release() - Increases counter by 1 -> signals waiting threads 

### Producer-Consumer Model
- **Producer** generates data (item)
- **Consumer** waits and consumes data
- **Semaphore** ensures consumer waits until producer produces

### Code Interpretation
*Importing Modules*
- logging => for formatted thread output  
- threading => for threads and semaphore  
- time => to simulate delay  
- random => to generate random item  

*Logging Configuration*
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
- It displays timestamp, thread name, log level and the message

*Semaphore Initialization*
semaphore = threading.Semaphore(0)
- value = 0 means consumer cannot proceed initially and waits until producer signals

item = 0
- Global variable shared between producer and consumer

*Consumer Function*
def consumer():
    logging.info('Consumer is waiting')
    semaphore.acquire()
    logging.info('Consumer notify: item number {}'.format(item))

- Consumer starts and waits
acquire():
- If semaphore = 0 => blocks (waits)
- After producer releases => consumer resumes and prints consumed item

*Producer Function*
def producer():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Producer notify: item number {}'.format(item))
    semaphore.release()

- Sleeps for 3 seconds (simulating production delay)
- Generates random item
- Logs produced value
release():
- Increments semaphore to signal waiting consumer

*Thread Creation for both consumer and producer*
t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

*Thread Execution*
t1.start()
t2.start()
- Both threads start concurrently

*Synchronization*
t1.join()
t2.join()
- Ensures both threads complete before next iteration
Loop Execution

for i in range(10):
- Runs producer-consumer cycle 10 times

*Output Behavior*
2026-04-03 23:30:52,427 Thread-1 (consumer) INFO     Consumer is waiting
2026-04-03 23:30:55,430 Thread-2 (producer) INFO     Producer notify: item number 199
2026-04-03 23:30:55,431 Thread-1 (consumer) INFO     Consumer notify: item number 199

### Advantages of Semaphore
- Controls access to shared resources
- Prevents race conditions
- Supports multiple thread synchronization
- More flexible than locks

### Limitations
- Complex to debug
- Risk of deadlocks if misused
- Improper release/acquire can cause issues
- Harder to understand compared to locks

**************************************************************************************************

## Barrier Synchronization 
A **Barrier** is a synchronization mechanism provided by the `threading` module. It forces threads to wait until a specified number of threads have reached a certain point before continuing execution.

### Main Concept
- Threads execute independently  
- All threads must reach the barrier  
- Once all arrive, they proceed together  

### Code Interpretation
*Importing Modules*
- randrange => generates random delay
- Barrier => synchronization mechanism
- Thread => thread creation
- ctime() => current time
- sleep() => delay execution

*Global Variables*
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']
- num_runners = total number of threads
- Barrier(num_runners) = barrier waits for 3 threads
- runners = list of thread names

*Runner Function*
def runner():
    name = runners.pop()
- Each thread picks a unique name using pop()

*Simulating Execution Time*
sleep(randrange(2, 5))
- Each thread sleeps randomly b/w 2–4 seconds
- Simulates different execution speeds

*Upon Reaching the Barrier*
print('%s reached the barrier at: %s \n' % (name, ctime()))
- Displays when each thread reaches the barrier

*Barrier Synchronization*
finish_line.wait()
- Thread pauses here and waits until all threads reach this line
- Once all arrive, they continue together

*Thread Creation*
threads.append(Thread(target=runner))
- Creates a thread for each runner

*Starting Threads*
threads[-1].start()
- Starts execution of each thread

*Thread Joining*
for thread in threads:
    thread.join()
- Ensures main program waits for all threads

*Program Start & End*
print('START RACE!!!!')
print('Race over!')
- Shows beginning and end of execution

*Program Flow*
- Race starts
- Threads (runners) are created and started
- Each thread sleeps for a random time
- Each prints arrival time
- Each waits at finish_line.wait()
- Once all threads reach, barrier releases all
- Program ends

*Output Behavior*
START RACE!!!!
Louie reached the barrier at: Sat Apr  4 13:30:54 2026 

Dewey reached the barrier at: Sat Apr  4 13:30:55 2026 

Huey reached the barrier at: Sat Apr  4 13:30:56 2026 

Race over!

### Advantages of Barrier
- Ensures coordinated execution
- Useful in parallel tasks requiring checkpoints
- Simple and effective synchronization

### Limitations
- All threads must reach the barrier can result to delays
- Risk of deadlock if a thread never arrives
- Not suitable for dynamic number of threads

**************************************************************************************************

## Condition Synchronization (Producer–Consumer Problem)
A Condition is a synchronization mechanism in Python provided by the `threading` module. It allows threads to **wait until a certain condition is met** and enables communication between threads using `wait()` and `notify()`.

### Main Concept
- Threads share a common resource (list)  
- Consumer waits if no items are available  
- Producer waits if the list is full  
- Threads communicate using `wait()` and `notify()`  

### Code Interpretation

*Importing Modules*
- logging => structured output with thread info  
- threading => threads and condition variable  
- time => delay execution  

*Logging Configuration*
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
- Displays time, thread name, level, and message

*Global Variables*
items = []  **shared list (acts like a buffer)**
condition = threading.Condition()   **controls access and synchronization**

*with condition:*
- This means lock is automatically acquired and only one thread enters at a time. It also gives safe access to shared data (items).

*Consumer Class*
class Consumer(threading.Thread):
- Defines a consumer thread

if len(items) == 0:
    logging.info('no items to consume')
    condition.wait()
- If list is empty, consumer waits
- Releases lock and sleeps until notified

items.pop()
logging.info('consumed 1 item')
- Removes one item from list

condition.notify()
- Notifies producer to continue

for i in range(20):
    time.sleep(2)
    self.consume()
- Runs 20 times
- Slower execution (2 sec delay)

*Producer Class*
class Producer(threading.Thread):
- Defines a producer thread

if len(items) == 10:
    logging.info('items produced {}. Stopped'.format(len(items)))
    condition.wait()
- If list is full (here full = 10 items) then producer waits

items.append(1)
logging.info('total items {}'.format(len(items)))
- Adds item to list

condition.notify()
- Notifies consumer to consume

for i in range(20):
    time.sleep(0.5)
    self.produce()
- Runs 20 times
- Faster execution (0.5 sec delay)

*Thread Creation*
producer = Producer(name='Producer')
consumer = Consumer(name='Consumer')

*Starting Threads*
producer.start()
consumer.start()

*Thread Joining*
producer.join()
consumer.join()
- Ensures main program waits for both threads

*Program Flow*
- Consumer starts and find list empty. It waits until producer produces
- Producer starts and produces item
- Producer calls notify() to wake consumer
- Consumer consumes item and notifies producer
- If list becomes full, producer waits
- If list becomes empty, consumer waits

*Output Behavior*
2026-04-04 20:27:09,473 Producer          INFO     total items 1
2026-04-04 20:27:09,976 Producer          INFO     total items 2
2026-04-04 20:27:10,974 Consumer          INFO     consumed 1 item
...
2026-04-04 20:27:15,493 Producer          INFO     total items 10
2026-04-04 20:27:15,995 Producer          INFO     items produced 10. Stopped
...

### Advantages
- Enables communication between threads
- Efficient synchronization (wait only when needed)

### Limitations
- Complex compared to locks
- Risk of deadlocks if condition doesnot meet
- Requires careful handling of wait() and notify()

**************************************************************************************************

## Reentrant Lock (RLock) in Python
Rlock is a synchronization mechanism provided by the `threading` module that allows the same thread to acquire the same lock **multiple times** without causing a deadlock.

### Main Concept
- Multiple threads access a shared resource (total_items)  
- Lock ensures only one thread modifies data at a time  
- RLock allows **nested locking (lock inside lock)**  
- Prevents race conditions and deadlocks  

### Why Rlock?
- A normal Lock allows only one acquisition per thread  
- If the same thread tries to acquire it again, deadlock occurs 
RLock allows:
- Same thread can aquire lock multiple times  
- Keeps track of how many times lock is acquired  

### Code Interpretation
*Importing Modules*
- 'threading' for threads and locks  
- 'time' to simulate delay  
- 'random' to generate random number of operations  

*Box Class (Shared Resource)*
class Box:
- Represents a shared container

*Initialization*
self.lock = threading.RLock()
self.total_items = 0
- RLock() allows nested locking
- total_items is a shared variable

*Core Function*
def execute(self, value):
    with self.lock:
        self.total_items += value
- Updates shared variable
- +1 means add item
- -1 means remove item

*Add Method*
def add(self):
    with self.lock:
        self.execute(1)
- Acquires lock
- Calls another function that also acquires lock

*Remove Method*
def remove(self):
    with self.lock:
        self.execute(-1)
- Its similar to add, but removes item
 
*Nested Locking*
add() => acquires lock  
    execute() => acquires same lock again
- This works ONLY because of RLock

*Adder Thread*
def adder(box, items):
- Adds items one by one
while items:
    box.add()
    time.sleep(1)
    items -= 1
- Runs until all items are added
- Simulates delay also

*Remover Thread*
def remover(box, items):
- Removes items one by one
while items:
    box.remove()
    time.sleep(1)
    items -= 1

*Thread Creation*
t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
t2 = threading.Thread(target=remover, args=(box, random.randint(1,10)))
- adder = adds random 10–20 items
- remover = removes random 1–10 items

*Starting Threads*
t1.start()
t2.start()
- Both threads execute concurrently

*Thread Joining*
t1.join()
t2.join()
- Main thread waits for both threads

*Program Flow*
- Shared box is created
- Adder thread starts adding items
- Remover thread starts removing items
- Both access same variable (total_items)
- RLock ensures safe access
- Nested locking occurs inside methods
- Program ends after both threads finish

*Output Behavior*
N° 20 items to ADD
N° 1 items to REMOVE

ADDED one item -->19 item to ADD
REMOVED one item -->0 item to REMOVE
...

### Advantages of RLock
- Prevents deadlock in nested locking
- Ensures thread-safe operations and maintains data consistency
- Allows complex function calls with shared locks

### Limitations
- Its slightly slower than normal lock which can affect performance
- More complex to understand

**************************************************************************************************

## Event Synchronization 
An Event is a synchronization mechanism provided by the `threading` module. It is used for communication between threads using a signaling mechanism.

### Main Concept
- Event acts like a signal (flag)  
- Threads wait for the signal to proceed  
- Producer sets the signal  
- Consumer waits and responds  

### Code Interpretation
*Importing Modules*
- logging => structured output with thread info  
- threading => threads and event mechanism  
- time => delay execution  
- random => generate random values  

*Global Variables*
items = []  **shared list**
event = threading.Event()   **signaling object**

*Consumer Thread*
class Consumer(threading.Thread):
- Defines consumer thread  

while True:
    time.sleep(2)
    event.wait()
- Runs continuously  
- Waits until event is set  

*Consuming Item*
item = items.pop()
- Removes item from the list  

*Logging*
logging.info('Consumer notify: {} popped by {}'.format(item, self.name))
- logs a message with the details

*Producer Thread*
class Producer(threading.Thread):
- Defines producer thread  

for i in range(5):
    time.sleep(2)
- Produces limited items  

*Producing Item*
item = random.randint(0, 100)
items.append(item)

*Logging*
logging.info('Producer notify: item {} appended by {}'.format(item, self.name))

*Event Signaling*
event.set()
- Sends signal to waiting threads  

event.clear()
- Resets signal so consumer waits again until the producer produces 

*Thread Creation*
t1 = Producer()
t2 = Consumer()

*Starting Threads*
t1.start()
t2.start()

*Thread Joining*
t1.join()
t2.join()
- Main waits for threads  

*Program Flow*
- Consumer starts and waits  
- Producer creates item  
- Producer signals using event.set()  
- Consumer wakes and consumes item  
- Event is cleared  
- Process repeats  

*Output Behavior*
2026-04-05 14:34:28,685 Thread-1          INFO     Producer notify: item 80 appended by Thread-1
2026-04-05 14:34:28,686 Thread-2          INFO     Consumer notify: 80 popped by Thread-2
...

### Advantages of Event
- Simple thread communication  
- Efficient signaling mechanism  
- Easy to implement  

### Limitations
- No data protection (no lock)  
- Risk of race conditions  
- Not suitable for complex synchronization  

**************************************************************************************************

## Thread Synchronization using Queue 
A **Queue** is a thread-safe data structure provided by Python (`queue.Queue`). It is used for synchronization between threads and automatically handles locking and coordination.

### Main Concept
- Producer adds items to queue  
- Consumer removes items from queue  
- Queue handles synchronization automatically  
- No need for locks or condition variables  

### Code Interpretation
*Importing Modules*
- threading.Thread => for thread creation  
- queue.Queue => thread-safe queue  
- time => delay execution  
- random => generate random items  

*Queue Initialization*
queue = Queue()
- Shared resource between threads  
- Automatically thread-safe  

*Producer Class*
class Producer(Thread):
- Produces items and adds to queue  

for i in range(5):
- Produces 5 items  

self.queue.put(item)
- Safely inserts item into queue  

time.sleep(1)
- Simulates delay  

*Consumer Class*
class Consumer(Thread):
- Consumes items from queue  

while True:
- Runs continuously  

item = self.queue.get()
- Removes item from queue  
- Waits automatically if queue is empty  

self.queue.task_done()
- Marks task as completed  

*Thread Creation*
t1 = Producer(queue)
t2 = Consumer(queue)
t3 = Consumer(queue)
t4 = Consumer(queue)
- 1 producer, 3 consumers  

*Starting Threads*
t1.start()
t2.start()
t3.start()
t4.start()

*Thread Joining*
t1.join()
t2.join()
t3.join()
t4.join()
- Main waits for threads  

*Program Flow*
- Producer generates item  
- Adds item to queue  
- Consumer retrieves item  
- Processes item  
- Marks task done  
- Process repeats  

*Output Behavior*
Producer notify : item N°53 appended to queue by Thread-1

Consumer notify : 53 popped from queue by Thread-2
Producer notify : item N°224 appended to queue by Thread-1 
...

### Advantages of Queue
- Built-in thread safety  
- No need for manual synchronization  
- Automatically handles waiting  
- Easy to implement  

### Limitations
- Less control compared to locks  
- Consumers run infinitely if not handled  
- Not suitable for complex synchronization logic  

**************************************************************************************************