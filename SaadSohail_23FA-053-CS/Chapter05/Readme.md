# Chapter 05 : Concurrency and Async Programming in Python

This chapter contains Python programs related to concurrency, multithreading, multiprocessing, asyncio tasks, event loops, futures, callbacks, and finite state machines.

---

## 1. concurrent_futures.py

### What I learned

This program demonstrates sequential execution, thread pool execution, and process pool execution using Python’s `concurrent.futures` module.

### How to execute

```bash
python concurrent_futures.py
```

### End use

Used for improving performance by running multiple tasks concurrently.

### When and how to use

Used when tasks can run independently using threads or processes.

### Summary

Compares sequential execution with thread-based and process-based execution.

### Advantages

* Faster execution
* Supports parallel processing
* Easy implementation

### Disadvantages

* Threads are limited by GIL for CPU tasks
* Process pools consume more memory

---

## 2. asyncio_tasks.py

### What I learned

This program demonstrates asynchronous task execution using `asyncio.Task`.

### How to execute

```bash
python asyncio_tasks.py
```

### End use

Used for running multiple asynchronous operations simultaneously.

### When and how to use

Used when applications require non-blocking execution.

### Summary

Executes factorial, fibonacci, and binomial coefficient functions asynchronously.

### Advantages

* Efficient asynchronous execution
* Better handling of waiting operations

### Disadvantages

* Complex for beginners
* Not ideal for CPU-heavy tasks

---

## 3. event_loop_tasks.py

### What I learned

This program demonstrates task scheduling using the asyncio event loop.

### How to execute

```bash
python event_loop_tasks.py
```

### End use

Used for scheduling delayed and repeated tasks.

### When and how to use

Used in event-driven systems and asynchronous applications.

### Summary

Demonstrates task switching between Task A, Task B, and Task C using the event loop.

### Advantages

* Efficient event handling
* Supports timed execution

### Disadvantages

* Blocking operations reduce efficiency
* Debugging can be difficult

---

## 4. finite_state_machine.py

### What I learned

This program demonstrates a Finite State Machine (FSM) using asyncio coroutines.

### How to execute

```bash
python finite_state_machine.py
```

### End use

Used for state-based systems and workflow simulations.

### When and how to use

Used when systems transition between multiple states.

### Summary

Simulates transitions between different states asynchronously.

### Advantages

* Easy state management
* Useful for simulations

### Disadvantages

* Difficult to manage large state systems

---

## 5. future_callbacks.py

### What I learned

This program demonstrates the use of `Future` objects and callback functions in asyncio.

### How to execute

```bash
python future_callbacks.py 5 6
```

### End use

Used for handling asynchronous results.

### When and how to use

Used when asynchronous tasks need callbacks after completion.

### Summary

Executes asynchronous computations and prints results using callback functions.

### Advantages

* Efficient result handling
* Supports asynchronous programming

### Disadvantages

* Callback chains become complex
* Harder debugging