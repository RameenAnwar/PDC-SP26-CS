# Chapter 05 – Asynchronous Programming

## 1) asyncio_and_futures.py
This file demonstrates asynchronous programming using coroutines and Futures, where two tasks run concurrently and store their results when done.

- **Future**: An object that holds the result of an async operation that hasn't completed yet.
- **Coroutine**: A function defined with `@asyncio.coroutine` that can pause and resume execution.
- `first_coroutine` counts integers from 1 to N and stores the result in a Future.
- `second_coroutine` computes the factorial of N and stores the result in a Future.
- `yield from asyncio.sleep(4)` pauses each coroutine for 4 seconds without blocking others.
- `future.add_done_callback(got_result)` automatically calls `got_result()` when a Future completes.
- Both tasks are run together using `asyncio.wait(tasks)` inside the event loop.

**Advantages:**
- Both coroutines run concurrently, saving time compared to sequential execution.
- Futures allow result retrieval and callback attachment cleanly.
- Non-blocking sleep allows other coroutines to proceed during the wait.

**Disadvantages:**
- `@asyncio.coroutine` and `yield from` are older syntax, replaced by `async/await` in modern Python.
- Harder to read and debug than regular functions.
- Futures require explicit result setting which adds boilerplate.

**Time behavior:**
- Both coroutines sleep 4 seconds simultaneously, so total time ≈ 4 seconds, not 8.
- Concurrent execution gives a clear speedup over sequential.


## 2) asyncio_coroutine.py
This file demonstrates a Finite State Machine (FSM) simulation using asyncio coroutines, where the program moves between states based on random values.

- **Finite State Machine**: A model where a program transitions between a fixed set of states based on input.
- `start_state()` is the entry point, which randomly transitions to `state1` or `state2`.
- Each state generates a random value (0 or 1) to decide the next state transition.
- `yield from` is used to call the next state coroutine and wait for its result.
- The machine keeps transitioning until it reaches `end_state`, which stops computation.
- Each state returns a string describing its transition, building a trace of the full path taken.

**Advantages:**
- Clean way to model state-based logic using coroutines.
- Each state is isolated and easy to modify independently.
- `yield from` makes the flow readable and sequential-looking despite being async.

**Disadvantages:**
- Uses `time.sleep()` instead of `asyncio.sleep()`, which blocks the event loop , not truly async.
- Random transitions make the execution path unpredictable.
- Deep recursion between states could cause issues for large machines.

**Time behavior:**
- Each state sleeps for 1 second, so total time depends on how many transitions occur.
- Non-deterministic i.e. each run may take a different number of steps.


## 3) asyncio_event_loop.py
This file demonstrates manual control of the asyncio event loop, scheduling tasks to run one after another using `call_later`.

- **Event Loop**: The core of asyncio — it schedules and runs async tasks and callbacks.
- `call_later(delay, callback)` schedules a function to be called after a given number of seconds.
- `task_A`, `task_B`, and `task_C` are plain functions (not coroutines) that chain into each other.
- Each task checks if there is still time left before `end_time`; if yes, it schedules the next task.
- If time runs out, it calls `loop.stop()` to end the event loop.
- The loop runs for 60 seconds total using `loop.run_forever()`.

**Advantages:**
- Shows direct control over the event loop and scheduling.
- `call_later` allows precise timing of task execution.
- Useful for time-based or periodic task scheduling.

**Disadvantages:**
- Uses `time.sleep()` which blocks the event loop, defeats the purpose of async.
- Tasks are plain functions, not coroutines, so no actual async benefits here.
- Harder to manage as the number of tasks grows.

**Time behavior:**
- Loop runs for exactly 60 seconds then stops.
- Each task introduces a random 0–5 second delay before the next one is scheduled.


## 4) asyncio_task_manipulation.py
This file demonstrates running multiple coroutines in parallel using `asyncio.Task`, computing factorial, fibonacci, and binomial coefficient concurrently.

- **asyncio.Task**: Wraps a coroutine and schedules it to run on the event loop immediately.
- `factorial(10)` computes 10! by multiplying step by step, yielding after each step.
- `fibonacci(10)` computes the 10th Fibonacci number iteratively, yielding after each step.
- `binomial_coefficient(20, 10)` computes C(20,10) step by step, yielding after each step.
- `yield from asyncio.sleep(1)` inside each coroutine allows the others to run during the pause.
- All three tasks run concurrently using `asyncio.wait(task_list)`.

**Advantages:**
- True concurrent execution of multiple math computations.
- `asyncio.sleep()` correctly yields control unlike `time.sleep()`.
- Clean structure, each computation is self-contained in its own coroutine.

**Disadvantages:**
- Each step sleeps 1 second, so large inputs mean long total execution time.
- `asyncio.Task` is older syntax as modern Python uses `asyncio.create_task()`.
- CPU-bound work here gets no real speedup from async (async is better for I/O-bound).

**Time behavior:**
- All three tasks interleave their steps during each 1-second sleep.
- Total time ≈ max number of iterations × 1 second, not the sum of all three.


## 5) concurrent_futures_pooling.py
This file demonstrates and compares three execution methods: sequential, thread pool, and process pool, measuring time for each.

- **concurrent.futures**: A high-level module for running tasks in parallel using threads or processes.
- `count(number)` runs a loop 10 million times and returns the result simulating CPU-heavy work.
- `evaluate(item)` calls `count()` and prints the result for each item.
- **Sequential**: Runs `evaluate()` for each of 10 numbers one at a time.
- **ThreadPoolExecutor(max_workers=5)**: Runs tasks using 5 threads simultaneously.
- **ProcessPoolExecutor(max_workers=5)**: Runs tasks using 5 separate processes simultaneously.
- `executor.submit(evaluate, item)` submits each task to the pool without blocking.

**Advantages:**
- Easy comparison of all three execution models in one script.
- Process pool gives real speedup for CPU-bound tasks by bypassing the GIL.
- `with` statement handles pool cleanup automatically.

**Disadvantages:**
- Thread pool gives little speedup for CPU-bound tasks due to Python's GIL.
- `time.clock()` is deprecated in Python 3.8+ , should use instead `time.perf_counter()`.
- Process pool has overhead from spawning processes, so small tasks may not benefit.

**Time behavior:**
- Sequential is the slowest, runs all 10 items one by one.
- Thread pool is slightly faster but limited by GIL for CPU-bound work.
- Process pool is the fastest for this workload.