# Chapter 3 – Process-Based Parallelism

## Overview
This chapter explores process-based parallelism in Python using the `multiprocessing` module. Unlike thread-based parallelism, processes run in separate memory spaces and leverage multiple CPU cores. The chapter covers process creation, lifecycle management, inter-process communication, synchronization, and pooling.

> **Note:** All examples in this chapter should be run from the Command Prompt, not IDLE, as the `__main__` module is not importable by child processes in IDLE.

---

## Topics Covered

### 1. Understanding Python's Multiprocessing Module
**Concept:** Introduction to `multiprocessing`

**Explanation:**
The `multiprocessing` module is part of Python's standard library and implements the shared memory programming paradigm. It allows one or more processors with access to shared memory to execute tasks in parallel. It closely mirrors the `threading` API but uses separate processes instead of threads, bypassing Python's Global Interpreter Lock (GIL).

**Use:**
Used for CPU-bound tasks that benefit from true parallelism across multiple processor cores.

**Pros:**
- Bypasses the GIL for true parallel execution
- Isolated memory space prevents accidental data corruption

**Cons:**
- Higher memory usage than threads
- Inter-process communication is more complex

---

### 2. Spawning a Process
**Concept:** Child Process Creation

**Explanation:**
Spawning a process is the creation of a child process from a parent process. The parent can continue asynchronously or wait for the child to finish. The three steps are: define a `Process` object with a target function, call `start()` to begin execution, and call `join()` to wait for completion. Without `join()`, child processes do not end and must be killed manually.

**Use:**
Used to run independent tasks in parallel by launching separate child processes.

**Pros:**
- Simple and intuitive API
- Full isolation between parent and child

**Cons:**
- Process startup is slower than thread creation
- Must instantiate `Process` inside `if __name__ == '__main__'` block

---

### 3. Naming a Process
**Concept:** Process Identification

**Explanation:**
Processes can be assigned names for easier tracking and debugging. The main Python process is identified as `multiprocessing.process._MainProcess`, while child processes are identified as `multiprocessing.process.Process`. The current process name can be retrieved with `multiprocessing.current_process().name`.

**Use:**
Useful in applications with multiple service processes to distinguish each one in logs and output.

**Pros:**
- Improves readability of logs
- Simplifies debugging multi-process applications

**Cons:**
- Cosmetic only; does not affect process behavior

---

### 4. Running Processes in the Background
**Concept:** Daemon Processes

**Explanation:**
Background processes (daemon processes on Unix-like systems) run without user intervention, often handling long-running tasks like file sharing or OS updates. In Python's `multiprocessing` module, a process can be set as a daemon by setting its `daemon` attribute to `True`. Daemon processes are automatically terminated when the main program exits.

**Use:**
Used for background services or monitoring tasks that should not block program exit.

**Pros:**
- Automatically cleaned up when the parent process exits
- Suitable for long-running background tasks

**Cons:**
- Cannot spawn child processes of their own
- Forcefully terminated; no graceful shutdown guarantee

---

### 5. Killing a Process
**Concept:** Process Termination

**Explanation:**
Processes can be forcefully terminated using the `terminate()` method. The `is_alive()` method checks whether a process is still running. This is important in applications where a process may hang or need to be stopped based on a condition.

**Use:**
Used to forcefully stop a misbehaving or no-longer-needed process and free system resources.

**Pros:**
- Immediate termination
- Frees system resources quickly

**Cons:**
- Does not allow the process to clean up gracefully
- May leave shared resources in an inconsistent state

---

### 6. Defining Processes in a Subclass
**Concept:** Custom Process Class

**Explanation:**
The `multiprocessing.Process` class can be subclassed to encapsulate process logic. This requires overriding the `run()` method (and optionally `__init__`) to define the behavior executed when the process starts. The process is launched with `start()`, which internally calls `run()`.

**Use:**
Used when process behavior is complex enough to be organized as a class with state and methods.

**Pros:**
- Clean, object-oriented design
- Easier to manage process-specific state

**Cons:**
- Slightly more verbose than functional approach

---

### 7. Using a Queue to Exchange Data
**Concept:** Inter-Process Queue (FIFO)

**Explanation:**
A queue is a First-In, First-Out (FIFO) data structure used to safely pass data between processes. In the producer-consumer pattern, the producer puts data into the queue and the consumer retrieves it. The `multiprocessing.Queue` class handles internal locking, preventing race conditions automatically.

**Use:**
Used for safe, ordered data exchange between producer and consumer processes.

**Pros:**
- Thread- and process-safe by design
- Handles synchronization internally
- Supports blocking and timeout operations

**Cons:**
- Slightly slower than pipes due to additional overhead
- Queue is built on top of `Pipe()`, so performance is indirectly dependent

---

### 8. Using Pipes to Exchange Objects
**Concept:** Inter-Process Pipe

**Explanation:**
A pipe provides a direct communication channel between two processes. `multiprocessing.Pipe()` returns a pair of connection objects `(conn1, conn2)`. The `duplex` parameter controls whether the pipe is bidirectional (`True`) or unidirectional (`False`). Each connection uses `send()` and `recv()` methods to exchange objects.

**Use:**
Used when two processes need to communicate directly with high performance.

**Pros:**
- Faster than queues for point-to-point communication
- Simple send/receive interface

**Cons:**
- Only connects two endpoints (use Queue for multiple communicating processes)
- Unidirectional pipes require careful assignment of send/receive ends

---

### 9. Synchronizing Processes
**Concept:** Process Synchronization Primitives

**Explanation:**
The `multiprocessing` module provides synchronization primitives analogous to those in `threading`: Lock, RLock, Event, Condition, Semaphore, and Barrier. These ensure that processes coordinate access to shared resources and communicate state changes correctly. The `Barrier` object is particularly useful for dividing execution into phases — all processes must reach the barrier before any can continue.

**Use:**
Used when multiple processes share resources or must coordinate their execution order.

**Pros:**
- Familiar API matching the `threading` module
- Prevents race conditions and ensures orderly execution

**Cons:**
- Improper use can lead to deadlocks
- Barrier requires all processes to participate or the barrier blocks indefinitely

---

### 10. Managing a State Between Processes
**Concept:** Shared State Management

**Explanation:**
Because each process has its own memory space, sharing state requires explicit mechanisms. The `multiprocessing` module provides `Value` and `Array` for sharing simple data types, and `Manager` objects for sharing more complex structures like lists and dictionaries. Synchronization primitives (Lock, Event, Condition, Semaphore, RLock, Barrier) are used alongside shared state to ensure consistency.

**Use:**
Used when processes need to read from or write to common data structures safely.

**Pros:**
- Enables cooperation between isolated processes
- Manager supports complex data types

**Cons:**
- Shared state introduces synchronization complexity
- Manager-based sharing is slower than direct memory access

---

### 11. Using a Process Pool
**Concept:** Pool of Worker Processes

**Explanation:**
The `Pool` class manages a pool of worker processes to parallelize function execution across multiple inputs (data parallelism). Key methods include `apply()` (blocking), `apply_async()` (non-blocking), `map()` (parallel map), and `map_async()` (non-blocking parallel map). This abstracts process management entirely, letting the developer focus on the task logic.

**Use:**
Used for parallelizing CPU-bound tasks over large datasets by distributing work across a fixed number of processes.

**Pros:**
- Simplifies parallel execution with minimal boilerplate
- Automatically manages worker process lifecycle
- Supports both synchronous and asynchronous execution

**Cons:**
- Less control over individual process behavior
- Pool size must be tuned based on hardware and task type

---

## Summary
Chapter 3 provides a comprehensive guide to process-based parallelism using Python's `multiprocessing` module. By progressing from basic process spawning through naming, background execution, killing, subclassing, IPC via queues and pipes, synchronization, shared state management, and process pooling, the chapter equips developers with the full toolkit needed to build robust, multi-core parallel applications in Python.