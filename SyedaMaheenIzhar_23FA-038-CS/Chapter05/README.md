# chap 5
# Python Asyncio & Concurrent Futures 

## Overview

This project demonstrates different concurrency models in Python using:

* Asyncio Coroutines
* Asyncio Futures
* Asyncio Tasks
* Event Loop Scheduling
* Thread Pools
* Process Pools

It helps understand asynchronous programming and parallel execution for CPU-bound and I/O-bound tasks.

---

## Files Included

* `asyncio_and_futures.py`
* `asyncio_coroutine.py`
* `asyncio_event_loop.py`
* `asyncio_task_manipulation.py`
* `concurrent_future_pooling.py`

---

## Learning Objectives

* Understand Asyncio event loop
* Work with coroutines and tasks
* Use Futures and callbacks
* Schedule asynchronous execution
* Compare threading vs multiprocessing
* Identify CPU-bound vs I/O-bound workloads

---

## File Details

### 1. asyncio_and_futures.py

**Description:**
Uses Asyncio Futures and callbacks to run coroutines concurrently and return results.

**Run:**

```bash
python asyncio_and_futures.py 10 5
```

**Key Learnings:**

* Futures and result handling
* Callback functions
* Concurrent coroutine execution

---

### 2. asyncio_coroutine.py

**Description:**
Implements a Finite State Machine (FSM) using coroutines.

**Run:**

```bash
python asyncio_coroutine.py
```

**Key Learnings:**

* State transitions using coroutines
* Coroutine chaining
* Workflow simulation

---

### 3. asyncio_event_loop.py

**Description:**
Demonstrates event loop scheduling using `call_soon` and `call_later`.

**Run:**

```bash
python asyncio_event_loop.py
```

**Key Learnings:**

* Event loop basics
* Task scheduling
* Timed execution

---

### 4. asyncio_task_manipulation.py

**Description:**
Runs factorial, fibonacci, and binomial coefficient tasks concurrently.

**Run:**

```bash
python asyncio_task_manipulation.py
```

**Key Learnings:**

* Asyncio Tasks
* Parallel coroutine execution
* Cooperative multitasking

---

### 5. concurrent_future_pooling.py

**Description:**
Compares sequential, thread pool, and process pool execution.

**Run:**

```bash
python concurrent_future_pooling.py
```

**Key Learnings:**

* ThreadPoolExecutor
* ProcessPoolExecutor
* Performance comparison

---

## Advantages

* Better understanding of concurrency models
* Efficient handling of I/O-bound tasks
* True parallelism using multiprocessing
* Performance comparison between approaches

---

## Disadvantages

* Complex compared to sequential code
* Some examples use deprecated asyncio syntax
* Threading limited by Python GIL
* Process pool has higher memory overhead

---

## Notes

These examples use older syntax:

```python
@asyncio.coroutine
yield from
```

Modern Python equivalent:

```python
async def func():
    await asyncio.sleep(1)
```

