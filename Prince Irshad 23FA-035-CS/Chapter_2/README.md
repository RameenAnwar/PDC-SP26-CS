# Chapter 2
# PRINCE IRSHAD (23FA-035-CS)
---

## Table of Contents
* [1. Barrier](#1-barrier)
* [2. Condition](#2-condition)
* [3. Event](#3-event)
* [4. MyThreadClass](#4-mythreadclass)
* [5. MyThreadClass_lock](#5-mythreadclass_lock)
* [6. MyThreadClass_lock_2](#6-mythreadclass_lock_2)
* [7. RLock](#7-rlock)
* [8. Semaphore](#8-semaphore)
* [9. Thread_definition](#9-thread_definition)
* [10. Thread_determine](#10-thread_determine)
* [11. Thread_name_and_processes](#11-thread_name_and_processes)
* [12. Threading_with_queue](#12-threading_with_queue)

---

### 1. Barrier
* **What I Learned:** I learned how to use Python’s threading.Barrier to synchronize multiple threads so that they wait for each other at a specific point before continuing.
* **How it Executes:** A Barrier is initialized with the number of threads that must reach it before any can proceed. Each thread executes a function simulating work. When a thread reaches the barrier, it waits using `finish_line.wait()`. Only when all threads reach the barrier do they continue, synchronizing their actions.
* **End Use:** Useful in programs where multiple threads must reach a checkpoint or complete a step together, like in simulations, multiplayer games, or parallel computations.
* **Short Summary:** Demonstrates how to synchronize multiple threads using a Barrier, ensuring all threads reach a certain checkpoint before any of them continue execution.
* **Pros & Cons:** - **Advantages:** Ensures all threads reach a point before proceeding; useful for synchronizing stages in parallel processing; easy to implement.
  - **Disadvantages:** Threads can be blocked indefinitely if some threads fail to reach the barrier; slightly more complex than simple thread execution; overhead increases if used with many threads frequently.

---

### 2. Condition
* **What I Learned:** I learned how to use Python’s threading.Condition to synchronize producer and consumer threads, allowing threads to wait for a specific condition before proceeding.
* **How it Executes:** A Condition object coordinates access to a shared resource (like a list). The Producer adds items but waits if the list reaches capacity. The Consumer removes items but waits if the list is empty. `condition.wait()` pauses a thread until another thread calls `condition.notify()`, signaling that the state has changed.
* **End Use:** Commonly used in producer-consumer problems, multithreaded applications where threads wait for certain conditions (task queues, resource pools, event-driven systems).
* **Short Summary:** Demonstrates synchronizing producer and consumer threads using a Condition, allowing them to wait and notify each other to ensure safe shared resource access.
* **Pros & Cons:** - **Advantages:** Prevents race conditions; ensures threads only act when a specific condition is met; provides a clear synchronization mechanism.
  - **Disadvantages:** Requires careful management to avoid deadlocks or missed notifications; adds complexity; improper use can lead to threads waiting indefinitely.

---

### 3. Event
* **What I Learned:** I learned how to use Python’s threading.Event to synchronize threads by signaling when an event has occurred, allowing one thread to notify another.
* **How it Executes:** An Event object is used to signal between threads. The Producer generates items, appends them to a shared list, calls `event.set()` to notify the consumer, and then immediately calls `event.clear()` to reset the event. The Consumer waits on `event.wait()` and proceeds to pop the item only when the event is set.
* **End Use:** Useful for signaling, like notifying worker threads that new data is available, coordinating pipelines, or implementing simple triggers.
* **Short Summary:** Using a threading.Event to notify a consumer thread when the producer has added a new item, providing a straightforward signaling mechanism.
* **Pros & Cons:** - **Advantages:** Simple way to notify threads; avoids CPU-heavy busy-waiting; works well for signaling without complex locks.
  - **Disadvantages:** Only signals an occurrence (does not store data); improper setting/clearing can cause missed notifications or deadlocks; doesn't protect shared resources from race conditions on its own.

---

### 4. MyThreadClass
* **What I Learned:** I learned how to create a custom thread class by inheriting from threading.Thread, start multiple threads, and measure their execution time.
* **How it Executes:** A custom class inherits from Thread and defines a `run()` method. The method prints the thread name and process ID, sleeps to simulate work, and prints a completion message. The main block creates multiple instances, starts them concurrently, joins them to wait for completion, and calculates total execution time.
* **End Use:** Applications requiring concurrent tasks like simulations, I/O-bound operations, or background processing, while needing custom attributes/methods per thread.
* **Short Summary:** Defining a custom thread class, running multiple threads concurrently, waiting for completion using `join()`, and measuring total execution time.
* **Pros & Cons:** - **Advantages:** Easy to create reusable thread objects; saves time on independent tasks; allows performance measurement.
  - **Disadvantages:** Threads share memory, needing synchronization for shared data; too many threads can overwhelm the system.

---

### 5. MyThreadClass_lock
* **What I Learned:** I learned how to use a threading.Lock to ensure that only one thread executes a critical section at a time, preventing race conditions.
* **How it Executes:** A global lock is created using `threading.Lock()`. Inside the custom thread's `run()` method, the thread calls `acquire()` before entering the critical section (simulating work/printing) and calls `release()` when done. This forces multiple concurrent threads to execute the locked section one at a time.
* **End Use:** Critical in scenarios where multiple threads access shared resources (files, databases, counters) to prevent inconsistent data.
* **Short Summary:** Protecting critical sections in multithreaded programs using a global lock to ensure safe, interference-free execution.
* **Pros & Cons:** - **Advantages:** Ensures mutual exclusion; provides predictable output; easy to implement.
  - **Disadvantages:** Increases total execution time due to waiting; forgetting to release the lock causes deadlocks; reduces the concurrency benefit for CPU-bound tasks.

---

### 6. MyThreadClass_lock_2
* **What I Learned:** I learned how to partially use a threading.Lock to protect only a critical section, allowing non-critical code to run concurrently.
* **How it Executes:** The lock is acquired only for a small, critical part of the code (e.g., printing the start message). It is released immediately after, allowing the thread to perform its simulated work (sleeping) outside the lock. This lets multiple threads "work" simultaneously while keeping the shared console output safe.
* **End Use:** Useful when only a specific part of a thread needs mutual exclusion (like updating a variable), while the rest (like downloading a file) can execute concurrently.
* **Short Summary:** Demonstrates selective locking, protecting only the necessary critical section for mutual exclusion while maximizing concurrent execution.
* **Pros & Cons:** - **Advantages:** Reduces thread waiting time; prevents race conditions only where necessary; massively improves overall concurrency and efficiency.
  - **Disadvantages:** If non-critical code accidentally interacts with shared resources, race conditions will still occur; requires careful identification of what truly needs locking.

---

### 7. RLock
* **What I Learned:** I learned how to use Python’s threading.RLock (reentrant lock) to safely manage shared resources when the same thread might need to acquire the lock multiple times.
* **How it Executes:** An RLock object allows a thread to acquire the same lock recursively without deadlocking. The class uses this lock to protect a shared variable. A base method `execute()` acquires the lock, but the `add()` and `remove()` methods also acquire the lock before calling `execute()`. Because it's an RLock, the thread doesn't block itself.
* **End Use:** Complex multithreaded programs where a locked function calls another locked function within the same thread (e.g., nested resource access or inventory management).
* **Short Summary:** Using threading.RLock to safely allow threads to modify a shared resource, specifically handling scenarios where a thread acquires the same lock multiple times.
* **Pros & Cons:** - **Advantages:** Prevents self-deadlocks in recursive or nested function calls; ensures thread-safe operations.
  - **Disadvantages:** Slightly heavier/slower than a normal Lock; misuse can still cause logical errors.

---

### 8. Semaphore
* **What I Learned:** I learned how to use Python’s threading.Semaphore to control access to a shared resource and coordinate threads, ensuring a consumer waits for a producer.
* **How it Executes:** A Semaphore is initialized with a counter of 0. The consumer calls `acquire()` and immediately blocks because the counter is 0. The producer generates an item and calls `release()`, which increments the counter and wakes up the consumer.
* **End Use:** Controlling access to limited resources (like connection pools), managing task queues, or synchronizing thread execution order.
* **Short Summary:** Demonstrates using threading.Semaphore to synchronize execution, effectively forcing a consumer thread to pause until a producer signals that data is ready.
* **Pros & Cons:** - **Advantages:** Excellent for coordinating threads; prevents consumers from proceeding without available resources; handles both single and multiple resource limits.
  - **Disadvantages:** Incorrect use causes deadlocks; does not inherently protect against data corruption if multiple threads modify the exact same variable simultaneously (Locks are still needed for pure mutual exclusion).

---

### 9. Thread_definition
* **What I Learned:** I learned how to create and start threads in Python using the `threading.Thread` class, and how to pass arguments to a function executed by each thread.
* **How it Executes:** A function is defined to print a thread number. A loop creates multiple threads, passes the number as an argument, and starts them. However, because `.join()` is called immediately inside the loop, the main program stops and waits for each thread to finish before creating the next one.
* **End Use:** Used in basic multithreading programs, background tasks, and for learning how threads are created, started, and managed in Python.
* **Short Summary:** Demonstrates how to define and run threads in Python, but because of how `.join()` is placed, they execute sequentially instead of concurrently.
* **Pros & Cons:** - **Advantages:** A very simple way to create threads, pass arguments, and understand the absolute basics of the `threading` module.
  - **Disadvantages:** Because `.join()` is inside the loop, the threads run one by one. This gives zero performance improvement and defeats the purpose of parallel execution.

---

### 10. Thread_determine
* **What I Learned:** I learned how to assign specific names to threads and how to track exactly which thread is currently running using Python's thread identification tools.
* **How it Executes:** Three separate functions are defined. Each function asks for the name of the thread running it, prints a "starting" message, sleeps for 2 seconds to simulate work, and then prints an "exiting" message. The main block creates three threads, assigns them custom names, starts them all at once, and then uses `.join()` to ensure the main program waits for all three to finish.
* **End Use:** Extremely useful for debugging complex multithreaded applications, writing log files, and monitoring which part of the program is executing which specific background task.
* **Short Summary:** Demonstrates how to manually name threads and read those names during execution to track their individual behavior.
* **Pros & Cons:** - **Advantages:** Makes debugging a hundred times easier because you can see exactly which thread is doing what in the console output.
  - **Disadvantages:** The specific method used in the code (`threading.currentThread().getName()`) is actually deprecated in modern Python (the new way is `threading.current_thread().name`). Also, printing these logs adds a tiny bit of processing overhead.

--- 

### 11. Thread_name_and_processes
* **What I Learned:** I learned how to assign custom names to threads using an Object-Oriented approach (custom class) and track which thread is executing a specific task.
* **How it Executes:** A custom class `MyThreadClass` is created by inheriting from Python's main `Thread` class. The `__init__` method sets up the thread's custom name. When started, the `run()` method prints this name. In the main script, two threads are created, started, and then synchronized using `.join()` to ensure the program waits for both to finish.
* **End Use:** Great for structured multithreaded applications where you need to log thread activity, debug execution flow, or manage multiple named worker threads.
* **Short Summary:** Demonstrates how to create and track named threads using a custom Object-Oriented class structure.
* **Pros & Cons:** - **Advantages:** Makes the code much more organized and readable. Custom names make it very easy to identify threads during debugging.
  - **Disadvantages:** The code comments out the actual Process ID (`os.getpid()`) part, so it only shows thread names right now. Also, creating a full custom class just to name a thread adds a slight bit of extra code overhead.

---

### 12. Threading_with_queue
* **What I Learned:** I learned how to use Python's `queue.Queue` to safely pass data between threads (Producer and Consumer) without needing to manually manage locks.
* **How it Executes:** A shared Queue is passed to the threads. A Producer thread generates 5 random numbers and uses `.put()` to add them to the queue. Three Consumer threads run in a continuous loop, using `.get()` to pull numbers out and `.task_done()` to mark them complete. Because the Queue is inherently thread-safe, multiple consumers can pull data without crashing into each other.
* **End Use:** The absolute industry standard for task scheduling, background job processing, worker pools, and complex multithreaded data pipelines.
* **Short Summary:** Demonstrates the safest and cleanest way to share data between multiple threads using a built-in, thread-safe Queue.
* **Pros & Cons:** - **Advantages:** Completely eliminates the need for manual Locks, Events, or Conditions. It handles all the complex thread-safety and synchronization automatically in the background.
  - **Disadvantages:** In this specific code, the consumers run in a `while True:` infinite loop. This means the program will actually hang at the `.join()` statements at the very end because the consumer threads never officially finish or exit.