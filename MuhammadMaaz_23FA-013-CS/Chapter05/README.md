## 1. asyncio_and_futures.py

**What I Studied:**
I studied how asyncio Futures and coroutines work together. I learned how multiple asynchronous tasks can run concurrently and return results using Future objects.

**How I Executed:**
I created two coroutines: one to compute the sum of numbers and another to compute factorial. Each coroutine sets its result in a Future object. I used `asyncio.get_event_loop()` to run both coroutines concurrently and printed results using callbacks.

**End Uses:**
Used in asynchronous programming for handling multiple background tasks such as I/O operations, web requests, and concurrent computations.

**Advantages:**
- Enables concurrent execution without threads
- Efficient for I/O-bound tasks
- Uses event-driven programming model
- Improves application responsiveness

**Disadvantages:**
- Complex to understand for beginners
- Not suitable for CPU-heavy tasks
- Debugging asynchronous code is harder
- Requires event loop management


## 2. asyncio_coroutine.py

**What I Studied:**
I studied Finite State Machine (FSM) implementation using asyncio coroutines. I learned how different states can transition based on random input values using asynchronous flow.

**How I Executed:**
I created multiple coroutine states (state1, state2, state3, end_state). Each state randomly chooses the next state using `yield from`. The program runs until it reaches the end state using the asyncio event loop.

**End Uses:**
Used in workflow systems, simulations, AI behavior modeling, and event-driven state machines.

**Advantages:**
- Models real-world state transitions
- Non-blocking execution flow
- Flexible design for complex systems
- Easy to extend with new states

**Disadvantages:**
- Hard to trace execution path
- Can become complex with many states
- Random behavior reduces predictability
- Debugging is difficult


## 3. asyncio_event_loop.py

**What I Studied:**
I studied how the asyncio event loop schedules tasks using callbacks. I learned how functions can be executed in a sequence using `call_soon` and `call_later`.

**How I Executed:**
I created three tasks (A, B, C) that call each other in a loop using `loop.call_later`. The event loop runs for a fixed duration and stops when the time limit is reached.

**End Uses:**
Used in event-driven systems, scheduling tasks, simulations, and cyclic process execution.

**Advantages:**
- Efficient event scheduling
- Lightweight concurrency
- Good for timed operations
- No need for threads

**Disadvantages:**
- Callback-based structure is complex
- Hard to maintain for large systems
- Not suitable for CPU-heavy workloads
- Debugging callback chains is difficult


## 4. asyncio_task_manipulation.py

**What I Studied:**
I studied how asyncio.Task can be used to run multiple coroutines in parallel. I learned how tasks manage execution of factorial, fibonacci, and binomial coefficient calculations.

**How I Executed:**
I created three coroutines and wrapped them in `asyncio.Task`. These tasks were executed concurrently using the event loop, and results were printed after completion.

**End Uses:**
Used in parallel execution of independent tasks like mathematical computations, background processing, and async workflows.

**Advantages:**
- Runs multiple tasks concurrently
- Simple task management
- Efficient for independent operations
- Improves performance of async programs

**Disadvantages:**
- Limited to single-threaded event loop
- Not ideal for CPU-heavy computation
- Requires understanding of async concepts
- Debugging multiple tasks can be tricky


## 5. concurrent_futures_pooling.py

**What I Studied:**
I studied concurrent execution using ThreadPoolExecutor and ProcessPoolExecutor. I learned the difference between sequential, multithreaded, and multiprocess execution.

**How I Executed:**
I created a function that performs heavy computation and executed it in three ways: sequential loop, thread pool, and process pool. Execution time for each method was measured using time.clock.

**End Uses:**
Used in performance optimization, parallel computing, CPU-intensive tasks, and workload distribution.

**Advantages:**
- Easy parallel programming model
- Thread pool is good for I/O tasks
- Process pool is good for CPU tasks
- Built-in Python library support

**Disadvantages:**
- Threading limited by GIL
- Process overhead is high
- Debugging parallel execution is harder
- Not always faster than sequential for small tasks