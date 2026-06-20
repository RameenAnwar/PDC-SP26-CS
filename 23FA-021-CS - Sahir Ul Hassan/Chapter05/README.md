# Chapter 05 - Asyncio and Concurrent Futures

## What I learned overall

- `asyncio` is about cooperative multitasking: tasks only make progress when they `await`.
- Coroutines, the event loop, and task scheduling work together, so correct `await` usage matters more than just writing `async def`.
- `asyncio.create_task()` and `asyncio.gather()` make it easier to run independent work concurrently.
- `concurrent.futures` gives a higher-level way to compare sequential, threaded, and process-based execution.

## Concepts from each file

### `asyncio_coroutine.py`
This file demonstrates an asynchronous finite state machine:

- Defines multiple coroutine states (`start_state`, `state1`, `state2`, `state3`, `end_state`).
- Uses `await asyncio.sleep(1)` to simulate asynchronous work.
- Chooses the next state based on random input.

My takeaway: coroutines are a natural fit for workflows that move through states and pause between steps.

### `asyncio_event_loop.py`
This file shows how the event loop drives coroutine execution:

- Defines three async tasks: `task_A`, `task_B`, and `task_C`.
- Uses `asyncio.get_event_loop().time()` to manage a duration-based loop.
- Awaits tasks one after another inside the loop.

My observation: even with `async` functions, work only overlaps when tasks are scheduled concurrently rather than awaited strictly one by one.

### `asyncio_task_manipulation.py`
This file demonstrates explicit task creation:

- Uses `asyncio.create_task()` to start `factorial`, `fibonacci`, and `binomial_coefficient` concurrently.
- Collects all tasks with `await asyncio.gather(*tasks)`.
- Simulates long-running work with `await asyncio.sleep(1)` inside each loop.

My conclusion: `create_task()` is the right tool when I want multiple coroutines to run at the same time under the same event loop.

### `concurrent_futures_pooling.py`
This file compares three execution strategies:

- Runs the same workload sequentially first.
- Repeats it with `ThreadPoolExecutor`.
- Repeats it again with `ProcessPoolExecutor`.
- Measures elapsed time with `time.perf_counter()`.

My takeaway: this is a good chapter-ending comparison because it shows that threads and processes are tools for different types of workloads, and a serial baseline is necessary for fair timing.

## Personal chapter conclusions

- Async programming is not magic parallelism; it is structured waiting.
- `asyncio` works best when tasks frequently yield control.
- `concurrent.futures` is useful for experimenting with execution models and measuring real performance differences.
- Timing and workload choice matter as much as the API itself when deciding whether concurrency helps.

