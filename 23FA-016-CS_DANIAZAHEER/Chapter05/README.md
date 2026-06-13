# Chapter 5: Asynchronous Programming

## Introduction
Asynchronous programming is a programming paradigm that allows tasks to run concurrently without blocking each other. Unlike traditional sequential programming where one task must finish before the next begins, asynchronous programming lets a program start a task and move on to another while waiting for the first to complete. Python provides the **asyncio** module as its primary tool for writing asynchronous code using **coroutines**, **event loops**, **futures**, and **tasks**. It is especially useful for I/O-bound operations where waiting time can be used productively.

## Advantages
- Better performance for I/O-bound tasks (network, file, database operations)
- Multiple tasks can run concurrently in a single thread
- No need for complex thread synchronization (no race conditions)
- Lightweight compared to thread-based or process-based parallelism
- Clean and readable code using async/await or coroutine syntax

## Disadvantages
- Not suitable for CPU-bound tasks (use multiprocessing instead)
- Harder to debug compared to sequential code
- Older coroutine syntax (`@asyncio.coroutine` and `yield from`) can be confusing
- Blocking calls inside coroutines can freeze the entire event loop
- Requires careful design to avoid performance bottlenecks

## Requirements
```
pip install asyncio
```
All scripts use Python's built-in `asyncio` and `concurrent.futures` modules — no extra installation needed for most scripts.

---

## Topics Covered

---

### 1. Coroutines and Futures (`coroutine_and_future.py`)

#### Description
Demonstrates two coroutines running concurrently — one that counts integers up to N and another that computes the factorial of N. Each coroutine stores its result in a **Future** object. A callback function `got_result()` is triggered automatically when each future completes and prints the result.

#### Key Concepts
- `@asyncio.coroutine` — marks a function as a coroutine
- `yield from asyncio.sleep(4)` — suspends the coroutine without blocking the event loop
- `asyncio.Future()` — object that holds a result to be set in the future
- `future.set_result()` — stores the final result in the future
- `future.add_done_callback()` — registers a function to call when future completes
- `loop.run_until_complete(asyncio.wait(tasks))` — runs all tasks and waits for completion

#### Advantages
- Futures decouple computation from result handling
- Callbacks keep code modular and clean
- Both coroutines run concurrently despite being single-threaded

#### Disadvantages
- Callback-based code can become hard to follow in large programs
- `yield from` syntax is older style (replaced by `await` in Python 3.5+)

#### Use Cases
- Running multiple independent computations concurrently
- Handling async API calls where results arrive at different times
- Background tasks that notify the main program when done

---

### 2. Finite State Machine with Asyncio (`finite_state_machine.py`)

#### Description
Simulates a **Finite State Machine (FSM)** using asyncio coroutines. The program starts at `start_state` and randomly transitions between `state1`, `state2`, `state3`, and `end_state` based on random input values. Each state is implemented as a coroutine that calls the next state using `yield from`.

#### Key Concepts
- Each state is a coroutine that yields control to the next state
- `randint(0, 1)` generates random transitions between states
- `yield from` chains coroutines together
- The FSM terminates when `end_state` is reached
- `loop.run_until_complete()` runs the entire state machine

#### Advantages
- Clean and readable representation of state-based logic
- Easy to add new states or transitions
- Coroutines make the flow naturally sequential despite being async

#### Disadvantages
- `time.sleep()` inside coroutines blocks the event loop (should use `asyncio.sleep()`)
- Deep recursion of states can cause stack issues for large FSMs

#### Use Cases
- Game logic and AI behavior trees
- Protocol handling in network programming
- Workflow engines and process automation
- Parsing and lexical analysis

---

### 3. Event Loop with call_later (`manipulating_task.py`)

#### Description
Demonstrates the asyncio **event loop scheduler** using `call_later()`. Three tasks (A, B, C) are scheduled in a rotating sequence — Task A calls Task B, Task B calls Task C, and Task C calls Task A again. The loop continues for 60 seconds and then stops.

#### Key Concepts
- `loop.call_later(delay, callback)` — schedules a function to run after a delay
- `loop.call_soon(callback)` — schedules a function to run as soon as possible
- `loop.time()` — returns the current time of the event loop
- `loop.run_forever()` — runs the event loop until `loop.stop()` is called
- `loop.stop()` — stops the event loop

#### Advantages
- Fine-grained control over task scheduling
- No need for threads or processes for time-based task rotation
- Lightweight and efficient for scheduling repeated tasks

#### Disadvantages
- `time.sleep()` inside callbacks blocks the loop (should be avoided)
- Hard to manage complex scheduling logic manually
- Not suitable for tasks requiring precise timing

#### Use Cases
- Polling systems that check status at regular intervals
- Rotating task schedulers in server applications
- Game loops and animation timers
- Heartbeat or watchdog mechanisms

---

### 4. Asyncio Tasks — Parallel Math Functions (`asyncio_task.py`)

#### Description
Uses `asyncio.Task` to run three math functions — **factorial**, **fibonacci**, and **binomial coefficient** — concurrently. Each task yields control using `asyncio.sleep(1)` between iterations, allowing the other tasks to make progress. All three tasks are collected in a list and run together using `asyncio.wait()`.

#### Key Concepts
- `asyncio.Task(coroutine)` — wraps a coroutine into a scheduled task
- `yield from asyncio.sleep(1)` — yields control to other tasks
- `asyncio.wait(task_list)` — waits for all tasks in the list to complete
- Tasks are interleaved, not truly parallel (single-threaded concurrency)

#### Advantages
- Multiple computations interleave efficiently in a single thread
- `asyncio.sleep()` correctly yields control without blocking
- Clean and simple way to run multiple coroutines together

#### Disadvantages
- Still single-threaded — no true parallelism for CPU-bound work
- All tasks share the same event loop so one blocking call affects all
- Older `asyncio.Task` syntax (modern code uses `asyncio.create_task()`)

#### Use Cases
- Running multiple independent calculations concurrently
- Handling multiple client requests in an async server
- Interleaving I/O-bound operations efficiently

---

### 5. Thread Pool and Process Pool Executor (`pool.py`)

#### Description
Compares three execution modes for a CPU-bound counting task across 10 numbers — **sequential**, **thread pool**, and **process pool**. Uses `concurrent.futures.ThreadPoolExecutor` and `ProcessPoolExecutor` with 5 workers each. Measures and prints execution time for all three approaches.

#### Key Concepts
- `concurrent.futures.ThreadPoolExecutor(max_workers=5)` — pool of threads
- `concurrent.futures.ProcessPoolExecutor(max_workers=5)` — pool of processes
- `executor.submit(fn, arg)` — submits a task to the pool
- Thread pool shares memory but is limited by the GIL for CPU tasks
- Process pool bypasses the GIL and achieves true parallelism

#### Advantages
- Easy to switch between thread and process pools with same API
- Process pool gives real speedup for CPU-bound tasks
- `with` statement automatically manages pool lifecycle

#### Disadvantages
- Thread pool limited by Python's GIL for CPU-bound tasks
- Process pool has higher overhead due to process creation
- `time.clock()` is deprecated in Python 3.8+ (use `time.perf_counter()`)

#### Use Cases
- Batch processing large datasets in parallel
- Running independent CPU-heavy computations simultaneously
- Web scraping or API calls using thread pools
- Image or video processing pipelines using process pools

---
