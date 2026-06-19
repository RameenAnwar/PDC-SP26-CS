# Chapter 05 – Asynchronous and Concurrent Computing

## Overview

This chapter explores modern asynchronous and concurrent programming techniques in Python using **asyncio** and **concurrent.futures**. The implementations are built around mathematical computations such as **GCD (Greatest Common Divisor)** and **LCM (Least Common Multiple)** to demonstrate non-blocking execution, task scheduling, event loop management, and parallel processing.

The objective is to understand how Python handles asynchronous operations and compare different execution models for computational tasks.

---

## Concepts Implemented

### 1. Asyncio Future and Callbacks

**File:** `asyncio_and_futures038.py`

* Demonstrates the use of `asyncio.Future`.
* Registers callback functions that execute automatically when a task completes.
* Performs mathematical operations asynchronously.
* Avoids blocking the main execution flow.

#### Key Features

* Future objects
* Callback registration
* Non-blocking task completion
* Event-driven execution

---

### 2. Asynchronous Coroutine FSM

**File:** `asyncio_coroutine038.py`

* Implements a Finite State Machine (FSM) using asynchronous coroutines.
* Each state performs a mathematical computation before transitioning to the next state.
* Demonstrates asynchronous state management.

#### Key Features

* Coroutine-based execution
* State transitions
* Asynchronous workflow control
* Event-driven state machines

---

### 3. Event Loop Management

**File:** `asyncio_event_loop038.py`

* Demonstrates low-level event loop operations.
* Uses `call_soon()` and `call_later()` to schedule tasks.
* Executes recursive task chains such as:

```text
Task A → Task B → Task C
```

* Continues execution until a specified timeout is reached.

#### Key Features

* Event loop scheduling
* Delayed execution
* Recursive task chaining
* Timeout handling

---

### 4. Task Manipulation

**File:** `asyncio_task_manipulation038.py`

* Converts coroutines into Task objects.
* Executes multiple mathematical computations concurrently.

Implemented Algorithms:

* Factorial
* Fibonacci Sequence
* Binomial Coefficient

#### Key Features

* Task creation
* Parallel coroutine execution
* Concurrent mathematical processing
* Task scheduling and monitoring

---

### 5. Concurrent Futures Pooling

**File:** `concurrent_futures_pooling038.py`

* Compares different execution strategies for CPU-intensive computations.
* Uses ThreadPoolExecutor and ProcessPoolExecutor.
* Measures execution performance for mathematical operations.

#### Key Features

* Thread Pool execution
* Process Pool execution
* CPU-bound workload analysis
* Performance benchmarking

---

## Project Structure

| File Name                        | Description                            |
| -------------------------------- | -------------------------------------- |
| asyncio_and_futures038.py        | Future Objects and Callbacks           |
| asyncio_coroutine038.py          | Coroutine-based FSM                    |
| asyncio_event_loop038.py         | Event Loop Scheduling                  |
| asyncio_task_manipulation038.py  | Task Management and Concurrency        |
| concurrent_futures_pooling038.py | Thread Pool vs Process Pool Comparison |

---

## Performance Comparison

| Method       | Execution Model                  | Best Use Case              | Performance |
| ------------ | -------------------------------- | -------------------------- | ----------- |
| Sequential   | Single-threaded, blocking        | Simple scripts             | Slowest     |
| Thread Pool  | Shared memory, context switching | I/O-bound operations       | Moderate    |
| Process Pool | Multiple CPU cores               | CPU-intensive computations | Fastest     |

---

## Requirements

### Software Requirements

* Python 3.10+
* Tested on Python 3.14

### Libraries Used

All libraries are included in Python's Standard Library:

```python
import asyncio
import concurrent.futures
import time
import random
```

No external packages are required.

---

## Running the Programs

Execute any file using:

```bash
python filename.py
```

Example:

```bash
python asyncio_coroutine038.py
```

or

```bash
python concurrent_futures_pooling038.py
```

---

## Example Output

```text
Task Started...
Computing LCM...
Result = 36
Callback Executed Successfully

Execution Time: 0.000145 seconds
```

---

## Learning Objectives

After completing this chapter, you will be able to:

* Understand asynchronous programming concepts.
* Work with Futures and Callbacks.
* Create and manage Coroutines.
* Control Python Event Loops.
* Execute multiple Tasks concurrently.
* Compare Sequential, Thread Pool, and Process Pool execution.
* Identify suitable execution models for CPU-bound and I/O-bound workloads.
* Measure and analyze program performance.

---

## Performance Analysis

This chapter enables comparison between:

* Blocking vs Non-Blocking Execution
* Sequential vs Concurrent Processing
* Thread Pool vs Process Pool
* Event-Driven vs Traditional Programming
* CPU-Bound vs I/O-Bound Workloads

The results help determine the most efficient execution strategy for different application types.

---

## Future Enhancements

* Hybrid Asyncio + Multiprocessing Applications
* Distributed Task Scheduling
* Real-Time Monitoring Dashboard
* Network-Based Asynchronous Services
* Large-Scale Mathematical Computation Framework
* Integration with Web APIs and Databases

---

## Author

Huzaifa Alim

Computer Science Student
Usman Institute of Technology (UIT)
