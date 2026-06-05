# Chapter 5 – Event-Based Parallelism

## Topic: asyncio_and_futures.py

### What I Learned
I learned how to use `asyncio` with futures. A future stores the result of an asynchronous operation and allows a callback function to run when the result is ready.

### How to Execute
```bash
python asyncio_and_futures.py 5 5
```

### Use / Output
This program runs two coroutine-based tasks. The first coroutine counts numbers up to the given value. The second coroutine calculates the factorial of the given value. Both results are stored in futures and printed through callback functions.

Example output:
```text
First coroutine (sum of N ints) result = 5
Second coroutine (factorial) result = 120
```

### When to Use
Use futures when an asynchronous task will finish later and you want to store or handle its result when it is completed.

### Advantages
- Allows asynchronous result handling
- Callback functions can run automatically after completion
- Useful for non-blocking tasks

### Disadvantages
- More complex than normal function execution
- Old coroutine syntax may not work in newer Python versions
- Futures require careful event loop management

### Summary
This program shows how futures can store results from asynchronous coroutines and trigger callback functions when the results are ready.

---

## Topic: asyncio_coroutine.py

### What I Learned
I learned how coroutines can be used to simulate a finite state machine. Different states call each other asynchronously based on random transition values.

### How to Execute
```bash
python asyncio_coroutine.py
```

### Use / Output
The program starts from the start state and moves between state 1, state 2, and state 3 until it reaches the end state.

Example output:
```text
Finite State Machine simulation with Asyncio Coroutine
Start State called
...evaluating...
...evaluating...
...stop computation...
Resume of the Transition :
Start State calling State 2 with transition value = 0
```

### When to Use
Use coroutine-based state machines when program flow depends on different states and transitions.

### Advantages
- Shows how coroutines can control program flow
- Useful for understanding asynchronous state transitions
- Good example of event-driven logic

### Disadvantages
- Uses old `@asyncio.coroutine` syntax
- Uses `time.sleep()`, which blocks the event loop
- Random transitions can make output unpredictable

### Summary
This program demonstrates how asyncio coroutines can simulate a state machine where each state decides the next state based on input.

---

## Topic: asyncio_event_loop.py

### What I Learned
I learned how the asyncio event loop schedules and runs callback functions using `call_soon()` and `call_later()`.

### How to Execute
```bash
python asyncio_event_loop.py
```

### Use / Output
The program starts with `task_A`, then schedules `task_B`, then `task_C`, and repeats this cycle until the event loop reaches the end time.

Example output:
```text
task_A called
task_B called
task_C called
task_A called
```

### When to Use
Use an event loop when tasks need to be scheduled and executed later without writing manual loop control logic.

### Advantages
- Demonstrates event loop scheduling
- Useful for timed callbacks
- Helps understand asynchronous execution flow

### Disadvantages
- Uses `time.sleep()`, which blocks the event loop
- Can be harder to debug
- Requires manual stopping of the event loop

### Summary
The event loop controls when tasks are executed. This program shows how callbacks can be scheduled immediately or after a delay.

---

## Topic: asyncio_task_manipulation.py

### What I Learned
I learned how to create and run multiple asyncio tasks together. The program runs factorial, Fibonacci, and binomial coefficient calculations as asynchronous tasks.

### How to Execute
```bash
python asyncio_task_manipulation.py
```

### Use / Output
The program creates three asyncio tasks and runs them concurrently. Each task pauses using `asyncio.sleep()`, allowing the other tasks to continue.

Example output:
```text
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
```

### When to Use
Use asyncio tasks when multiple asynchronous operations need to run together in the same event loop.

### Advantages
- Runs multiple tasks concurrently
- Better for I/O-style asynchronous work
- Uses one event loop instead of multiple processes

### Disadvantages
- Not ideal for heavy CPU-bound computation
- Old coroutine syntax may not work in newer Python versions
- Requires understanding of event loops and tasks

### Summary
Asyncio tasks allow multiple coroutines to run concurrently. This is useful when tasks spend time waiting and can give control back to the event loop.

---

## Topic: concurrent_futures_pooling.py

### What I Learned
I learned how to compare sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module.

### How to Execute
```bash
python concurrent_futures_pooling.py
```

### Use / Output
The program runs a heavy counting function on multiple numbers. It first runs sequentially, then using a thread pool, and finally using a process pool. It compares the execution time of all three methods.

Example output:
```text
Item 1, result 10000000
Item 2, result 20000000
Sequential Execution in 8.5 seconds
Thread Pool Execution in 7.9 seconds
Process Pool Execution in 3.4 seconds
```

### When to Use
Use `concurrent.futures` when you want a simple way to manage thread pools or process pools.

### Advantages
- Simple API for parallel execution
- Supports both thread and process pools
- Useful for comparing execution methods
- Process pools can improve CPU-bound task performance

### Disadvantages
- `time.clock()` is removed in newer Python versions
- Threads may not improve CPU-heavy tasks because of Python's GIL
- Process pools use more memory
- Results are not collected in this version of the code

### Summary
This program compares sequential, threaded, and process-based execution. It shows that process pools are usually better for CPU-heavy tasks, while thread pools are more useful for I/O-bound tasks.

---

# Chapter 5 Summary

In this chapter, I learned about event-based parallelism in Python using `asyncio` and `concurrent.futures`. Event-based parallelism allows programs to handle multiple tasks by scheduling them through an event loop instead of running everything step by step.

This chapter covered coroutines, futures, event loops, asyncio tasks, callbacks, and thread/process pooling using `concurrent.futures`.

## Main Concepts Covered

- Asyncio coroutines
- Futures
- Callback functions
- Event loop
- Task scheduling
- `call_soon()`
- `call_later()`
- Asyncio tasks
- Thread pool executor
- Process pool executor
- Sequential vs parallel execution

## Overall Advantages

- Useful for asynchronous programming
- Helps manage waiting tasks efficiently
- Allows multiple tasks to run concurrently
- Good for I/O-bound operations
- `concurrent.futures` gives a simple interface for threads and processes

## Overall Disadvantages

- Async programming is harder for beginners
- Old asyncio syntax may not work in newer Python versions
- Blocking functions like `time.sleep()` reduce the benefit of asyncio
- CPU-heavy work is usually better with process pools
- Debugging asynchronous programs can be difficult

## Final Summary

Chapter 5 explains how Python can handle event-based parallelism using `asyncio` and `concurrent.futures`. Asyncio is useful for tasks that wait, such as network requests or timers, while process pools are better for CPU-heavy tasks. This chapter also shows that asynchronous programming requires careful event loop management and modern Python syntax.
