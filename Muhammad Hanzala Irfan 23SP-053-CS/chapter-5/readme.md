# Chapter 5 – Asynchronous Programming

## Overview
This chapter introduces the asynchronous execution model as a third paradigm alongside sequential and parallel programming. Unlike multithreaded programming where the OS controls context switching, the asynchronous model gives the developer explicit control over task execution using a single thread. Python's `asyncio` module (introduced in Python 3.4) and the `concurrent.futures` module are the primary tools explored, using coroutines, futures, tasks, and event loops.

---

## Topics Covered

### 1. Using the concurrent.futures Python Module
**Concept:** Thread & Process Pool Abstraction

**Explanation:**
The `concurrent.futures` module provides a high-level abstraction over threads and processes by modelling them as asynchronous functions. It is built around two core classes:

- `concurrent.futures.Executor` — an abstract class providing methods to execute calls asynchronously.
- `concurrent.futures.Future` — encapsulates the asynchronous execution of a callable and holds its result when ready.

Key methods include `submit(function, argument)` for scheduling a call, `map(function, argument)` for asynchronous mapping, and `shutdown(Wait=True)` to release resources. The two concrete subclasses are `ThreadPoolExecutor` and `ProcessPoolExecutor`, which pool resources to avoid the overhead of repeatedly creating threads or processes.

**Use:**
Used to run I/O-bound tasks concurrently (via `ThreadPoolExecutor`) or CPU-bound tasks in parallel (via `ProcessPoolExecutor`) without manual thread or process management.

**Pros:**
- High-level, clean API hiding thread/process complexity
- Resource pooling reduces creation overhead
- Future objects allow easy result retrieval

**Cons:**
- Less fine-grained control than raw `threading` or `multiprocessing`
- Not integrated with the `asyncio` event loop natively

---

### 2. Managing the Event Loop with asyncio
**Concept:** Event Loop

**Explanation:**
The `asyncio` module allows one event loop per process. The event loop is the central component that manages and distributes the execution of tasks, coroutines, and I/O callbacks. It operates in a continuous cycle:

```
while (1):
    events = getEvents()
    for e in events:
        processEvent(e)
```

Key components of `asyncio` include:
- **Event loop** — registers and switches control between tasks.
- **Coroutines** — suspendable functions that yield control back to the loop.
- **Futures** — objects representing computations not yet complete.
- **Tasks** — subclass of asyncio used to wrap and schedule coroutines.

An event source generates events; an event handler processes them. The loop keeps track of all pending events and dispatches them when the main thread is free.

**Use:**
Used as the foundation of any `asyncio`-based application — the event loop must be started before coroutines or tasks can execute.

**Pros:**
- Single-threaded, avoiding concurrency bugs like race conditions
- Explicit control over execution order
- Efficient for high-concurrency I/O-bound workloads

**Cons:**
- One blocking call can stall the entire loop
- More complex programming model compared to threading
- Only one event loop per process by default

---

### 3. Handling Coroutines with asyncio
**Concept:** Coroutines

**Explanation:**
A coroutine is a generalization of the subroutine concept. Unlike subroutines which are called and return, coroutines can suspend their execution mid-way, yield control back to the event loop, and resume from where they left off once their awaited operation completes. Coroutines are defined using the `@asyncio.coroutine` decorator (or `async def` in newer Python versions) and use `yield from` (or `await`) to pause execution.

Key properties of coroutines:
- Multiple entry points that can yield multiple times.
- Can transfer execution to any other coroutine.
- The event loop interleaves their execution, keeping track of state.

This allows a pool of coroutines to form a pipeline without a supervising function ordering them explicitly.

**Use:**
Used to write non-blocking code that handles I/O-bound operations (network calls, file reads) efficiently within a single thread.

**Pros:**
- No data race conditions (single-threaded)
- Highly readable and maintainable concurrent code
- Efficient for large numbers of concurrent I/O tasks

**Cons:**
- Does not provide true parallelism for CPU-bound tasks
- Requires consistent use of `await`/`yield from` throughout the call chain
- Mixing blocking and async code can stall the loop

---

### 4. Manipulating Tasks with asyncio
**Concept:** asyncio Tasks

**Explanation:**
The `asyncio.Task` class wraps a coroutine and schedules it to run on the event loop. When a coroutine is wrapped in a task, it is automatically connected to the event loop and begins executing when the loop starts. Tasks enable multiple coroutines to run concurrently on the same event loop.

Key behavior:
- A task suspends the wrapped coroutine when it encounters a `yield from future` and resumes it when the future completes.
- The event loop runs one task at a time, but tasks in different threads can use separate event loops.
- While one task waits on a future, the event loop picks up and runs another task.

**Use:**
Used to schedule and manage multiple concurrently running coroutines — for example, computing factorial, Fibonacci, and binomial coefficients simultaneously.

**Pros:**
- Enables concurrent coroutine execution with minimal boilerplate
- Automatic scheduling by the event loop
- Clean cancellation and status checking via `cancel()` and `done()`

**Cons:**
- Still single-threaded — no CPU parallelism
- Task exceptions must be explicitly handled or they are silently lost
- Debugging concurrent tasks can be non-trivial

---

### 5. Dealing with asyncio and Futures
**Concept:** asyncio Futures

**Explanation:**
`asyncio.Future` represents a result (or exception) that is not yet available — an abstraction of something yet to be computed. Callbacks registered on a future object are invoked automatically when the result becomes ready. Key methods include:

- `cancel()` — cancels the future and schedules its callbacks.
- `result()` — returns the future's result when done.
- `exception()` — returns any exception set on the future.
- `add_done_callback(fn)` — registers a callback to run on completion.
- `set_result(result)` — marks the future as done and stores the result.
- `set_exception(exception)` — marks the future as done with an error.

While similar to `concurrent.futures.Future`, `asyncio.Future` is tightly integrated with the event loop and coroutine system.

**Use:**
Used to represent and manage pending results in async workflows, particularly when coroutines need to signal completion or errors to other parts of the program — for example, computing the sum of N integers and the factorial of N concurrently.

**Pros:**
- Integrates naturally with the asyncio event loop and coroutines
- Callback-based model decouples computation from result handling
- Supports both result and exception propagation

**Cons:**
- More verbose than simple `await` for straightforward tasks
- Futures are low-level; prefer tasks or `await` for most use cases
- Not interchangeable with `concurrent.futures.Future`

---

## Summary
Chapter 5 builds a comprehensive understanding of asynchronous programming in Python. Starting with the `concurrent.futures` module for pooled thread/process abstraction, it transitions into the `asyncio` ecosystem — covering the event loop, coroutines, tasks, and futures. Together these tools enable writing highly concurrent, non-blocking applications using a single-threaded execution model, making Python well-suited for I/O-intensive workloads such as network servers and web scrapers.