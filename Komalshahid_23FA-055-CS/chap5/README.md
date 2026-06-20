Python Asyncio & Concurrent Futures — Chapter 5
This repository covers asynchronous programming in Python using the asyncio module and concurrent.futures. Each program demonstrates a different approach to running tasks concurrently — from event loops and coroutines to futures, tasks, and thread/process pools. These techniques allow a program to handle multiple operations at the same time without blocking.

Program Descriptions

1. asyncio_event_loop.py — Event Loop with Scheduled Tasks
Description:
This file demonstrates Python's asyncio event loop — the core engine that drives asynchronous execution. Three tasks (A, B, C) are scheduled to run one after another in a cycle for 60 seconds.
How it works:
task_A, task_B, and task_C are plain functions. Each sleeps for a random time (0–5 seconds), then schedules the next task using loop.call_later(1, next_task). If the time limit is almost reached, the loop stops instead of scheduling the next task.
Result:
task_A called
task_B called
task_C called
task_A called
...
Advantages:

Shows the basic mechanics of an event loop and how tasks are scheduled.
No coroutines needed — plain functions work with call_later.

Disadvantages:

Uses time.sleep() which blocks the event loop — in real async code asyncio.sleep() should be used.
Runs for a fixed 60 seconds regardless of outcome.

Where it can be used:

Scheduling periodic background tasks, building simple state machines, or understanding how event loops work.


2. asyncio_coroutine.py — Finite State Machine with Coroutines
Description:
This file simulates a Finite State Machine (FSM) using asyncio coroutines. The machine starts at a start state and randomly transitions through states 1, 2, and 3 until it reaches the end state.
How it works:
Each state is a coroutine function. It picks a random value (0 or 1), sleeps for 1 second, and based on the value moves to the next state using yield from. The chain continues until end_state is reached and the full transition path is printed.
Result:
Finite State Machine simulation with Asyncio Coroutine
Start State called
...evaluating...
...evaluating...
...stop computation...
Resume of the Transition:
Start State calling State 1 with transition value = 1 ...
(Output varies since transitions are random.)
Advantages:

Clean way to model state-based logic using coroutines.
Each state is isolated and easy to modify independently.

Disadvantages:

Uses time.sleep() instead of asyncio.sleep() which blocks the loop during each state.
Transition path depends on random values so output is different every run.

Where it can be used:

Protocol parsers, game logic, workflow engines, or any system that moves through defined states based on input conditions.


3. asyncio_and_futures.py — Coroutines with Futures and Callbacks
Description:
This file shows how asyncio.Future objects work. Two coroutines run in parallel — one computes the sum of N integers and the other computes a factorial. Each stores its result in a future object and a callback prints it when ready.
How it works:
Two futures are created. first_coroutine counts from 1 to num1 and sets the sum as the future result. second_coroutine computes the factorial of num2. Both run together using asyncio.wait. When each future completes, the got_result callback automatically prints the result.
Result:
First coroutine (sum of N ints) result = 5
Second coroutine (factorial) result = 720
Advantages:

Shows the complete async pattern — coroutines, futures, and callbacks working together.
Both tasks run concurrently, not sequentially.

Disadvantages:

Requires two number arguments from the command line — crashes without them.
Both coroutines have a fixed 4-second sleep regardless of input size.

Where it can be used:

Running multiple computations concurrently, parallel API calls, or any task where a result is needed in the future without blocking other work.


4. asyncio_task_manipulation.py — Asyncio Tasks Running in Parallel
Description:
This file uses asyncio.Task to run three mathematical computations — factorial, fibonacci, and binomial coefficient — concurrently inside a single event loop. The tasks take turns executing step by step.
How it works:
Each function is a coroutine that uses yield from asyncio.sleep(1) between each step to hand control back to the event loop. All three are wrapped in asyncio.Task and run together using asyncio.wait. The event loop interleaves their execution so all three progress simultaneously.
Result:
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)
Asyncio.Task: Compute factorial(3)
...
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
Advantages:

Clearly demonstrates cooperative multitasking — tasks yield control voluntarily.
All three computations interleave cleanly without blocking each other.

Disadvantages:

The 1-second sleep between each step makes the total execution slow for large inputs.
asyncio.Task() used this way is deprecated in newer Python versions.

Where it can be used:

Running multiple I/O-bound tasks concurrently, such as fetching data from multiple APIs simultaneously.


5. concurrent_futures_pooling.py — Thread Pool vs Process Pool vs Sequential
Description:
This file compares three execution methods for the same CPU-heavy task — sequential, thread pool, and process pool — and prints the time each one takes. It uses Python's concurrent.futures module.
How it works:
A count function loops 10 million times and returns a result. This function is run on numbers 1 to 10 in three different ways. Sequential runs them one at a time. ThreadPoolExecutor runs 5 threads in parallel. ProcessPoolExecutor runs 5 processes in parallel. The total time for each approach is measured and printed.
Result:
Item 1, result 10000000
...
Sequential Execution in X seconds
Thread Pool Execution in X seconds
Process Pool Execution in X seconds
Process pool is generally the fastest for this CPU-heavy task.
Advantages:

Directly compares all three execution approaches in one place.
Clear demonstration of when process pools outperform thread pools for CPU-bound work.

Disadvantages:

CPU-heavy task — may take a while on slower machines.
Uses time.clock() which is removed in Python 3.8+ and needs a small fix to run.

Where it can be used:

Benchmarking, data processing pipelines, or deciding between threading and multiprocessing for a given task.


Applications
ConceptReal-World UseEvent LoopWeb servers, GUI applications, real-time systemsCoroutines & FSMProtocol parsers, game logic, workflow enginesFutures & CallbacksParallel API calls, async data fetchingAsyncio TasksConcurrent web requests, async pipelinesThread PoolI/O-bound tasks like file reading, web scrapingProcess PoolCPU-bound tasks like data processing, ML training

About
Each program in this repository demonstrates a different aspect of asynchronous and concurrent programming in Python. Together they cover the event loop, coroutines, futures, tasks, and pool-based execution — the core building blocks of modern async Python applications.