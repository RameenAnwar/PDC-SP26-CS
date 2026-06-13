# Chapter 5: Asynchronous Programming

---

## 1. asyncio_and_futures.py

### What I learned:

I learned how to use asyncio.Future objects as placeholders for results that will be computed asynchronously. This script demonstrates how to pass a future into a coroutine, set its result when a long-running math task completes (like summing integers or computing a factorial), and trigger a callback function (got_result) the moment that future resolves.

### How to execute:

Run in cmd: python asyncio_and_futures.py 100000 10 (where 100000 and 10 are the integer inputs for the first and second coroutines, respectively).

### Use cases:

Tracking the completion state of background tasks and decoupling the code that executes a task from the code that processes its final result.

### Requirements for execution:

The asyncio built-in library and passing two command-line arguments for the mathematical calculations.

### Advantages:

Provides a clean callback mechanism (add_done_callback) to execute logic instantly upon future completion without active polling.

### Disadvantages:

Relies on legacy generator-based coroutine syntax (@asyncio.coroutine and yield from), which is deprecated in modern Python in favor of async/await.

---

## 2. asyncio_coroutine.py

### What I learned:

I learned how to simulate a Finite State Machine (FSM) using asynchronous coroutines. The script shows how execution can transition dynamically from one state function to another based on random runtime conditions, passing control back and forth asynchronously using yield from.

### How to execute:

Run in cmd: python asyncio_coroutine.py to watch the state machine evaluate random inputs and step through states until it hits the end state.

### Use cases:

Modeling complex operational workflows, network protocol state machines, or turn-based game logic where transitions depend on asynchronous events.

### Requirements for execution:

The asyncio, time, and random libraries utilizing the loop.run_until_complete() method to kick off the initial state.

### Advantages:

Makes complex, multi-state transition logic highly readable and modular by mapping each state to its own isolated function.

### Disadvantages:

The use of synchronous time.sleep(1) inside the coroutines blocks the entire event loop, defeating the primary purpose of asynchronous concurrency during those delays.

---

## 3. asyncio_event_loop.py

### What I learned:

I learned how to interact directly with the asyncio event loop's internal clock and scheduling mechanics. This script demonstrates how to schedule functions to run sequentially in the future using loop.call_soon and loop.call_later, creating a cooperative execution loop between three separate tasks until a global timeout is reached.

### How to execute:

Run in cmd: python asyncio_event_loop.py and watch task_A, task_B, and task_C hand off execution to one another over a 60-second window.

### Use cases:

Implementing polling loops, heartbeat signals for microservices, or scheduling recurring background maintenance tasks.

### Requirements for execution:

The loop.call_later() and loop.time() methods to dynamically track and schedule tasks relative to the event loop's timeline.

### Advantages:

Provides precision control over when a non-coroutine function gets injected into the event loop queue without needing full coroutine definitions.

### Disadvantages:

Mismanaging the conditional boundaries can easily lead to infinite loops or unexpected application halts if loop.stop() isn't safely triggered.

---

## 4. asyncio_task_manipulation.py

### What I learned:

I learned how to wrap coroutines into asyncio.Task objects to schedule and execute multiple operations concurrently. This script showcases running three heavy mathematical operations (factorial, Fibonacci sequence, and binomial coefficient) in parallel, allowing them to yield control back to the loop via asyncio.sleep(1).

### How to execute:

Run in cmd: python asyncio_task_manipulation.py to see the step-by-step computation logs interleaved as the tasks run in parallel.

### Use cases:

Running independent mathematical computations or I/O bound requests simultaneously instead of waiting for each to finish sequentially.

### Requirements for execution:

The asyncio.Task() wrapper and asyncio.wait() to group and await the execution of the entire task list.

### Advantages:

Maximizes CPU/resource efficiency during I/O delays by letting other tasks process numbers while one is paused/sleeping.

### Disadvantages:

Because Python's standard asyncio runs on a single thread, true multi-core parallel execution is not achieved; tasks are interleaved, not executed simultaneously on separate CPU cores.

---

## 5. concurrent_futures_pooling.py

### What I learned:

I learned how to compare and leverage different execution paradigms using Python’s concurrent.futures module. This script measures and contrasts the execution speeds of a heavy mathematical calculation across three distinct modes: Sequential execution, Thread Pools (ThreadPoolExecutor), and Process Pools (ProcessPoolExecutor).

### How to execute:

Run in cmd: python concurrent_futures_pooling.py to compare the completion times for all three execution strategies.

### Use cases:

Benchmarking applications to choose between multi-threading (best for I/O-bound tasks) and multi-processing (best for CPU-bound calculations like heavy math).

### Requirements for execution:

The concurrent.futures library and using with context managers to cleanly manage executor worker pools.

### Advantages:

Offers a high-level, unified API (executor.submit) to switch from sequential code to parallel execution with minimal changes to core logic.

### Disadvantages:

ThreadPoolExecutor struggles to optimize heavy CPU-bound tasks due to Python's Global Interpreter Lock (GIL), making ProcessPoolExecutor necessary despite its higher memory overhead.