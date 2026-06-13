# Chapter 5 - Asyncio and Concurrency in Python

This chapter covers asynchronous programming, event loops, coroutines, and concurrent execution techniques in Python.

---

## 📌 Topics Covered

### 1. asyncio_and_futures
This topic explains how **Futures** work in asyncio.  
Futures represent results that will be available in the future after asynchronous execution completes.

---

### 2. asyncio_coroutine
This topic introduces **coroutines** using `asyncio.coroutine` and `yield from`.  
Coroutines allow functions to pause and resume execution, enabling non-blocking behavior.

---

### 3. asyncio_event_loop
The **event loop** is the core of asyncio.  
It manages and executes asynchronous tasks, callbacks, and coroutines.

Key functions:
- `get_event_loop()`
- `run_until_complete()`
- `run_forever()`
- `close()`

---

### 4. asyncio_task_manipulation
This topic demonstrates how to create and manage **asyncio Tasks**.  
Tasks allow multiple coroutines to run concurrently.

Features:
- Task scheduling
- Parallel execution
- Callback handling

---

### 5. concurrent_futures_pooling
This topic covers **ThreadPoolExecutor** and **ProcessPoolExecutor**.

It compares:
- Sequential Execution (slow)
- Thread Pool Execution (moderate speed improvement)
- Process Pool Execution (fastest for CPU-heavy tasks)

