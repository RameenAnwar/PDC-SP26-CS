# Chapter 05: Asyncio and Futures

This folder contains example code for Python concurrency using `asyncio` and `concurrent.futures`.

## Files included

- `asyncio_and_futures.py`
- `asyncio_coroutine.py`
- `asyncio_event_loop.py`
- `asyncio_task_manipulation.py`
- `concurrent_futures_pooling.py`

---

## `asyncio_and_futures.py`

### What it does

- Defines two coroutines: `first_coroutine` and `second_coroutine`.
- Each coroutine receives a `Future` and a number input.
- `first_coroutine` counts from 1 to `num` and then waits 4 seconds.
- `second_coroutine` computes the factorial of `num` and then waits 4 seconds.
- When each coroutine finishes, it sets the result into its `Future`.
- A callback `got_result` prints each future's result.
- The event loop runs both coroutines concurrently using `asyncio.wait`.

### How to run

```bash
python asyncio_and_futures.py 10 5
```

### Expected output

If `num1=10` and `num2=5`, the output should be:

```text
First coroutine (sum of N ints) result = 10
Second coroutine (factorial) result = 120
```

The order is not guaranteed, but both lines should appear after the coroutines complete.

---

## `asyncio_coroutine.py`

### What it does

- Simulates a finite state machine using `asyncio.coroutine` and `yield from`.
- `start_state` chooses either `state1` or `state2` randomly.
- Each state prints a message, pauses with `time.sleep(1)`, then transitions to another state.
- `state3` may transition to `end_state` or back to another state.
- `end_state` prints a final stop message and returns its output.
- The code uses randomness with `randint(0, 1)`, so the state transition path changes each run.

### How to run

```bash
python asyncio_coroutine.py
```

### Expected output

Output varies, but it begins with:

```text
Finite State Machine simulation with Asyncio Coroutine
Start State called
```

Then it prints several evaluation lines such as:

```text
...evaluating...
```

Finally it prints a resumed transition message like:

```text
Resume of the Transition : 
Start State calling State 2 with transition value = 0
State 2 calling End State with transition value = 1
```

Because the transitions are random, the exact path and final state string differ each run.

---

## `asyncio_event_loop.py`

### What it does

- Uses the low-level asyncio event loop directly.
- Defines three callback-style functions: `task_A`, `task_B`, and `task_C`.
- Each task sleeps for a random number of seconds between 0 and 5 using blocking `time.sleep`.
- After each task runs, the next task is scheduled with `loop.call_later(1, ...)` when enough time remains.
- The loop stops after about 60 seconds or when no more tasks are scheduled.

### How to run

```bash
python asyncio_event_loop.py
```

### Expected output

The program prints repeated calls such as:

```text
task_A called
task_B called 
task_C called
```

The sequence continues until the loop stops. Because each task uses random sleep, the calls are spaced irregularly. After about 60 seconds, the program exits.

---

## `asyncio_task_manipulation.py`

### What it does

- Creates three asyncio tasks using `asyncio.Task`.
- `factorial(10)` computes factorial values step-by-step, sleeping 1 second after each step.
- `fibonacci(10)` computes Fibonacci numbers step-by-step, sleeping 1 second after each step.
- `binomial_coefficient(20, 10)` computes a binomial coefficient step-by-step, sleeping 1 second after each step.
- The event loop runs all tasks concurrently with `asyncio.wait`.

### How to run

```bash
python asyncio_task_manipulation.py
```

### Expected output

The output will interleave progress lines from each task, for example:

```text
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)
Asyncio.Task: Compute factorial(3)
Asyncio.Task: Compute fibonacci(1)
Asyncio.Task: Compute binomial_coefficient(2)
...
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
```

The exact interleaving may vary, but all three results are printed after the tasks finish.

---

## `concurrent_futures_pooling.py`

### What it does

- Defines `number_list` from 1 to 10.
- Defines a CPU-bound function `count(number)` that loops 10 million times.
- `evaluate(item)` calls `count(item)` and prints the item and result.
- Runs the same work in three modes:
  - sequential execution
  - `ThreadPoolExecutor` with 5 workers
  - `ProcessPoolExecutor` with 5 workers
- Each mode prints a completion time using `time.clock()`.

### How to run

```bash
python concurrent_futures_pooling.py
```

### Expected output

Output includes lines like:

```text
Item 1, result 10000000
Item 2, result 10000000
...
Sequential Execution in X.XXXX seconds
```

Then the same item lines appear again for the thread pool and process pool phases, followed by timing lines:

```text
Thread Pool Execution in Y.YYYY seconds
Process Pool Execution in Z.ZZZZ seconds
```

Because the work is CPU-bound, the process pool is likely faster than the thread pool on CPython. Exact timing values vary by machine.

---

## Notes

- These examples use older `asyncio` syntax (`@asyncio.coroutine` and `yield from`) that is compatible with Python 3.4+ but not the modern `async def` / `await` style.
- `concurrent_futures_pooling.py` uses `time.clock()`, which is deprecated in recent Python versions; on Python 3.8+ it may raise a warning or error.
- `asyncio_event_loop.py` uses blocking `time.sleep`, which is not ideal for asyncio but is used here to demonstrate event loop scheduling.
