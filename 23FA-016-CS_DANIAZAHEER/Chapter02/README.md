 ## 1. Thread_definition.py

**Topic:** Thread Creation and Execution

**What is happening?**
The program demonstrates how to create and run threads using Python’s threading module. A function `my_func` is defined, which prints the thread number. In the main function, a loop runs 10 times and creates a new thread in each iteration. Each thread executes the function with a different number.

The `start()` method begins the execution of each thread. However, the `join()` method is called immediately after starting the thread, which makes the program wait for the current thread to finish before starting the next one. As a result, the execution becomes sequential instead of fully parallel.

**How to run:**
python Thread_definition.py

**When to use:**
When learning how threads are created and managed in Python.

**Advantages:**
- Simple and easy way to create threads
- Helps in understanding basic threading concepts
- Useful for dividing tasks into smaller units

**Disadvantages:**
- Using `join()` inside the loop prevents parallel execution
- Threads share memory, which may cause data conflicts
- Python’s GIL limits true parallelism

**End use:**
Used for understanding thread creation and execution. In real applications, threads are used for handling multiple tasks simultaneously, but proper synchronization is required to achieve efficient performance.

## 2. Thread_determine.py

**Topic:** Thread Identification and Execution

**What is happening?**
The program creates three separate threads, each assigned to a different function (function_A, function_B, and function_C). Each function prints a message when the thread starts and when it finishes execution. The thread name is displayed using `threading.currentThread().getName()` to identify which thread is running.

A delay of 2 seconds is added using `time.sleep()` to simulate work being done by each thread. All threads are started using the `start()` method, allowing them to run concurrently. The `join()` method is then used to ensure that the main program waits for all threads to complete before exiting.

**How to run:**
python Thread_determine.py

**When to use:**
When you need to identify and track multiple threads during execution.

**Advantages:**
- Helps in understanding how multiple threads run simultaneously
- Thread names make it easier to track execution
- Demonstrates concurrent execution of tasks

**Disadvantages:**
- Threads share memory, which may lead to data conflicts
- Debugging can be difficult with multiple threads
- Python’s GIL limits true parallel execution

**End use:**
Used for monitoring and managing multiple threads in a program. It is helpful in applications where tracking thread activity is important, such as logging, debugging, and concurrent task handling.

## 3. Thread_name_and_processes.py

**Topic:** Thread Creation using Class (Custom Thread)

**What is happening?**
The program demonstrates how to create threads by extending the `Thread` class. A custom class `MyThreadClass` is defined, which inherits from the `Thread` class. Each thread is given a name during initialization.

The `run()` method is overridden to define the task that each thread will perform. When the thread starts, it executes the `run()` method and prints the name of the thread.

In the main function, two thread objects are created and started. The `join()` method is used to ensure that both threads complete their execution before the program prints "End".

**How to run:**
python Thread_name_and_processes.py

**When to use:**
When you want more control over thread behavior by creating custom thread classes.

**Advantages:**
- Provides better structure and organization using classes
- Easy to manage complex thread behavior
- Allows customization of thread functionality

**Disadvantages:**
- Slightly more complex than simple thread creation
- Requires understanding of object-oriented programming
- Debugging can be harder with multiple threads

**End use:**
Used in applications where threads need to perform structured or complex tasks. It is helpful when building scalable and organized multithreaded programs.

## 4. MyThreadClass.py

**Topic:** Multiple Threads using Class with Execution Time

**What is happening?**
The program creates multiple threads by extending the `Thread` class. Each thread is given a name and a random duration using `randint()`. The `run()` method prints the thread name along with the process ID and then pauses execution for a random time using `time.sleep()` to simulate work.

In the main function, nine threads are created and started. All threads run concurrently and complete at different times depending on their assigned duration. The `join()` method ensures that the main program waits for all threads to finish before printing "End".

The total execution time is calculated using `time.time()` to show how long the program takes to complete.

**How to run:**
python MyThreadClass.py

**When to use:**
When executing multiple independent tasks concurrently and measuring overall execution time.

**Advantages:**
- Demonstrates concurrent execution of multiple threads
- Shows how to assign different workloads to threads
- Helps in measuring execution time of parallel tasks

**Disadvantages:**
- Threads share memory, which may lead to conflicts
- Execution order is unpredictable
- Python’s GIL limits true parallelism

**End use:**
Used in applications where multiple tasks need to run at the same time, such as simulations, background processing, and performance testing.

## 5. MyThreadClass_lock.py

**Topic:** Thread Synchronization using Lock

**What is happening?**
The program demonstrates the use of a lock to control access to shared resources in a multithreaded environment. A global lock `threadLock` is created using `threading.Lock()`.

Multiple threads are created using a custom class that extends the `Thread` class. In the `run()` method, each thread first acquires the lock using `threadLock.acquire()` before executing its task. This ensures that only one thread runs the critical section at a time.

After completing its task (printing and sleeping for a random duration), the thread releases the lock using `threadLock.release()`. This allows the next thread to acquire the lock and execute.

Although multiple threads are created, the use of a lock forces them to run one at a time, preventing overlapping execution in the critical section.

**How to run:**
python MyThreadClass_lock.py

**When to use:**
When multiple threads need to access shared resources and synchronization is required to avoid conflicts.

**Advantages:**
- Prevents race conditions
- Ensures safe access to shared data
- Maintains data consistency

**Disadvantages:**
- Reduces parallel performance due to sequential execution
- Improper use can lead to deadlocks
- Adds complexity to the program

**End use:**
Used in multithreaded applications where shared resources must be accessed safely, such as file handling, database operations, and critical data processing.

## 6. MyThreadClass_lock_2.py

**Topic:** Optimized Lock Usage in Threads

**What is happening?**
The program demonstrates a more efficient use of locks in multithreading. A global lock `threadLock` is created to control access to a shared section of code.

Each thread acquires the lock before printing its starting message and immediately releases it afterward. This ensures that only the print statement is protected, while the rest of the thread's execution runs independently.

After releasing the lock, the thread sleeps for a random duration and then prints its completion message without holding the lock. This allows other threads to run in parallel while only the critical section (printing) remains synchronized.

Compared to the previous version, this approach improves concurrency by minimizing the time a lock is held.

**How to run:**
python MyThreadClass_lock_2.py

**When to use:**
When only a small part of the code needs synchronization, and the rest can safely run in parallel.

**Advantages:**
- Improves performance by reducing lock usage time
- Allows better parallel execution of threads
- Prevents unnecessary blocking of threads

**Disadvantages:**
- Still requires careful identification of critical sections
- Incorrect usage may lead to inconsistent results
- Slightly more complex than basic locking

**End use:**
Used in multithreaded applications where only specific operations need protection, allowing the rest of the program to execute concurrently for better performance.

## 7. Rlock.py

**Topic:** Reentrant Lock (RLock)

**What is happening?**
The program demonstrates the use of a reentrant lock (`RLock`) to manage shared resources safely in a multithreaded environment. A class `Box` is created, which maintains a shared variable `total_items`.

The methods `add()` and `remove()` modify this shared value by calling another method `execute()`. All these methods use the same lock. Since `add()` and `remove()` internally call `execute()`, the same thread needs to acquire the lock multiple times.

This is made possible using `RLock`, which allows a thread to acquire the same lock more than once without causing a deadlock. Two threads are created: one adds items to the box, and the other removes items. Both threads run concurrently while safely updating the shared value.

**How to run:**
python Rlock.py

**When to use:**
When a thread needs to acquire the same lock multiple times, especially in nested function calls.

**Advantages:**
- Prevents deadlock when the same thread reuses the lock
- Ensures safe access to shared resources
- Useful in complex, nested locking situations

**Disadvantages:**
- Slightly slower than a regular lock
- More complex to understand and implement
- Misuse can still lead to logical errors

**End use:**
Used in multithreaded applications where functions call other functions that also require locking. It ensures safe and flexible synchronization in nested operations.

## 8. Semaphore.py

**Topic:** Thread Synchronization using Semaphore (Producer-Consumer)

**What is happening?**
The program demonstrates synchronization between threads using a semaphore. A global variable `item` is shared between two threads: producer and consumer.

The consumer thread waits for a signal by calling `semaphore.acquire()`. Initially, the semaphore value is 0, so the consumer blocks and waits. The producer thread generates a random item after a delay and then calls `semaphore.release()`, which increases the semaphore value and allows the consumer to proceed.

Once released, the consumer continues execution and prints the item. This process repeats multiple times in a loop, showing coordination between producer and consumer threads.

**How to run:**
python Semaphore.py

**When to use:**
When controlling access between threads, especially in producer-consumer problems.

**Advantages:**
- Efficient synchronization between threads
- Prevents race conditions
- Allows controlled access to shared resources

**Disadvantages:**
- Can be difficult to debug
- Incorrect use may lead to deadlocks
- Requires careful management of acquire and release

**End use:**
Used in real-world applications like task queues, resource management, and communication between threads where one thread produces data and another consumes it.

## 9. Condition.py

**Topic:** Thread Synchronization using Condition Variable

**What is happening?**
The program demonstrates synchronization between producer and consumer threads using a condition variable. A shared list `items` is used to store produced items.

The producer thread adds items to the list, while the consumer thread removes them. A `Condition` object is used to manage coordination between threads.

If the list is empty, the consumer waits using `condition.wait()` until the producer adds an item. Similarly, if the list reaches a limit (10 items), the producer waits until the consumer removes an item.

The `notify()` method is used to wake up the waiting thread after an item is added or removed. This ensures proper communication and coordination between producer and consumer threads.

**How to run:**
python Condition.py

**When to use:**
When threads need to wait for a specific condition before continuing execution.

**Advantages:**
- Provides better control compared to basic locks
- Efficient communication between threads
- Useful for managing shared resources with conditions

**Disadvantages:**
- More complex to implement and understand
- Incorrect use can lead to deadlocks or missed signals
- Requires careful handling of wait and notify

**End use:**
Used in applications like task scheduling, resource pooling, and producer-consumer systems where threads must coordinate based on certain conditions.

## 10. Event.py

**Topic:** Thread Synchronization using Event

**What is happening?**
The program demonstrates synchronization between threads using an event object. A shared list `items` is used where the producer adds items and the consumer removes them.

The consumer thread continuously waits for a signal using `event.wait()`. It remains blocked until the event is set. The producer thread generates random items, appends them to the list, and signals the consumer by calling `event.set()`.

After signaling, the event is cleared using `event.clear()` so that the consumer waits again for the next signal. This process continues for a fixed number of iterations, allowing controlled communication between producer and consumer.

**How to run:**
python Event.py

**When to use:**
When one thread needs to wait for a signal from another thread before continuing execution.

**Advantages:**
- Simple and easy signaling mechanism
- Useful for one-way communication between threads
- Reduces unnecessary checking or polling

**Disadvantages:**
- Less flexible compared to condition variables
- Needs careful handling of set and clear operations
- Can miss signals if not used properly

**End use:**
Used in applications where threads need to wait for an event or signal, such as task triggering, notifications, and simple coordination between threads.

## 11. Barrier.py

**Topic:** Thread Synchronization using Barrier

**What is happening?**
The program demonstrates the use of a barrier to synchronize multiple threads. A barrier is created for a fixed number of threads (`num_runners = 3`), meaning all threads must reach a certain point before any of them can continue.

Each thread represents a runner. After a random delay, each runner reaches the barrier and prints a message with the current time. The `finish_line.wait()` call makes each thread wait at the barrier until all threads have arrived.

Once all threads reach the barrier, they are released together and the program continues execution. This ensures that no thread proceeds beyond the barrier until all have completed the initial phase.

**How to run:**
python Barrier.py

**When to use:**
When multiple threads need to wait for each other before continuing execution.

**Advantages:**
- Ensures synchronization at a specific point
- Useful for coordinating multiple threads
- Simple way to manage group execution

**Disadvantages:**
- All threads must reach the barrier, otherwise program may hang
- Not suitable for dynamic number of threads
- Limited flexibility compared to other synchronization methods

**End use:**
Used in scenarios like simulations, parallel tasks, and workflows where all threads must complete a phase before moving to the next step.

## 12. Threading_with_queue.py

**Topic:** Thread Synchronization using Queue

**What is happening?**
The program demonstrates synchronization between threads using a queue. A `Queue` is used as a shared data structure between producer and consumer threads.

The producer thread generates random items and adds them to the queue using `put()`. Multiple consumer threads continuously retrieve items from the queue using `get()` and process them.

The queue automatically handles synchronization, ensuring that only one thread accesses an item at a time. The `task_done()` method is used by consumers to indicate that a task has been completed.

This approach avoids the need for manual locks and provides a safe and efficient way to manage communication between threads.

**How to run:**
python Threading_with_queue.py

**When to use:**
When multiple threads need to safely share and process data without manually handling locks.

**Advantages:**
- Built-in thread safety (no need for explicit locks)
- Efficient communication between producer and consumer
- Easy to implement and manage

**Disadvantages:**
- Less control compared to manual synchronization
- Consumers may run indefinitely if not controlled
- Slight overhead due to queue management

**End use:**
Used in real-world applications like task queues, job scheduling systems, and data processing pipelines where multiple threads work on shared tasks.


