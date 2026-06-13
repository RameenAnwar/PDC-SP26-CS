# Chapter 2 – Thread Synchronization & Advanced Threading

## Files Included

- Barrier.py
- Condition.py
- Event.py
- Semaphore.py
- Rlock.py
- MyThreadClass.py
- MyThreadClass_lock.py
- MyThreadClass_lock_2.py
- Thread_definition.py
- Thread_determine.py
- Thread_name_and_processes.py
- Threading_with_queue.py

## Topics Covered

- Thread Creation
- Synchronization Techniques
- Locks & RLocks
- Semaphores, Events, Conditions
- Barriers
- Producer-Consumer Problem
- Queue Communication

## How to Execute

```bash
python filename.py
```

## Concept Summary

### Thread Basics

Creating and managing threads using functions and classes.

### Custom Thread Class

Using `Thread` class and overriding `run()` method.

### Locks

Ensures only one thread accesses shared resource at a time.
Prevents race conditions.

### RLock

Same thread can acquire lock multiple times.
Used in nested locking.

### Semaphore

Controls number of threads accessing a resource.

### Condition

Used for communication between threads (wait & notify).

### Event

Used for signaling between threads.

### Barrier

All threads wait until everyone reaches a point.

### Queue

Safe communication between threads (Producer-Consumer).

## Applications

- Multithreaded systems
- Resource sharing
- Real-time processing
- Parallel execution

## Advantages

- Efficient resource usage
- Faster execution
- Safe synchronization

## Disadvantages

- Complex logic
- Deadlocks possible
- Debugging difficult

## Conclusion

Chapter 2 focuses on synchronization techniques to ensure safe and efficient execution of multiple threads in parallel systems.
