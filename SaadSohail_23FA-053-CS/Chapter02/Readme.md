# chapter 02 : Threading and Synchronization in Python

## 1. Thread_definition.py

### What I learned

This program shows the basic way to create threads using a function. Each thread runs a simple function and prints its number.

### How to execute

python Thread_definition.py

### End use

Used to understand basic thread creation.

### When and how to use

Used when simple parallel tasks are needed. Threads are created using threading.Thread and started using start().

### Summary

Basic introduction to threading.

### Advantages

* Simple and easy to understand
* Good for beginners

### Disadvantages

* Not suitable for complex tasks

---

## 2. Thread_determine.py

### What I learned

This program demonstrates how different threads run simultaneously and how their execution can be tracked using thread names.

### How to execute

python Thread_determine.py

### End use

Used to observe thread execution behavior.

### When and how to use

Used when debugging or analyzing thread execution.

### Summary

Shows how threads start and finish independently.

### Advantages

* Helps understand execution flow

### Disadvantages

* No synchronization used

---

## 3. Thread_name_and_processes.py

### What I learned

This file shows how thread names can be assigned and displayed during execution.

### How to execute

python Thread_name_and_processes.py

### End use

Useful for identifying threads in debugging.

### When and how to use

Used when multiple threads are running and need identification.

### Summary

Focuses on thread identification.

### Advantages

* Improves readability and debugging

### Disadvantages

* Does not control execution

---

## 4. MyThreadClass.py

### What I learned

This program demonstrates creating threads using a class instead of a function. Each thread performs a task and sleeps for a random time.

### How to execute

python MyThreadClass.py

### End use

Used in object-oriented multi-threaded applications.

### When and how to use

Used when thread logic needs to be organized using classes.

### Summary

Thread creation using class-based approach.

### Advantages

* Better structure
* Reusable code

### Disadvantages

* Slightly complex for beginners

---

## 5. MyThreadClass_lock.py

### What I learned

This program uses a lock to ensure that only one thread runs a critical section at a time.

### How to execute

python MyThreadClass_lock.py

### End use

Used to protect shared resources.

### When and how to use

Used when multiple threads access the same data.

### Summary

Demonstrates lock-based synchronization.

### Advantages

* Prevents race conditions

### Disadvantages

* Can slow down execution

---

## 6. MyThreadClass_lock_2.py

### What I learned

This is another version of lock usage where locking and unlocking are handled slightly differently.

### How to execute

python MyThreadClass_lock_2.py

### End use

Used to understand different lock handling techniques.

### When and how to use

Used when experimenting with lock placement.

### Summary

Shows variation in lock usage.

### Advantages

* Flexible locking approach

### Disadvantages

* Can be confusing

---

## 7. Rlock.py

### What I learned

This program demonstrates the use of a reentrant lock (RLock), which allows the same thread to acquire the lock multiple times.

### How to execute

python Rlock.py

### End use

Used in nested locking situations.

### When and how to use

Used when a function calls another function that also needs locking.

### Summary

Advanced locking mechanism.

### Advantages

* Prevents self-deadlock

### Disadvantages

* Slightly slower

---

## 8. Semaphore.py

### What I learned

This program shows how a semaphore controls access to a resource by allowing a limited number of threads.

### How to execute

python Semaphore.py

### End use

Used in resource management.

### When and how to use

Used when access needs to be limited.

### Summary

Controls number of active threads.

### Advantages

* Efficient resource control

### Disadvantages

* Complex for beginners

---

## 9. Event.py

### What I learned

This program demonstrates communication between threads using events. One thread signals and others wait.

### How to execute

python Event.py

### End use

Used for signaling between threads.

### When and how to use

Used when one thread depends on another.

### Summary

Thread communication using signals.

### Advantages

* Simple communication

### Disadvantages

* Risk of missed signals

---

## 10. Condition.py

### What I learned

This program implements a producer-consumer model using condition variables.

### How to execute

python Condition.py

### End use

Used in task queues and buffering systems.

### When and how to use

Used when threads depend on conditions.

### Summary

Advanced thread coordination.

### Advantages

* Efficient synchronization

### Disadvantages

* Complex implementation

---

## 11. Barrier.py

### What I learned

This program shows how threads wait at a barrier until all threads reach the same point.

### How to execute

python Barrier.py

### End use

Used in parallel computations.

### When and how to use

Used when synchronization is needed at a checkpoint.

### Summary

Synchronizes threads at a fixed point.

### Advantages

* Ensures coordination

### Disadvantages

* Fixed number of threads required

---

## 12. Threading_with_queue.py

### What I learned

This program uses a queue to safely pass data between threads.

### How to execute

python Threading_with_queue.py

### End use

Used in producer-consumer systems.

### When and how to use

Used when safe data sharing is required.

### Summary

Thread-safe communication using queue.

### Advantages

* Safe and easy

### Disadvantages

* Blocking may slow execution

---

