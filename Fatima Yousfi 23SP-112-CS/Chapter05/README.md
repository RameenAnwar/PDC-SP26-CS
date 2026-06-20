# Chapter 05

This chapter covers asynchronous programming with `asyncio` and executor-based parallelism with `concurrent.futures`.

## `asyncio_and_futures.py`

- Accepts two command-line integers.
- Creates two `Future` objects, runs two coroutines, and prints results through done callbacks.

## `asyncio_coroutine.py`

- Simulates a small finite-state machine with chained coroutines.
- The flow moves between `start_state`, `state1`, `state2`, `state3`, and `end_state` based on random transitions.

## `asyncio_event_loop.py`

- Demonstrates manual scheduling with `call_soon()` and `call_later()`.
- The loop rotates through `task_A`, `task_B`, and `task_C` for about sixty seconds before stopping.
- The code uses `time.sleep()` inside scheduled callbacks, which blocks the event loop.

## `asyncio_task_manipulation.py`

- Creates three `asyncio.Task` objects.
- The tasks compute a factorial, a Fibonacci value, and a binomial coefficient while yielding control with `asyncio.sleep(1)`.

## `concurrent_futures_pooling.py`

- Compares sequential execution with a `ThreadPoolExecutor` and a `ProcessPoolExecutor`.
- Each task runs a CPU-heavy counting loop and prints its result.
- The script uses `time.clock()`, which belongs to older Python versions.

## How to run

Examples:

```bash
python asyncio_coroutine.py
python asyncio_and_futures.py 100 10
```
