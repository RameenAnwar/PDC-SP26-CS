# Chapter # 5

---

## 1. asyncio_and_futures.py

### Description:
Demonstrates asyncio Futures — two coroutines run concurrently, each computing a result and setting it on a Future object. Callbacks are triggered automatically when futures complete.

### How it Works:
- Two async coroutines created — `first_coroutine` computes sum of N integers, `second_coroutine` computes factorial
- Each coroutine sets result on its Future using `future.set_result()`
- `got_result` callback prints result when future is done
- `asyncio.gather()` runs both coroutines concurrently
- Both sleep for 4 seconds but run in parallel so total time is ~4 seconds

### Result:
Prints sum of integers 1 to num1 and factorial of num2 after 4 seconds concurrently.

### Advantages:
- Futures allow callback-based result handling
- `asyncio.gather()` runs multiple coroutines concurrently
- Non-blocking — both tasks run in parallel

### Disadvantages:
- Requires command line arguments — error if not provided
- More complex than simple async functions

### Where to Use:
- Running multiple independent async computations simultaneously
- Any scenario where callback on task completion is needed

---

## 2. asyncio_coroutine.py

### Description:
Demonstrates a Finite State Machine (FSM) using asyncio coroutines. Program randomly transitions between states until it reaches the end state.

### How it Works:
- `start_state` randomly transitions to state1 or state2
- Each state randomly transitions to another state or end state
- `time.sleep(1)` adds delay at each state
- Recursion continues until `end_state` is reached
- `asyncio.run(start_state())` starts the event loop

### Result:
Prints each state transition with its value until end state is reached. Output varies each run due to random transitions.

### Advantages:
- Clean way to model state machines using async functions
- Easy to add new states without changing existing ones
- Readable flow of execution

### Disadvantages:
- Deep recursion may cause stack overflow for long chains
- `time.sleep()` blocks event loop — should use `await asyncio.sleep()` for true async

### Where to Use:
- Simulating state machines in games or protocols
- Modeling workflow systems with conditional transitions
- Any system with defined states and transitions

---

## 3. asyncio_event_loop.py

### Description:
Demonstrates asyncio event loop scheduling — three tasks (A, B, C) are scheduled in sequence using `call_later()` and run for 60 seconds before loop stops.

### How it Works:
- `task_A` runs first, sleeps random time, then schedules `task_B` after 1 second
- `task_B` schedules `task_C`, `task_C` schedules back `task_A`
- Each task checks if remaining time allows another cycle
- Loop stops when 60 seconds have passed
- `loop.run_forever()` keeps loop running until `loop.stop()` is called

### Result:
Prints task_A, task_B, task_C called repeatedly in sequence for 60 seconds then stops.

### Advantages:
- `call_later()` allows precise scheduling of tasks
- No threads needed — single threaded event loop handles all tasks
- Easy to control execution timing

### Disadvantages:
- `time.sleep()` blocks entire event loop — no other tasks can run during sleep
- Hard to control exact execution count due to random sleep values

### Where to Use:
- Scheduled task execution in servers
- Polling systems that check status at regular intervals
- Any time-based sequential task scheduling

---

## 4. asyncio_task_manipulation.py

### Description:
Demonstrates asyncio Tasks — three math functions (factorial, fibonacci, binomial coefficient) run concurrently as separate tasks using `asyncio.create_task()`.

### How it Works:
- Three async functions defined — factorial, fibonacci, binomial coefficient
- Each function loops with `await asyncio.sleep(1)` between iterations
- `asyncio.create_task()` wraps each coroutine as a Task
- `asyncio.wait()` waits for all tasks to complete
- All three tasks run concurrently — interleaved output

### Result:
Prints interleaved computation steps of all three functions simultaneously, then final results of factorial(10), fibonacci(10), and binomial_coefficient(20,10).

### Advantages:
- True concurrency — all three tasks run simultaneously
- `create_task()` schedules tasks immediately without waiting
- Clean and readable compared to manual threading

### Disadvantages:
- Only concurrent, not parallel — still single threaded
- Not suitable for CPU-heavy tasks — use multiprocessing instead

### Where to Use:
- Running multiple I/O-bound tasks simultaneously
- Web scraping, API calls, or database queries in parallel
- Any scenario requiring concurrent execution of independent tasks

---

## 5. concurrent_futures_pooling.py

### Description:
Demonstrates and compares three execution methods — sequential, thread pool, and process pool — for computing a heavy count function on a list of numbers.

### How it Works:
- `count()` performs 10 million iterations and multiplies result by input number
- Sequential runs each item one by one in a loop
- `ThreadPoolExecutor` runs 5 threads simultaneously
- `ProcessPoolExecutor` runs 5 processes simultaneously
- `time.perf_counter()` measures execution time for each method

### Result:
Prints each item's result and total execution time for all three methods. Process pool is fastest for CPU-bound tasks, sequential is slowest.

### Advantages:
- Easy comparison of all three execution methods in one file
- `concurrent.futures` provides clean high-level API for both threads and processes
- Automatically manages worker pool lifecycle

### Disadvantages:
- Thread pool not efficient for CPU-bound tasks due to GIL
- Process pool has higher memory overhead
- Sequential is always slowest for independent tasks

### Where to Use:
- CPU-intensive batch processing with process pool
- I/O-bound tasks like file reading or API calls with thread pool
- Benchmarking parallel vs sequential performance

---