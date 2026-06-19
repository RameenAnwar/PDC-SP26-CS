# Barrier

*Description:*
Demonstrates Python's Barrier — a synchronization tool that makes all threads wait until every thread has reached a certain point before continuing.

*How it Works:*
3 runner threads created, each sleeps for random time (2-5 sec)
Each runner prints when it reaches the barrier
finish_line.wait() holds each thread until all 3 have arrived
Only then all threads proceed together

*Result:*
All 3 runners reach the barrier at different times but none proceeds until all have arrived — simulates a race finish line.

*Advantages:*
Ensures all threads sync at a specific point
Simple to implement
Useful for phased/staged tasks

*Disadvantages:*
All threads must reach barrier — if one fails, others wait forever
Not flexible for dynamic number of threads

*Where to Use:*
Parallel simulations where all parts must complete one phase before next
Game development (all players ready before round starts)
Scientific computing with phased calculations


# Condition

*Description:*
Demonstrates Python's Condition — a synchronization tool used in Producer-Consumer problem where one thread produces data and another consumes it in a controlled way.

*How it Works:*
Producer adds items to list every 0.5 sec, stops at 10 items and waits
Consumer removes items every 2 sec, waits if list is empty
condition.wait() pauses thread until notified
condition.notify() wakes up the waiting thread

*Result:*
Producer and Consumer run simultaneously but stay synchronized — no overflow or underflow of items list.

*Advantages:*
Prevents race conditions between threads
Efficient — threads wait instead of busy looping
Clean communication between threads

*Disadvantages:*
Complex to implement and debug
Deadlock possible if notify() is never called
Hard to scale with many producers/consumers

*Where to Use:*
Task queues in web servers
Data pipelines (one thread downloads, another processes)
Any producer-consumer scenario in real applications


# Event

*Description:*
Demonstrates Python's Event — a simple thread synchronization tool where one thread signals another to proceed using set/clear mechanism.

*How it Works:*
Producer adds a random item every 2 sec and calls event.set() to signal consumer
Consumer waits with event.wait() until producer signals
event.clear() resets the signal after consumer is notified
Process repeats 5 times

*Result:*
Consumer only acts when Producer signals — no item is consumed before it's produced.

*Advantages:*
Simpler than Condition — easy to implement
Clean signaling between threads
No risk of consuming non-existent items

*Disadvantages:*
Only one signal at a time — not suitable for multiple consumers
event.clear() timing can cause missed signals
Less control compared to Condition

*Where to Use:*
Start/stop signals between threads
Notification systems
When one thread needs to trigger another at a specific moment


# MyThreadClass

*Description:*
Demonstrates creating custom threads by extending Python's Thread class — each thread has a name, duration, and runs concurrently.

*How it Works:*
MyThreadClass inherits from Thread and overrides run()
9 threads created with random sleep duration (1-10 sec)
All threads start together and run concurrently
join() waits for each thread to finish before ending program
Prints process ID and thread name when each starts and ends

*Result:*
All 9 threads run simultaneously, each finishing at different times based on random duration. Total time equals longest thread's duration, not sum of all.

*Advantages:*
Clean OOP approach to threading
Each thread can have custom behavior via run()
Threads run in parallel — saves time

*Disadvantages:*
No thread pool — creating many threads manually is inefficient
Hard to manage if thread count is large
Random duration makes execution unpredictable

*Where to Use:*
Running multiple independent tasks simultaneously
Background tasks in applications
Downloading multiple files at once


# MyThreadClass_lock

*Description:*
Same as MyThreadClass but with a Lock added — ensures only one thread runs at a time, preventing simultaneous access to shared resources.

*How it Works:*
threadLock = threading.Lock() creates a lock
Each thread must acquire() the lock before running
After finishing, thread calls release() to free the lock
Next thread can only start after lock is released
Result: threads run one by one despite being started together

*Result:*
Threads execute sequentially (not in parallel) — total time equals sum of all thread durations, much slower than without lock.

*Advantages:*
Prevents race conditions
Shared data stays safe and consistent
Simple to implement

*Disadvantages:*
Kills parallelism — threads run one by one
Deadlock possible if release() is never called
Slower than no-lock version

*Where to Use:*
Writing to a shared file or database from multiple threads
Updating shared variables safely
Any critical section that must not be accessed simultaneously


# MyThreadClass_lock_2

*Description:*
Improved version of lock — lock is released immediately after printing, so threads sleep in parallel instead of waiting for each other.

*How it Works:*
Lock is acquired only for the print statement (critical section)
Lock is released before time.sleep() — so sleep happens in parallel
Threads still print one at a time but sleep simultaneously
Much faster than MyThreadClass_lock

*Result:*
Threads print sequentially but sleep in parallel — total time is much less than lock version, closer to no-lock version.

*Advantages:*
Protects only the critical section (print)
Threads can still run in parallel for non-critical parts
Best balance between safety and performance

*Disadvantages:*
Easy to forget where to place lock/release correctly
Wrong placement can still cause race conditions or deadlock

*Where to Use:*
When only a specific part of thread needs protection
Logging from multiple threads
Any scenario where critical section is small and short


# Rlock

*Description:*
Demonstrates Python's RLock (Reentrant Lock) — a lock that can be acquired multiple times by the same thread without causing deadlock.

*How it Works:*
Box class has an RLock to protect total_items
add() calls execute(1) — both acquire the same lock (nested)
remove() calls execute(-1) — same nested lock behavior
Two threads run simultaneously — one adds, one removes items
RLock allows same thread to re-acquire lock without blocking itself

*Result:*
Items are added and removed concurrently without deadlock, even though same lock is acquired twice by same thread.

*Advantages:*
Prevents deadlock in nested/recursive lock scenarios
Same thread can acquire lock multiple times safely
Clean with with statement — auto releases lock

*Disadvantages:*
Slower than regular Lock
Can still deadlock if different threads are involved
Overuse can hide poor design

*Where to Use:*
Recursive functions that need locking
When a locked method calls another locked method
Complex class methods that share same lock



# Semaphore

*Description:*
Demonstrates Python's Semaphore — a counter-based synchronization tool where consumer waits until producer signals that an item is ready.

*How it Works:*
Semaphore(0) starts with count 0 — consumer blocks immediately
consumer calls semaphore.acquire() — waits until count > 0
producer waits 3 sec, generates random item, calls semaphore.release() — increments count
Consumer gets notified and reads the item
This repeats 10 times

*Result:*
Consumer always waits for producer to produce an item first — perfectly synchronized, no item is consumed before it's produced.

*Advantages:*
Controls access to limited resources
Can allow multiple threads up to a set limit
Simpler than Condition for basic signaling

*Disadvantages:*
No ownership — any thread can release semaphore
Hard to debug if count goes wrong
Deadlock possible if release() is never called

*Where to Use:*
Limiting simultaneous database connections
Controlling access to limited resources (printers, slots)
Producer-consumer problems


# Thread_definition
*Description:*
Basic demonstration of creating and running threads in Python using threading.Thread with a simple function as target.

*How it Works:*
my_func prints which thread number called it
10 threads created in a loop, each passing its index as argument
Each thread starts with start() and immediately joined with join()
Because join() is inside loop, threads run one by one

*Result:*
Prints thread number 0 to 9 sequentially — not in parallel because join() is called right after each start().

*Advantages:*
Simplest way to create threads in Python
Easy to pass arguments to thread function
Good starting point for learning threading

*Disadvantages:*
join() inside loop makes it sequential — no parallelism
Not efficient for large number of threads
No thread pooling

*Where to Use:*
Basic task automation
Learning threading concepts
Simple sequential background tasks


# Thread_determine

*Description:*
Demonstrates how to name threads and identify them during execution using threading.currentThread().getName().

*How it Works:*
3 functions created — A, B, C — each sleeps for 2 sec
Each thread given a specific name matching its function
All 3 threads start together and run in parallel
getName() prints which thread is currently executing
join() waits for all threads to finish

*Result:*
All 3 threads start simultaneously, print their name on start and exit — total time is 2 sec not 6 sec because they run in parallel.

*Advantages:*
Named threads easy to identify and debug
Parallel execution saves time
currentThread() useful for logging and monitoring

*Disadvantages:*
Manual naming can get confusing with many threads
No return value from threads
Still limited by GIL for CPU-bound tasks

*Where to Use:*
Debugging multi-threaded applications
Running multiple independent functions simultaneously
Logging which thread performed which action



# Thread_name_and_processes

*Description:*
Demonstrates how to assign names to custom threads and identify which process they belong to using os.getpid().

*How it Works:*
MyThreadClass inherits from Thread with a custom name
2 threads created with names "Thread#1" and "Thread#2"
Each thread prints its name and process ID when it runs
Both threads start and run in parallel
join() waits for both to finish

*Result:*
Prints each thread's name along with the process ID they belong to — both threads share the same process ID since threads run within one process.

*Advantages:*
Easy to track which thread belongs to which process
Clean OOP approach to thread naming
Useful for debugging multi-threaded apps

*Disadvantages:*
Very basic — no real task being performed
Manual thread creation doesn't scale well
No error handling

*Where to Use:*
Identifying threads in logs
Debugging process-thread relationships
Learning difference between threads and processes


# Threading_with_queue

*Description:*
Demonstrates thread synchronization using Python's Queue — one producer adds items and multiple consumers take items in a safe, organized way.

*How it Works:*
Producer adds 5 random items to queue, one every second
3 Consumer threads wait and pop items from queue as they arrive
queue.get() blocks consumer until item is available
queue.task_done() signals that item has been processed
Queue handles all synchronization automatically

*Result:*
Items are produced and consumed in order — no race conditions, no manual lock needed because Queue is thread-safe by default.

*Advantages:*
Queue is thread-safe — no need for manual locks
Multiple consumers can work simultaneously
Clean and scalable design

*Disadvantages:*
Consumers run forever (while True) — no clean exit condition
Queue can overflow if producer is faster than consumers
Harder to control execution order

*Where to Use:*
Task queues in web servers
Background job processing
Any pipeline where multiple workers consume shared tasks