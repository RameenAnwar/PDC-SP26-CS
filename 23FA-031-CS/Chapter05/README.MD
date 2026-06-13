# Python Concurrency and Async Programming Examples

This repository demonstrates different approaches to concurrency and asynchronous programming in Python using:

- `asyncio`
- Coroutines
- Event Loops
- Futures
- Tasks
- Thread Pools
- Process Pools

---

# Table of Contents

1. Introduction
2. Asyncio Overview
3. Event Loop
4. Coroutines
5. Futures
6. Tasks
7. Thread Pool vs Process Pool
8. Files Description
   - asyncio_and_futures.py
   - asyncio_coroutine.py
   - asyncio_event_loop.py
   - asyncio_task_manipulation.py
   - concurrent_futures_pooling.py

---

# 1. Introduction

Python provides several ways to perform multiple operations concurrently:

### Sequential Execution

Tasks execute one after another.

```
Task A
↓
Task B
↓
Task C
```

---

### Concurrent Execution

Tasks overlap in execution.

```
Task A ─┐
Task B ─┼── Running together
Task C ─┘
```

Concurrency improves performance and resource utilization.

Python supports concurrency using:

- Asyncio
- Threads
- Processes

---

# 2. Asyncio Overview

`asyncio` is Python's library for writing asynchronous programs.

It is useful for:

- Network programming
- Web servers
- File operations
- Simulations
- Cooperative multitasking

Main Components:

```
Event Loop
    ↓
Coroutines
    ↓
Tasks
    ↓
Futures
```

---

# 3. Event Loop

The Event Loop is the heart of asyncio.

It:

- schedules tasks
- executes coroutines
- handles callbacks
- manages asynchronous operations

Diagram:

```
            Event Loop
                 |
     -------------------------
     |           |           |
 Coroutine1  Coroutine2  Coroutine3
```

Functions:

### Get Event Loop

```python
loop = asyncio.get_event_loop()
```

---

### Run Until Complete

```python
loop.run_until_complete(task)
```

Runs until all tasks finish.

---

### Run Forever

```python
loop.run_forever()
```

Runs continuously until stopped.

---

### Stop Loop

```python
loop.stop()
```

Stops execution.

---

### Close Loop

```python
loop.close()
```

Releases resources.

---

# 4. Coroutines

A coroutine is a special function that can pause and resume execution.

Old syntax:

```python
@asyncio.coroutine
def my_coroutine():
    yield from asyncio.sleep(1)
```

Modern syntax:

```python
async def my_coroutine():
    await asyncio.sleep(1)
```

Coroutines enable cooperative multitasking.

---

# 5. Futures

A Future represents a result that will be available later.

Example:

```python
future = asyncio.Future()
```

Initially:

```
Pending
```

After completion:

```
Done
```

Result retrieved by:

```python
future.result()
```

States:

```
Pending
Running
Completed
Cancelled
```

---

# 6. Tasks

Task = Wrapped Coroutine

```python
task = asyncio.Task(coroutine())
```

Tasks run concurrently inside the event loop.

Example:

```
Task 1
Task 2
Task 3

↓
Run together
```

---

# 7. Thread Pool vs Process Pool

### ThreadPoolExecutor

Uses threads.

Good for:

- I/O operations
- Network requests
- File reading

```
Thread 1
Thread 2
Thread 3
```

---

### ProcessPoolExecutor

Uses separate processes.

Good for:

- CPU-intensive computations
- Mathematical calculations

```
Process 1
Process 2
Process 3
```

---

# File 1 : asyncio_and_futures.py

## Purpose

Demonstrates:

- Coroutines
- Futures
- Callbacks
- Event loop

---

## first_coroutine()

```python
def first_coroutine(future, num):
```

Calculates:

```
1 + 1 + 1 + ... + 1
```

(counter)

Example:

```
num = 5

count = 5
```

Sleeps for 4 seconds:

```python
yield from asyncio.sleep(4)
```

Stores result:

```python
future.set_result(...)
```

---

## second_coroutine()

Calculates factorial.

Example:

```
5!

=5×4×3×2×1
=120
```

Stores result inside another future.

---

## Future Objects

```python
future1 = asyncio.Future()
future2 = asyncio.Future()
```

These are placeholders for results.

---

## Callback Function

```python
def got_result(future):
    print(future.result())
```

Executed automatically when a future completes.

Registered by:

```python
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)
```

---

## Task Flow

```
Event Loop
    |
    +---- first_coroutine
    |
    +---- second_coroutine
            |
            ↓
        Future Completed
            |
            ↓
         Callback
            |
            ↓
        Print Result
```

---

# File 2 : asyncio_coroutine.py

## Purpose

Simulates a Finite State Machine (FSM).

States:

```
Start State
State1
State2
State3
End State
```

---

## Random Transitions

```python
input_value = randint(0,1)
```

Randomly chooses:

```
0
or
1
```

---

## State Diagram

```
              Start
             /    \
            /      \
       State2      State1
         |            |
         ↓            ↓
      State1 ←→ State2
          \      /
           \    /
            State3
               |
          0 ----+---- 1
               |
            End State
```

---

## start_state()

Beginning of the FSM.

Depending on random value:

```python
0 → state2()

1 → state1()
```

---

## state1()

May transition to:

- state2()
- state3()

using:

```python
yield from state2()
```

or

```python
yield from state3()
```

---

## state2()

Transitions to:

- state1()
- state3()

---

## state3()

Transitions to:

- state1()
- end_state()

---

## end_state()

Stops the computation.

Returns:

```python
End State
```

---

## Coroutine Chaining

```
start_state()
      |
      ↓
state1()
      |
      ↓
state2()
      |
      ↓
state3()
      |
      ↓
end_state()
```

---

# File 3 : asyncio_event_loop.py

## Purpose

Demonstrates low-level event loop scheduling.

---

Tasks:

```
task_A
task_B
task_C
```

These repeatedly call each other.

---

## call_soon()

```python
loop.call_soon(task_A, end_loop, loop)
```

Schedules immediate execution.

---

## call_later()

```python
loop.call_later(1, task_B, end_time, loop)
```

Schedules execution after one second.

---

## Circular Scheduling

```
task_A
   ↓
task_B
   ↓
task_C
   ↓
task_A
```

Continues until:

```python
loop.stop()
```

---

## run_forever()

```python
loop.run_forever()
```

Runs continuously.

---

## Overall Flow

```
Event Loop
     |
task_A
     |
task_B
     |
task_C
     |
task_A
     |
task_B
...
```

until 60 seconds expire.

---

# File 4 : asyncio_task_manipulation.py

## Purpose

Runs three mathematical computations concurrently.

---

Tasks:

1. Factorial
2. Fibonacci
3. Binomial coefficient

---

## factorial()

Example:

```
5!

=120
```

Each iteration:

```python
yield from asyncio.sleep(1)
```

Allows other tasks to execute.

---

## fibonacci()

Sequence:

```
0
1
1
2
3
5
8
13
21
34
```

Generated using:

```python
a,b = b,a+b
```

---

## binomial_coefficient()

Formula:

```
nCr = n! / (r!(n-r)!)
```

Example:

```
20C10
```

---

## Creating Tasks

```python
asyncio.Task(factorial(10))
```

Task objects:

```python
task_list = [
Task1,
Task2,
Task3
]
```

---

## asyncio.wait()

```python
loop.run_until_complete(asyncio.wait(task_list))
```

Waits until all tasks finish.

---

## Execution Pattern

```
Factorial
Fibonacci
Binomial

↓
Run simultaneously

↓
Results
```

---

# File 5 : concurrent_futures_pooling.py

## Purpose

Compares:

1. Sequential execution
2. Thread pool execution
3. Process pool execution

---

## count()

Heavy CPU computation:

```python
for i in range(10000000):
```

Consumes processor time.

---

## evaluate()

Calls:

```python
count(item)
```

Prints:

```python
Item 5, result ...
```

---

# Sequential Execution

```python
for item in number_list:
    evaluate(item)
```

Execution:

```
1
2
3
4
5
...
```

One after another.

---

# Thread Pool Execution

```python
ThreadPoolExecutor(max_workers=5)
```

Creates:

```
Thread1
Thread2
Thread3
Thread4
Thread5
```

Tasks are distributed among threads.

Suitable for:

- Network requests
- APIs
- Databases
- File operations

---

# Process Pool Execution

```python
ProcessPoolExecutor(max_workers=5)
```

Creates independent processes:

```
Process1
Process2
Process3
Process4
Process5
```

Best for:

- CPU-intensive work
- Mathematical calculations
- Machine learning
- Image processing

---

# Comparison

| Feature         | Sequential | Thread Pool | Process Pool |
| --------------- | ---------- | ----------- | ------------ |
| Runs One by One | Yes        | No          | No           |
| Uses Threads    | No         | Yes         | No           |
| Uses Processes  | No         | No          | Yes          |
| CPU Intensive   | Slow       | Medium      | Fast         |
| I/O Operations  | Slow       | Fast        | Fast         |
| Memory Usage    | Low        | Medium      | High         |

---

# Important Concepts Covered

### Event Loop

Schedules and manages asynchronous execution.

---

### Coroutines

Functions that pause and resume.

---

### yield from

Transfers execution to another coroutine.

---

### sleep()

Temporarily suspends a coroutine.

---

### Future

Represents a value available later.

---

### Callback

Executed automatically after completion.

---

### Task

Wrapper around a coroutine.

---

### wait()

Waits for all tasks to finish.

---

### Thread Pool

Concurrency using threads.

---

### Process Pool

Parallelism using multiple processes.

---

# Overall Architecture

```
                    Python Concurrency
                           |
        -------------------------------------------------
        |                     |                         |
      Asyncio            Thread Pool               Process Pool
        |                     |                         |
   ----------------      Multiple Threads        Multiple Processes
   |       |      |
Coroutines Tasks Futures
        |
    Event Loop
```

This repository provides a complete introduction to Python concurrency, asynchronous programming, and parallel execution mechanisms.
