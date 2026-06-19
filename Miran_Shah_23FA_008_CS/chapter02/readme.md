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

---

### 1. Barrier
* **What I Learned:** I learned how to use a Barrier to make multiple threads wait for each other at a checkpoint before moving forward.  
* **How it Executes:** You set the number of threads required. Each thread does its work and stops at `.wait()`. Threads continue only when all have reached the barrier.  
* **End Use:** Used in multiplayer games, simulations, or parallel tasks where a stage must finish before continuing.  
* **Short Summary:** Synchronizes threads so they all reach a checkpoint together.  
* **Pros & Cons:**  
  - **Advantages:** Keeps parallel tasks in sync.  
  - **Disadvantages:** If one thread crashes or hangs, all threads wait forever.  

### 2. Condition
* **What I Learned:** I learned how to use Condition variables to make threads wait for a state change before executing.  
* **How it Executes:** A Condition manages shared data. Producer threads pause if storage is full; consumer threads pause if empty. Threads use `.wait()` to pause and `.notify()` to signal others when the state changes.  
* **End Use:** Producer-consumer systems, task queues, or any resource-dependent threads.  
* **Short Summary:** Uses wait/notify to safely pass data between threads.  
* **Pros & Cons:**  
  - **Advantages:** Prevents data errors and ensures proper timing.  
  - **Disadvantages:** Setup is complex; missed notifications can cause indefinite waits.  

### 3. Event
* **What I Learned:** I learned how to use an Event to signal between threads like a traffic light.  
* **How it Executes:** One thread calls `.set()` to signal readiness and `.clear()` to reset. Receiving threads wait on `.wait()` until the signal.  
* **End Use:** Background tasks, simple triggers, or notifying threads of new data.  
* **Short Summary:** Sends a simple signal from one thread to another.  
* **Pros & Cons:**  
  - **Advantages:** Simple; prevents busy waiting.  
  - **Disadvantages:** Only sends a signal, not actual data; does not protect shared memory.  

### 4. MyThreadClass
* **What I Learned:** I learned how to create custom thread classes and run multiple threads concurrently while tracking their execution time.  
* **How it Executes:** Subclass `Thread`, define `run()`, create threads, start them, use `.join()`, and measure total time.  
* **End Use:** Background processing, simulations, or independent concurrent tasks.  
* **Short Summary:** Custom thread objects for concurrent work with timing.  
* **Pros & Cons:**  
  - **Advantages:** Reusable thread objects; organized tasks.  
  - **Disadvantages:** Too many threads can overload CPU; shared data requires careful management.  

### 5. MyThreadClass_lock
* **What I Learned:** I learned how to use a Lock to ensure only one thread accesses a critical section at a time.  
* **How it Executes:** Threads call `.acquire()` before accessing shared resources and `.release()` afterward, forcing others to wait their turn.  
* **End Use:** Writing to shared files, updating databases, or modifying shared variables safely.  
* **Short Summary:** Protects critical code sections to prevent simultaneous access.  
* **Pros & Cons:**  
  - **Advantages:** Prevents race conditions and data corruption.  
  - **Disadvantages:** Threads wait in line, slowing execution; forgetting `.release()` can freeze the program.  

### 6. MyThreadClass_lock_2
* **What I Learned:** I learned how to optimize locks by only locking critical lines, leaving other work parallel.  
* **How it Executes:** `.acquire()` and `.release()` are used only around sensitive code; heavy work runs outside the lock.  
* **End Use:** Safe shared data access without reducing parallel performance.  
* **Short Summary:** Selective locking maximizes speed while keeping code safe.  
* **Pros & Cons:**  
  - **Advantages:** Reduces waiting time, keeps program fast.  
  - **Disadvantages:** Must include all shared data in locked section to avoid corruption.  

### 7. RLock
* **What I Learned:** I learned how to use a Reentrant Lock (RLock) to prevent a thread from blocking itself.  
* **How it Executes:** Same thread can acquire the lock multiple times without freezing. Nested calls to locked functions work safely.  
* **End Use:** Complex programs with nested locked functions.  
* **Short Summary:** Lock that allows a thread to safely lock a resource multiple times.  
* **Pros & Cons:**  
  - **Advantages:** Prevents self-deadlocks.  
  - **Disadvantages:** Slightly slower than regular Lock.  

### 8. Semaphore
* **What I Learned:** I learned how to use a Semaphore to limit how many threads can access a resource at once.  
* **How it Executes:** Semaphore starts with a counter (e.g., 0). Consumers call `.acquire()` but block if the count is 0. Producers call `.release()` to increase the count, unblocking consumers.  
* **End Use:** Limit database connections, manage task queues, or enforce execution order.  
* **Short Summary:** Counter-based control of thread access and order.  
* **Pros & Cons:**  
  - **Advantages:** Controls limits and coordinates thread order.  
  - **Disadvantages:** Does not provide full mutual exclusion; Locks are still needed for shared data.