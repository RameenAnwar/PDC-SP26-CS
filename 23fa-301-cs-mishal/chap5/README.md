# Chapter 5: Asynchronous Programming – A Detailed Beginner's Guide

This guide explains the fundamentals of asynchronous programming, how it differs from other execution models (sequential, parallel, multithreaded), and how to use Python’s main async tools: `concurrent.futures` and `asyncio`.

---

## 1. Three Core Execution Models – How Code Runs

| Model            | How It Works                                                                                                | Best For                                      | Drawback                                     |
| :--------------- | :---------------------------------------------------------------------------------------------------------- | :-------------------------------------------- | :------------------------------------------- |
| **Sequential**   | One task after another. Each step waits for the previous to finish.                                         | Simple scripts, batch processing.             | Wastes time if tasks involve waiting (I/O).  |
| **Parallel**     | Multiple tasks run simultaneously on different CPU cores.                                                   | Heavy computation, number crunching.          | High resource usage, complex to synchronize. |
| **Asynchronous** | Single thread, but tasks voluntarily pause during waiting periods. The event loop switches to another task. | I/O‑bound programs, high‑concurrency servers. | Requires careful coding (`async`/`await`).   |

---

## 2. Blocking vs. Non‑Blocking – The Critical Distinction

### Blocking (Synchronous)

- The caller **waits** idly until the operation finishes.
- The thread cannot do anything else during that time.
- **Example:** `time.sleep(5)` – the whole program freezes for 5 seconds.

### Non‑Blocking (Asynchronous)

- The caller **starts** the operation and **immediately** returns control to the event loop.
- When the operation completes, the loop **resumes** the task.
- **Example:** `await asyncio.sleep(5)` – the task pauses, other tasks run.

#### Comparison Table

| Feature             | Blocking                                 | Non‑Blocking                         |
| :------------------ | :--------------------------------------- | :----------------------------------- |
| **Thread state**    | Idle, waiting                            | Active, can switch to another task   |
| **Resource use**    | Wastes CPU cycles (spinning or sleeping) | Efficient – no idle waiting          |
| **Code complexity** | Simple, linear                           | Requires callbacks or `async/await`  |
| **Scalability**     | Poor for many concurrent operations      | Excellent (thousands of connections) |

---

## 3. Asynchronous vs. Multithreaded Programming – Detailed Comparison

| Aspect                   | Multithreading                                                 | Asynchronous                                                           |
| :----------------------- | :------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Underlying mechanism** | OS‑level threads. The OS scheduler decides which thread runs.  | Single thread + event loop. The programmer decides when to switch.     |
| **Switching overhead**   | Relatively high (thread context switch).                       | Very low (function call pause/resume).                                 |
| **Data sharing**         | Requires locks, semaphores, mutexes – risk of race conditions. | No locks needed – only one thread runs at a time.                      |
| **Memory footprint**     | Each thread has its own stack (typically 1‑8 MB).              | One stack for all coroutines (tiny overhead).                          |
| **CPU‑bound tasks**      | Can use multiple cores for true parallelism.                   | Cannot – single thread limits CPU utilisation (use processes instead). |
| **I/O‑bound tasks**      | Works but often overkill; thread creation cost high.           | Ideal – lightweight and efficient.                                     |
| **Debugging**            | Hard – race conditions, deadlocks, unpredictable ordering.     | Easier – deterministic switching at `await` points.                    |

---

## 4. Advantages of the Asynchronous Model

- **Fine‑grained control** over when tasks pause and resume.
- **Optimises resource usage** – avoids creating thousands of threads.
- **Ideal for event‑driven programs**:
  - GUI applications (keep interface responsive).
  - Network servers (handle many clients with one thread).
  - I/O‑bound tasks (database queries, file reads, API calls).
- **Lower memory overhead** – can handle 10,000+ concurrent connections with ~50 MB RAM (compared to threads needing GBs).
- **No race conditions** – because only one coroutine runs at a time (no need for locks).

---

## 5. Real‑World Example: Web Server + Database

**Scenario:** A web server receives many client requests, each requiring a database query.

### Asynchronous Approach (e.g., using `asyncio`)

1. **Single async flow** – The main thread uses an event loop. It sends a DB query and immediately moves to handle other clients (non‑blocking).
2. **Offloading** – While the main thread manages tasks, the **I/O subsystem** (OS, network card, disk controller) handles the actual database operations, possibly using other cores.

### Offloading in Action – Two Levels

| Level                      | Who Offloads?                     | What Task?                            | Where?                                                 |
| :------------------------- | :-------------------------------- | :------------------------------------ | :----------------------------------------------------- |
| **Application → Database** | The web server (async event loop) | Sending SQL query, waiting for result | Between application and database server                |
| **Database → OS**          | The database engine               | Reading/writing disk blocks           | Inside the database system (using OS asynchronous I/O) |

This double offloading keeps both the web server and the database highly responsive.

---

## 6. Python Tools for Asynchronous Programming

### Tool 1: `concurrent.futures` – Simple Async for Existing Code

**Purpose:** Run existing synchronous functions in threads or processes without rewriting them as coroutines.

#### Key Classes

| Class                 | Use Case                                                 |
| :-------------------- | :------------------------------------------------------- |
| `ThreadPoolExecutor`  | I/O‑bound tasks (network, files, databases)              |
| `ProcessPoolExecutor` | CPU‑heavy tasks (math, image processing)                 |
| `Future`              | A placeholder for a result that will be available later. |

#### Important Methods

| Method                | Description                                                          |
| :-------------------- | :------------------------------------------------------------------- |
| `submit(func, arg)`   | Schedules `func(arg)` to run. Returns a `Future`.                    |
| `map(func, iterable)` | Runs `func` on every item of the iterable, returns results in order. |
| `shutdown()`          | Cleans up the executor (called automatically when using `with`).     |

#### Why Use a Pool?

- **Reuses** existing threads/processes (reduces creation overhead).
- **Limits** resource consumption (prevents creating too many).
- **Automatically manages** lifecycle (start/stop) and synchronisation.

#### Quick Decision Guide

| Task Type                               | Recommended Executor       |
| :-------------------------------------- | :------------------------- |
| Database query, file read, network call | `ThreadPoolExecutor`       |
| Heavy calculation (e.g., 10M loop)      | `ProcessPoolExecutor`      |
| Mixed I/O + CPU                         | Use two pools or `asyncio` |

#### `Future` Object – Useful Methods

```python
future.done()       # Returns True if task finished (successfully or with error)
future.result()     # Blocks until done, then returns the value (or raises exception)
future.cancel()     # Attempt to cancel (only works if task hasn't started)
future.running()    # True if task is currently executing
```
