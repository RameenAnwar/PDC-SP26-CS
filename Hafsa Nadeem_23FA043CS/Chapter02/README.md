1. What We Learned:

Threads & Concurrency: How to run multiple tasks at the same time using Python threading.
Thread Synchronization: Using Lock, RLock, Semaphore, Barrier, Condition, Event to control shared data safely.
Queues: Communicating between threads safely using Queue.
Classes & Objects in Threads: Creating threads by extending Thread class.
File Execution Flow: How threads execute, wait, and notify each other.


2. How Code Runs:


Serial (No Threads): One task at a time. Simple but slow.
Threading: Tasks run simultaneously in the same program. Good for I/O or waiting tasks.
Synchronization Tools:
Lock → Only one thread accesses shared data at a time.
RLock → Same as lock, but can be acquired multiple times by same thread.
Semaphore → Limits number of threads doing a task.
Barrier → Waits until all threads reach a certain point.
Condition → Thread waits until a condition is met.
Event → One thread signals another to continue.
Queue: Thread-safe way to send data between threads.


3. End Use / When & How to Use:


Threading: Useful for running multiple tasks at once, like downloading files or updating UI.
Locks / RLocks / Semaphores: When multiple threads share data, to avoid conflicts.
Barrier: When threads must wait for each other to reach the same point.
Event / Condition: For coordinating producer-consumer type tasks.
Queue: Best for safe communication between threads.


4. Advantages & Disadvantages:

Threading:

Pros: Runs many tasks at the same time, good for waiting tasks.
Cons: Can’t fully use CPU for heavy calculations because of Python’s GIL.

Lock / RLock:

Pros: Protects data from being changed by multiple threads at once.
Cons: Can make threads wait if one thread is using the data.

Semaphore:

Pros: Limits how many threads can do a task at the same time.
Cons: Threads may have to wait if the limit is reached.

Barrier:

Pros: Makes threads wait until all threads reach the same point.
Cons: Threads wait even if some finish early.

Condition / Event:

Pros: Lets one thread signal another to continue.
Cons: Needs careful coding to avoid mistakes or deadlocks.

Queue:

Pros: Safe way for threads to share data.
Cons: Slightly slower because it manages the queue.