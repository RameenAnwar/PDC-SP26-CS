# Chapter 2: Thread-Based Parallelism

This folder contains Python scripts that demonstrate how to implement thread-based parallelism using Python's built-in `threading` module. It covers basic thread creation, subclassing, and various synchronization primitives to manage concurrent execution safely.

## 📂 File Overview

### 1. Thread Basics
These scripts demonstrate the fundamental ways to create and manage threads:
* **`Thread_definition.py`**: Shows how to instantiate and start basic threads by passing a target function.
* **`Thread_determine.py`**: Demonstrates how to name threads and identify the currently executing thread.
* **`MyThreadClass.py`**: Shows how to implement threads by subclassing the `threading.Thread` class and overriding the `run()` method.

### 2. Thread Synchronization (Locks)
These scripts tackle the problem of race conditions by using Locks to restrict access to shared resources:
* **`MyThreadClass_lock.py` & `MyThreadClass_lock_2.py`**: Implementations of basic Thread Locks (`threading.Lock()`) to acquire and release shared resources safely among multiple threads.
* **`Rlock.py`**: Demonstrates the use of Reentrant Locks (`threading.RLock()`), allowing the same thread to acquire the lock multiple times without causing a deadlock.

### 3. Advanced Synchronization Primitives
These scripts cover advanced mechanisms for thread communication and coordination:
* **`Semaphore.py`**: Uses `threading.Semaphore()` to manage an internal counter, controlling access to a resource with limited capacity.
* **`Condition.py`**: Implements a classic Producer-Consumer model using `threading.Condition()`, allowing threads to wait for specific state changes and notify others.
* **`Event.py`**: Uses `threading.Event()` for simple communication between threads (one thread sets the event, others wait for it to be set).
* **`Barrier.py`**: Demonstrates `threading.Barrier()`, forcing a specific number of threads to wait for each other at a defined synchronization point before proceeding.

## 🚀 How to Run the Tests

To test any of the synchronization concepts, run the respective file from your terminal/command prompt:

```bash
# Example: Running the Semaphore test
python Semaphore.py

# Example: Running the Barrier test
python Barrier.py

```

## 👨‍💻 Author
**Huzaifa Alim** - Computer Science Student @ Usman Institute of Technology

## 📜 License
This project is open source and available under the MIT License.

