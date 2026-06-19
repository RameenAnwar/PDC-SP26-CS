# CHAPTER 2

## 1. Barrier.py

### Description

Demonstrates synchronization of multiple threads using a `threading.Barrier`, where threads wait until all participants reach a common point.

### How it works

* Three threads represent runners.
* Each thread sleeps for a random time.
* All threads call `Barrier.wait()`.
* Execution continues only when all threads reach the barrier.

### Result

All threads pause at the barrier and resume simultaneously once all have arrived.

### Advantages

* Useful for coordinating phases of execution.
* Ensures all threads reach a checkpoint before proceeding.

### Disadvantages

* Requires exact number of threads.
* Can lead to deadlock if a thread fails to reach the barrier.

### Where it can be used

* Parallel simulations
* Multi-stage computations
* Game engines (synchronizing rounds)

---

## 2. Condition.py

### Description

Implements producer-consumer problem using `threading.Condition`.

### How it works

* Producer adds items to a shared list.
* Consumer removes items.
* Threads wait when conditions are not satisfied (empty/full buffer).
* `condition.wait()` and `condition.notify()` manage synchronization.

### Result

Producer and consumer coordinate access to shared resource without conflicts.

### Advantages

* Fine-grained synchronization.
* Efficient communication between threads.

### Disadvantages

* Complex logic.
* Risk of missed notifications or deadlocks if misused.

### Where it can be used

* Producer-consumer systems
* Buffer management
* Task scheduling systems

---

## 3. Event.py

### Description

Uses `threading.Event` for signaling between producer and consumer threads.

### How it works

* Producer sets an event after adding an item.
* Consumer waits for the event using `event.wait()`.
* Consumer proceeds when event is set.

### Result

Consumer only processes items when signaled by producer.

### Advantages

* Simple signaling mechanism.
* Easy to implement one-to-many or one-to-one communication.

### Disadvantages

* No built-in queueing of events.
* Missed signals if not handled properly.

### Where it can be used

* Trigger-based systems
* Start/stop signals
* Thread coordination

---

## 4. MyThreadClass.py

### Description

Basic example of thread creation using Python’s `Thread` class.

### How it works

* Each thread executes a `run()` method.
* Threads sleep for a random duration.
* No synchronization is used.

### Result

Multiple threads run concurrently and print messages independently.

### Advantages

* Simple to understand threading basics.
* Demonstrates concurrency.

### Disadvantages

* No control over shared resources.
* No synchronization.

### Where it can be used

* Basic concurrent tasks
* Learning threading fundamentals

---

## 5. MyThreadClass_lock.py

### Description

Demonstrates thread synchronization using a `Lock`.

### How it works

* A lock is acquired before critical section.
* Only one thread executes the critical section at a time.
* Lock is released after execution.

### Result

Threads execute critical section sequentially.

### Advantages

* Prevents race conditions.
* Ensures data integrity.

### Disadvantages

* Can reduce concurrency.
* Risk of deadlock if not handled properly.

### Where it can be used

* Shared resource protection
* File/database access
* Critical section control

---

## 6. MyThreadClass_lock_2.py

### Description

Similar to the previous lock example but emphasizes timing and multiple threads.

### How it works

* Multiple threads acquire a lock before printing.
* Each thread sleeps after releasing lock.

### Result

Threads execute one at a time in critical section, but sleep concurrently.

### Advantages

* Demonstrates real-world lock usage with multiple threads.

### Disadvantages

* Still limits concurrency in critical section.

### Where it can be used

* Controlled logging systems
* Sequential task execution within concurrency

---

## 7. Rlock.py

### Description

Uses `threading.RLock` (re-entrant lock) to allow a thread to acquire the same lock multiple times.

### How it works

* Methods `add`, `remove`, and `execute` all acquire the same lock.
* A thread can safely re-acquire the lock within nested calls.

### Result

Safe nested locking without deadlocks.

### Advantages

* Prevents deadlock in recursive locking.
* Suitable for complex object-oriented locking.

### Disadvantages

* Slightly more overhead than standard lock.

### Where it can be used

* Recursive functions
* Complex class-based synchronization
* Nested resource access

---

## 8. Semaphore.py

### Description

Demonstrates use of `threading.Semaphore` for controlling access.

### How it works

* Semaphore initialized to 0.
* Consumer waits using `acquire()`.
* Producer releases semaphore after producing an item.

### Result

Consumer waits until producer signals availability.

### Advantages

* Controls access to limited resources.
* Useful for signaling between threads.

### Disadvantages

* Harder to debug than simple locks.
* Mismanagement can cause blocking issues.

### Where it can be used

* Resource pooling
* Connection limiting
* Signaling mechanisms

---

## 9. Thread_definition.py

### Description

Basic thread creation using a function target.

### How it works

* A function is executed in multiple threads.
* Each thread prints its identifier.

### Result

Threads execute function concurrently.

### Advantages

* Simple thread creation using functions.
* Lightweight implementation.

### Disadvantages

* Limited structure compared to classes.
* Harder to extend.

### Where it can be used

* Simple parallel tasks
* Quick concurrency experiments

---

## 10. Thread_determine.py

### Description

Demonstrates naming and identifying threads.

### How it works

* Threads are given custom names.
* Each thread prints its name during execution.

### Result

Threads display their execution identity.

### Advantages

* Useful for debugging and logging.
* Helps track thread execution.

### Disadvantages

* No synchronization mechanism.

### Where it can be used

* Debugging multithreaded applications
* Logging systems

---

## 11. Thread_name_and_processes.py

### Description

Shows thread identification along with process information.

### How it works

* Threads print identifiers (and optionally process IDs).
* Helps distinguish between threads in a process.

### Result

Displays thread identity and process-related information.

### Advantages

* Useful for system-level debugging.
* Helps understand multiprocessing vs multithreading.

### Disadvantages

* Limited functional complexity.

### Where it can be used

* System diagnostics
* Debugging concurrent programs

---

## 12. Threading_with_queue.py

### Description

Implements producer-consumer model using `queue.Queue`.

### How it works

* Producer puts items into a queue.
* Multiple consumers retrieve items using `get()`.
* Queue handles synchronization internally.

### Result

Safe communication between threads without manual locking.

### Advantages

* Thread-safe by default.
* Simplifies producer-consumer design.
* Avoids explicit locks/conditions.

### Disadvantages

* Less control over synchronization logic.
* Blocking behavior may require tuning.

### Where it can be used

* Task queues
* Job scheduling systems
* Background worker systems
* Pipeline architectures

---
