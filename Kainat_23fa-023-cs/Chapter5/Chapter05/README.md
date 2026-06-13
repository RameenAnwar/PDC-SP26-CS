## asyncio_and_futures.py

This program demonstrates asynchronous programming in Python using the asyncio library.

Two coroutines are defined: one calculates the sum of numbers from 1 to N, and the other calculates the factorial of a number.

Both coroutines run concurrently using the event loop, without blocking each other.

Each coroutine uses asyncio.sleep() to simulate a delay and then sets the result in a Future object.

A callback function is used to print the result once each Future is completed.

The program takes input values from command-line arguments.

Important concepts in this program:
- Asynchronous programming (asyncio)
- Coroutines using @asyncio.coroutine
- Event loop execution
- Future objects
- Callbacks (add_done_callback)
- Concurrent task execution

Asyncio allows multiple tasks to run concurrently in a single thread by using an event loop. This improves efficiency for I/O-bound operations by avoiding blocking execution.

## asyncio_coroutine

This program demonstrates a Finite State Machine (FSM) simulation using Python asyncio coroutines.

The system consists of multiple states (state1, state2, state3, and end_state), where each state transitions to another based on randomly generated values.

The execution begins from the start_state, which randomly chooses the next state.

Each state performs a small delay using time.sleep() and then decides the next transition path.

The process continues until the system reaches the end_state, which stops the computation.

Important concepts in this program:
- Finite State Machine (FSM)
- Asynchronous programming using asyncio
- Coroutine-based state transitions
- Random state selection
- Event-driven execution flow

A Finite State Machine models different states and transitions between them based on conditions. Using asyncio coroutines, these transitions can be simulated in a structured and asynchronous way, making it useful for modeling workflows and system behavior.

## asyncio_event_loop

This program demonstrates event loop scheduling using Python asyncio with callback-based tasks.

Three functions (task_A, task_B, task_C) are executed in a cyclic manner using the event loop.

Each task prints its name, waits for a random delay, and then schedules the next task using loop.call_later().

The execution continues in a cycle until the total loop time reaches a defined end time, after which the loop is stopped.

Important concepts in this program:
- asyncio event loop
- Callback scheduling using call_later()
- Cyclic task execution
- Time-based stopping condition
- Cooperative multitasking behavior

The asyncio event loop can schedule tasks in a cycle using callbacks. This allows tasks to run in a controlled sequence over time, making it useful for event-driven and time-based systems.

## asyncio_task_manipulation

## PARALLEL EXECUTION USING asyncio TASKS

This program demonstrates parallel execution of multiple mathematical computations using asyncio.Task in Python.

Three different coroutines are defined: factorial, fibonacci, and binomial coefficient calculation.

Each coroutine performs step-by-step computation and uses asyncio.sleep() to simulate asynchronous delays.

All three tasks are wrapped in asyncio.Task objects and executed concurrently using the event loop.

The asyncio.wait() function ensures that all tasks complete before the program terminates.

Important concepts in this program:
- asyncio Task objects
- Concurrent execution of coroutines
- Event loop management
- Cooperative multitasking
- Parallel execution simulation

Asyncio.Task allows multiple coroutines to run concurrently in a single thread. This is useful for running independent tasks in parallel without creating multiple threads or processes.

## concurrent_future_pooling

This program demonstrates the difference between sequential execution, thread-based parallelism, and process-based parallelism using Python’s concurrent.futures module.

A function is defined that performs a CPU-heavy loop calculation and returns a result based on the input number.

The program first runs all tasks sequentially, then executes them using a ThreadPoolExecutor, and finally using a ProcessPoolExecutor.

Execution time is measured for each approach to compare performance differences.

Important concepts in this program:
- Sequential execution
- ThreadPoolExecutor (multithreading)
- ProcessPoolExecutor (multiprocessing)
- CPU-bound task simulation
- Performance comparison
- Parallel execution models

Sequential execution runs tasks one after another, while thread pools share a single process and are better for I/O tasks. Process pools use multiple CPU cores and are best for CPU-intensive tasks, providing better performance in heavy computations.

