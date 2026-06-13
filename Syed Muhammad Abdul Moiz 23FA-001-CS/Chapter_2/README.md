# Chapter 2 

### Table of Contents
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
* **What I Learned:** I learned how to use a Barrier to make multiple threads wait for each other at a specific checkpoint before moving forward.
* **How it Executes:** You set a specific number of threads required. Each thread does its work and stops at the barrier using .wait(). The threads only continue running when all of them have reached this checkpoint.
* **End Use:** Used in multiplayer games, simulations, or parallel tasks where a specific stage must be completed by everyone before starting the next stage.
* **Short Summary:** Synchronizing threads to ensure they all reach a checkpoint together before continuing.
* **Pros & Cons:** - **Advantages:** Easily keeps parallel tasks in sync.
  - **Disadvantages:** If even one thread crashes or gets stuck before the barrier, all other threads will be stuck waiting forever.

### 2. Condition
* **What I Learned:** I learned how to use Condition variables to make threads wait for a specific state change (like checking if a list is full or empty) before doing their job.
* **How it Executes:** A Condition manages access to shared data. A 'Producer' thread adds data but pauses if the storage is full. A 'Consumer' thread removes data but pauses if it is empty. Threads use .wait() to pause and .notify() to wake other threads up when the data changes.
* **End Use:** Best for "producer-consumer" systems, task queues, or anywhere threads need to wait for resources to become available.
* **Short Summary:** Using a Condition to safely pass data between threads by making them wait and notify each other.
* **Pros & Cons:** - **Advantages:** Prevents data errors and ensures threads only run when the right conditions are met.
  - **Disadvantages:** Complex to set up, and a missed notification can cause threads to pause indefinitely.

### 3. Event
* **What I Learned:** I learned how to use an Event to act like a simple traffic light, allowing one thread to send a signal to another thread.
* **How it Executes:** One thread works and then calls .set() to turn the "green light" on, signaling that data is ready. It then uses .clear() to reset the light. The receiving thread waits at .wait() until the green light is signaled before it proceeds.
* **End Use:** Perfect for simple triggers, like telling background workers that new data has arrived and is ready to process.
* **Short Summary:** A simple signaling mechanism to let one thread know that another thread has finished a task.
* **Pros & Cons:** - **Advantages:** Very simple to use and stops the CPU from wasting power on busy waiting.
  - **Disadvantages:** It only sends a basic signal (no actual data). It also doesn't protect shared memory from race conditions on its own.

### 4. MyThreadClass
* **What I Learned:** I learned how to create my own custom Thread blueprint (class) and run multiple threads at the same time while tracking their speed.
* **How it Executes:** The script creates a custom class that inherits from Python's main Thread class. Inside, it defines a run() method with simulated work. The main script creates several of these custom threads, starts them, uses .join() to wait for them, and calculates the total time.
* **End Use:** Great for background processing or simulations where each thread needs its own specific attributes and custom behaviors.
* **Short Summary:** Building custom thread objects to run concurrent tasks and measure how long they take.
* **Pros & Cons:** - **Advantages:** Makes thread objects reusable and keeps independent tasks organized.
  - **Disadvantages:** Creating too many threads can overload the computer, and shared data still needs careful management.

### 5. MyThreadClass_lock
* **What I Learned:** I learned how to use a Lock to block other threads from entering a sensitive part of the code (critical section) at the same time.
* **How it Executes:** A global lock is created. Before doing its main work or modifying shared data, the thread uses .acquire() to lock the door. Once finished, it uses .release() to unlock it. This forces threads to take turns.
* **End Use:** Crucial whenever multiple threads are trying to write to the same file, update a database, or change the same variable at once.
* **Short Summary:** Using a global lock to protect sensitive code so that only one thread can run it at a time.
* **Pros & Cons:** - **Advantages:** Guarantees that shared data won't get corrupted (prevents race conditions).
  - **Disadvantages:** Forces threads to wait in line, which slows down the program. Forgetting to unlock will freeze the whole script.

### 6. MyThreadClass_lock_2
* **What I Learned:** I learned how to optimize locks by only locking the exact lines of code that need protection, leaving the rest of the thread free to run in parallel.
* **How it Executes:** Instead of locking the entire thread's workload, the .acquire() and .release() are used strictly around the tiny shared part (like a print statement). The heavy work (like sleeping or downloading) happens outside the lock so threads can still multitask.
* **End Use:** Used when you want the safety of a lock but also want to keep the high speed of parallel processing.
* **Short Summary:** Selectively locking only the sensitive parts of the code to maximize speed and efficiency.
* **Pros & Cons:** - **Advantages:** Drastically reduces waiting time and keeps the program running fast while staying safe.
  - **Disadvantages:** You have to be very careful; if you accidentally leave out a shared variable from the locked area, the data will corrupt.

### 7. RLock
* **What I Learned:** I learned how to use a Reentrant Lock (RLock) to avoid a situation where a thread accidentally blocks itself.
* **How it Executes:** An RLock lets the same thread lock the door multiple times without getting stuck. In this script, a base method locks the resource, but other methods also lock it before calling the base method. The RLock remembers that the thread already owns the lock and lets it through.
* **End Use:** Very useful in complex programs where a locked function might call another locked function from inside the same thread.
* **Short Summary:** Using a special lock that allows a single thread to safely lock the same resource multiple times without freezing.
* **Pros & Cons:** - **Advantages:** Completely prevents self-deadlocks in nested functions.
  - **Disadvantages:** It runs slightly slower than a regular Lock because it has to keep track of who owns it.

### 8. Semaphore
* **What I Learned:** I learned how to use a Semaphore to act like a bouncer, limiting how many threads can access a resource or forcing threads to wait for a signal.
* **How it Executes:** A Semaphore is created with a starting counter of 0. A Consumer thread tries to .acquire() it but gets blocked because the count is zero. A Producer thread finishes its work and calls .release(), which increases the counter and wakes the Consumer up.
* **End Use:** Ideal for limiting connections to a database, managing task queues, or enforcing a strict order between threads.
* **Short Summary:** Using a counter-based Semaphore to pause a consumer thread until a producer thread says data is ready.
* **Pros & Cons:** - **Advantages:** Perfect for controlling limits and coordinating the exact order of threads.
  - **Disadvantages:** It doesn't provide pure mutual exclusion for shared data on its own (you still need Locks for that), and mistakes can cause deadlocks.

### 9. Thread_definition
* **What I Learned:** I learned how to create and start threads using a simple function, without making a class. It showed me the basic structure of multithreading in Python.
* **How it Executes:** A function is defined that prints which thread is calling it. In the main function, multiple threads are created using a loop. Each thread is started using `.start()` and immediately joined using `.join()`, so threads execute one by one.
* **End Use:** Useful for understanding the basics of thread creation and execution, especially for small tasks or beginner-level multithreading programs.
* **Short Summary:** Creating threads using a simple function and running them sequentially using `.start()` and `.join()`.
* **Pros & Cons:** - **Advantages:** Very simple and easy to understand for beginners.
  - **Disadvantages:** Because of immediate `.join()`, threads don’t run in parallel, reducing performance benefits.

### 10. Thread_determine
* **What I Learned:** I learned how to assign names to threads and identify which thread is currently running.
* **How it Executes:** Three different functions are created. Each thread is given a custom name and runs its respective function. Inside each function, `currentThread().getName()` is used to print which thread is executing, along with start and exit messages.
* **End Use:** Helpful in debugging and tracking thread execution in complex applications where multiple threads are running.
* **Short Summary:** Naming threads and identifying them during execution using built-in threading functions.
* **Pros & Cons:** - **Advantages:** Makes debugging easier by clearly showing which thread is active.
  - **Disadvantages:** Adds extra code and is not necessary for very small programs.

### 11. Thread_name_and_processes
* **What I Learned:** I learned how to create custom threads using a class and assign names to them for better identification.
* **How it Executes:** A custom class is created by extending `Thread`. Each thread is initialized with a name. When executed, each thread prints its name. Threads are started and then joined to ensure the program waits for completion.
* **End Use:** Useful when managing multiple threads in a structured way, especially when each thread represents a specific task.
* **Short Summary:** Using a custom thread class to assign names and manage thread execution.
* **Pros & Cons:** - **Advantages:** Provides better organization and readability when working with multiple threads.
  - **Disadvantages:** Slightly more complex compared to simple function-based threading.

### 12. Threading_with_queue
* **What I Learned:** I learned how to use a Queue to safely share data between threads without manually handling locks.
* **How it Executes:** A Producer thread generates random items and puts them into a queue. Multiple Consumer threads continuously take items from the queue and process them. The queue automatically handles synchronization between threads.
* **End Use:** Commonly used in producer-consumer systems like task scheduling, job processing systems, and message queues.
* **Short Summary:** Using a queue to manage communication between producer and consumer threads safely.
* **Pros & Cons:** - **Advantages:** Built-in thread safety, no need to manually use locks; easy to implement producer-consumer pattern.
  - **Disadvantages:** Consumers may run indefinitely if not properly stopped; slightly harder to control flow in complex cases.