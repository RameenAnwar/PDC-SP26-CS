# Threading and Synchronization in Python

## Student Information
**Name:** Shameer Waqar  
**Roll Number:** 23FA-011-CS  

---

## Overview
This repository focuses on the mechanics of threading in Python. It explores how multiple threads can be managed and controlled using various synchronization techniques. Each script demonstrates a specific concurrency concept, providing a practical foundation for building and managing multi-threaded systems.

---

## Scripts & Concepts

### 1. `Thread_definition.py`
* **Description:** Introduces the fundamentals of thread creation using functions. Demonstrates how threads can execute simple tasks independently.
* **Execution:** `python Thread_definition.py`
* **Use Case:** Best for running basic, isolated tasks concurrently.
* **Pros & Cons:** Highly accessible for beginners, but lacks advanced functionality.

### 2. `Thread_determine.py`
* **Description:** Illustrates parallel execution and demonstrates how to track thread activity using assigned thread names.
* **Execution:** `python Thread_determine.py`
* **Use Case:** Essential for observing, analyzing, and debugging the execution flow of multi-threaded programs.
* **Pros & Cons:** Great for understanding concurrency flow, but lacks resource synchronization.

### 3. `Thread_name_and_processes.py`
* **Description:** Focuses on the identification and naming conventions of threads during active execution.
* **Execution:** `python Thread_name_and_processes.py`
* **Use Case:** Useful when managing complex applications where multiple threads need to be distinctly tracked.
* **Pros & Cons:** Improves code clarity and debugging, though it does not provide execution control.

### 4. `MyThreadClass.py`
* **Description:** Transitions to an object-oriented approach. Threads are created using classes, with each performing a task and pausing for randomized intervals.
* **Execution:** `python MyThreadClass.py`
* **Use Case:** Ideal for scenarios requiring a structured, modular, and reusable threading architecture.
* **Pros & Cons:** Keeps code organized and reusable, but introduces a slightly steeper learning curve.

### 5. `MyThreadClass_lock.py`
* **Description:** Introduces the concept of Lock synchronization to restrict critical section access to a single thread at a time.
* **Execution:** `python MyThreadClass_lock.py`
* **Use Case:** Crucial when multiple threads need to safely read and write to shared data.
* **Pros & Cons:** Successfully prevents race conditions, though it may introduce minor performance bottlenecks.

### 6. `MyThreadClass_lock_2.py`
* **Description:** Showcases an alternative architectural approach to implementing locks within thread execution.
* **Execution:** `python MyThreadClass_lock_2.py`
* **Use Case:** Useful for experimenting with different lock placements and synchronization architectures.
* **Pros & Cons:** Offers flexibility, but the logic can become difficult to track.

### 7. `Rlock.py`
* **Description:** Explores Reentrant Locks (RLocks), allowing the same thread to acquire a lock multiple times without deadlocking itself.
* **Execution:** `python Rlock.py`
* **Use Case:** Necessary for nested functions or recursive algorithms that share the same lock.
* **Pros & Cons:** Prevents self-deadlocks, but comes with slight processing overhead.

### 8. `Semaphore.py`
* **Description:** Demonstrates how semaphores act as internal counters to limit the total number of threads accessing a specific resource simultaneously.
* **Execution:** `python Semaphore.py`
* **Use Case:** Perfect for controlling access to strictly limited resources (e.g., database connections).
* **Pros & Cons:** Highly efficient for throttling, but can be difficult to orchestrate in massive systems.

### 9. `Event.py`
* **Description:** Implements signal-based synchronization. One thread dispatches a signal while others wait for it before proceeding.
* **Execution:** `python Event.py`
* **Use Case:** Used when a thread's execution is entirely dependent on the completion of another task.
* **Pros & Cons:** Clean and simple communication, but carries the risk of missed or deadlocked signals.

### 10. `Condition.py`
* **Description:** Implements a classic producer-consumer model using condition variables for advanced state tracking.
* **Execution:** `python Condition.py`
* **Use Case:** Ideal for queue-based systems where threads must pause until a specific state is met.
* **Pros & Cons:** Highly efficient coordination, but requires managing complex internal logic.

### 11. `Barrier.py`
* **Description:** Explores checkpoint synchronization. Threads are forced to wait at a designated barrier until all participating threads have arrived.
* **Execution:** `python Barrier.py`
* **Use Case:** Necessary for phased parallel tasks where all threads must finish step one before moving to step two.
* **Pros & Cons:** Guarantees absolute coordination, but strictly requires a fixed, predetermined number of threads.

### 12. `Threading_with_queue.py`
* **Description:** Utilizes thread-safe queues to seamlessly exchange data between executing threads.
* **Execution:** `python Threading_with_queue.py`
* **Use Case:** The standard approach for data sharing in robust producer-consumer architectures.
* **Pros & Cons:** Inherently thread-safe and straightforward to implement, though queue bottlenecks can cause delays.

---

## Conclusion
This section provided a comprehensive deep-dive into Python's threading capabilities. By exploring various synchronization modules—from simple Locks to complex Barriers and Queues—I developed a clear understanding of how to handle concurrent operations efficiently while maintaining strict data consistency.