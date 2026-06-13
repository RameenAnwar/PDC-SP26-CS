# Chapter 05 — Asyncio and Futures

This chapter contains examples demonstrating `asyncio` coroutines, event loop scheduling, and the `concurrent.futures` pooling APIs.

- `asyncio_and_futures.py`:
  - Uses `asyncio.Future` objects and coroutine functions to compute two results concurrently.
  - Accepts two command-line integers and prints results via `Future` callbacks after the coroutines complete.

- `asyncio_coroutine.py`:
  - Implements a small finite-state-machine using `@asyncio.coroutine` and `yield from` to chain coroutine calls.
  - Shows coroutine-based control flow and sleeping to simulate work.

- `asyncio_event_loop.py`:
  - Demonstrates direct scheduling on the `asyncio` event loop using `call_soon` and `call_later`.
  - Uses blocking `time.sleep()` inside scheduled tasks (not idiomatic for asyncio) to simulate variable-duration work; prefer `asyncio.sleep()` in real code.

- `asyncio_task_manipulation.py`:
  - Creates three `asyncio.Task` instances running different coroutine computations (`factorial`, `fibonacci`, `binomial_coefficient`) and waits for their completion.
  - Each coroutine yields control (`yield from asyncio.sleep(1)`) to simulate asynchronous progress.

- `concurrent_futures_pooling.py`:
  - Compares sequential execution, `ThreadPoolExecutor`, and `ProcessPoolExecutor` using a CPU-bound `count()` function.
  - Submits tasks with `executor.submit` and prints elapsed times; useful to study CPU vs I/O-bound behavior and when to use threads vs processes.

How to run

- Standard Python invocation for these examples. Some examples take command-line arguments, e.g.:

```
python asyncio_and_futures.py 100 10
```

Notes

- The code uses legacy `@asyncio.coroutine`/`yield from` syntax; for modern code prefer `async def` and `await` (Python 3.5+).
- Avoid blocking calls (like `time.sleep`) inside coroutine-driven code; use `await asyncio.sleep(...)` instead.
