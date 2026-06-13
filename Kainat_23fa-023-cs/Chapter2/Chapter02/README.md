## BARRIER

This program demonstrates Barrier synchronization using multithreading.

Three threads (runners) start execution at the same time. Each thread takes a random time to reach a common point called the barrier.

When a thread reaches the barrier, it waits until all other threads arrive. Once all threads reach the barrier, they continue execution together.
   
Barrier is used to synchronize multiple threads.

It ensures that all threads reach a certain point before continuing execution.

This is useful when tasks depend on each other and must proceed together.

## CONDITION

This program demonstrates thread synchronization using a Condition variable.

Two threads are used: Producer and Consumer.

The Producer adds items to a shared list, while the Consumer removes items from it.

Both threads wait and notify each other based on the condition of the list.

Condition variables are used to control the execution of threads.

They help threads wait for a condition and notify other threads when the condition changes.

This ensures proper coordination between threads.

## EVENT

This program demonstrates thread synchronization using an Event.

Two threads are used: Producer and Consumer.

The Producer generates items and adds them to a shared list, while the Consumer waits for a signal and then removes items from the list.

Event is used to signal between threads.

One thread can notify another thread when a task is completed.

This helps in coordinating execution between threads.

## MY THREAD CLASS

This program demonstrates creation and execution of multiple threads using a custom Thread class.

Each thread runs independently, prints its name and process ID, sleeps for a random duration, and then finishes execution.

Threads allow multiple tasks to run concurrently within a program.

Each thread executes independently and can complete at different times.

Using join() ensures the main program waits for all threads to finish.

## MT THREAD CLASS LOCK 1

This program demonstrates thread synchronization using a Lock (mutex).

Multiple threads are created, but only one thread can execute the critical section at a time using a lock.

A lock is used to control access to shared resources.

It ensures that only one thread executes a critical section at a time.

This prevents conflicts and maintains correct program behavior.

## MY THREAD CLASS LOCK 2

This program demonstrates the use of a Lock (mutex) in multithreading, but only for a small part of the code.

Multiple threads are created and run concurrently. 

The lock is applied only while printing the "running" message, and then released before the thread sleeps and completes.

Locks can be used to protect only critical sections of code instead of the whole function.

This allows better performance by letting threads run concurrently where safe.

Partial locking improves efficiency compared to locking the entire thread execution.


## RLOCK

This program demonstrates thread synchronization using a Reentrant Lock (RLock).

Two threads are created: one adds items to a shared object (Box) and the other removes items.

Both threads safely modify a shared variable total_items using RLock.

RLock allows a thread to acquire the same lock multiple times safely.

It is useful when a function holding a lock calls another function that also requires the same lock.

This prevents deadlocks and ensures safe access to shared data.

## SEMAPHORES

This program demonstrates thread synchronization using a Semaphore.

It implements a simple producer-consumer behavior where the Producer generates an item and the Consumer waits until the item is available before consuming it.

The Producer produces a random number after a delay, and the Consumer waits until the semaphore signals that the item is ready.

A semaphore is used to control access between threads and to signal availability of resources.

It allows one thread to notify another when a resource becomes available.

This helps in coordinating execution between producer and consumer threads.

## THREAD DEFINITION

This program demonstrates a basic example of multithreading in Python.
It creates 10 threads, and each thread calls a function that prints its thread number.

Each thread is started and immediately joined, meaning they execute one after another instead of fully parallel execution.

Threads can be created using the threading module.

If join() is used immediately after start(), threads behave like serial execution.

To achieve parallel execution, all threads should be started first and then joined afterward.

## THREAD DETERMINE

This program demonstrates basic multithreading in Python using three separate functions executed in different threads.

Each thread is given a name and runs independently, printing messages when starting and exiting.

Threads can be assigned custom names for better identification during execution.

Each thread runs independently and can execute concurrently with others.

The join() method ensures that the main program waits for all threads to complete before exiting.

## THREAD NAME AND PROCESES

This program demonstrates how to create threads by extending the Thread class in Python.

Two threads are created, and each thread prints its name when it is running.

It also demonstrates how threads belong to the same process.

Threads can be created by inheriting the Thread class and overriding the run() method.

All threads run within the same process, but execute independently.

Thread execution can be controlled using start() and join() methods.

## THREAD WITH QUEUE

This program demonstrates thread synchronization using a Queue in Python.

One Producer thread generates random items and adds them to a shared queue.

Multiple Consumer threads take items from the queue and process them.

The Queue automatically handles synchronization between threads.

Queue is a thread-safe structure used for communication between threads.

It automatically handles locking, so manual synchronization is not required.

Producer adds data and Consumers safely retrieve it without conflict.