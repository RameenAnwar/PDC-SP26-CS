# Asyncio Coroutines in Python

## Description
This code demonstrates asynchronous programming using `asyncio` coroutines to execute multiple tasks concurrently.

## What This Code Does
- Defines two coroutines:
  - First coroutine calculates sum count  
  - Second coroutine calculates factorial  
- Uses `Future` objects to store results  
- Executes both coroutines concurrently  
- Prints results using callback functions  

## Execution Flow
1. Read two numbers from command-line arguments  
2. Create asyncio event loop  
3. Create two `Future` objects  
4. Create coroutine tasks:
   - `first_coroutine()`  
   - `second_coroutine()`  
5. Add callback functions using `add_done_callback()`  
6. Run tasks concurrently using `asyncio.wait()`  
7. Print results after completion  
8. Close event loop  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py 5 6
   ```

## End Use
Used for:
- Asynchronous task execution  
- Concurrent I/O operations  
- Non-blocking programming  

## When to Use
Use when:
- Multiple tasks can run concurrently  
- Waiting operations (I/O, APIs, timers) are involved  

Avoid when:
- Heavy CPU computation is required  
- Simple sequential execution is enough  

## How to Use
1. Import `asyncio`  
2. Define coroutines using `@asyncio.coroutine`  
3. Use `yield from` for async waiting  
4. Create tasks and futures  
5. Run tasks using event loop  

## Advantages
- Efficient concurrent execution  
- Non-blocking operations  
- Lightweight compared to threads/processes  

## Disadvantages
- Complex for beginners  
- Not suitable for CPU-intensive tasks  
- Requires event loop management  

## One-Line Summary
Asyncio coroutines allow multiple tasks to run concurrently without blocking the program.



# Finite State Machine using Asyncio Coroutines

## Description
This code demonstrates a Finite State Machine (FSM) simulation using `asyncio` coroutines in Python.

## What This Code Does
- Simulates multiple states using coroutines  
- Randomly transitions between states  
- Uses asynchronous execution with `yield from`  
- Ends when the program reaches `end_state()`  

## Execution Flow
1. Start from `start_state()`  
2. Random value decides next state  
3. Program transitions between:
   - `state1()`  
   - `state2()`  
   - `state3()`  
4. Each state:
   - Prints transition information  
   - Waits for 1 second  
   - Chooses next state randomly  
5. Execution stops at `end_state()`  
6. Event loop runs all coroutine transitions  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- State machine simulation  
- Workflow management  
- Asynchronous state transitions  
- AI/game logic systems  

## When to Use
Use when:
- System behavior depends on states  
- Asynchronous transitions are needed  
- Event-driven workflows are required  

Avoid when:
- Simple linear execution is enough  
- No state transitions are required  

## How to Use
1. Import `asyncio`  
2. Define states as coroutines  
3. Use `yield from` for transitions  
4. Create event loop  
5. Start execution using `run_until_complete()`  

## Advantages
- Clear state-based design  
- Asynchronous execution  
- Flexible workflow transitions  

## Disadvantages
- Complex for large state systems  
- Harder to debug recursive transitions  
- Uses old coroutine syntax (`@asyncio.coroutine`)  

## One-Line Summary
This program simulates a finite state machine using asynchronous coroutines and random state transitions.


# Asyncio Event Loop Task Scheduling

## Description
This code demonstrates task scheduling using the `asyncio` event loop in Python.

## What This Code Does
- Defines three tasks:
  - `task_A()`  
  - `task_B()`  
  - `task_C()`  
- Tasks call each other repeatedly  
- Uses `call_later()` for delayed scheduling  
- Runs tasks for 60 seconds using the event loop  

## Execution Flow
1. Create asyncio event loop  
2. Set loop end time (60 seconds)  
3. Start execution with `task_A()` using `call_soon()`  
4. Each task:
   - Prints task name  
   - Sleeps for random time  
   - Schedules next task using `call_later()`  
5. Loop continues until end time is reached  
6. Event loop stops and closes  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Task scheduling  
- Event-driven programming  
- Asynchronous workflows  
- Repeated background operations  

## When to Use
Use when:
- Tasks must run repeatedly  
- Delayed execution is required  
- Event loop scheduling is needed  

Avoid when:
- Simple sequential execution is enough  
- Heavy CPU processing is required  

## How to Use
1. Import `asyncio`  
2. Create tasks/functions  
3. Schedule tasks using:
   - `call_soon()`  
   - `call_later()`  
4. Run loop using `run_forever()`  
5. Stop loop using `loop.stop()`  

## Advantages
- Efficient task scheduling  
- Non-blocking execution model  
- Good for event-driven systems  

## Disadvantages
- Complex flow control  
- Harder debugging  
- `time.sleep()` blocks event loop  

## One-Line Summary
This program schedules and executes tasks repeatedly using the asyncio event loop.


# Asyncio Tasks for Parallel Math Functions

## Description
This code demonstrates parallel execution of multiple mathematical functions using `asyncio.Task`.

## What This Code Does
- Defines three asynchronous coroutines:
  - Factorial calculation  
  - Fibonacci calculation  
  - Binomial coefficient calculation  
- Executes all tasks concurrently using `asyncio.Task`  
- Uses asynchronous delays with `asyncio.sleep()`  
- Prints results after computation  

## Execution Flow
1. Define asynchronous math functions  
2. Create tasks using `asyncio.Task()`:
   - `factorial(10)`  
   - `fibonacci(10)`  
   - `binomial_coefficient(20,10)`  
3. Create asyncio event loop  
4. Run all tasks concurrently using `asyncio.wait()`  
5. Print outputs of each function  
6. Close event loop  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Concurrent task execution  
- Mathematical simulations  
- Non-blocking asynchronous programming  

## When to Use
Use when:
- Multiple independent tasks can run together  
- Non-blocking execution is needed  
- Concurrent workflows are required  

Avoid when:
- Tasks are CPU-intensive  
- Sequential execution is preferred  

## How to Use
1. Import `asyncio`  
2. Define coroutines using `@asyncio.coroutine`  
3. Create tasks using `asyncio.Task()`  
4. Run tasks with `asyncio.wait()`  
5. Use event loop to execute tasks  

## Advantages
- Concurrent task execution  
- Lightweight compared to threads  
- Efficient asynchronous programming  

## Disadvantages
- Not suitable for heavy CPU tasks  
- More difficult to understand for beginners  
- Uses older coroutine syntax  

## One-Line Summary
This program runs multiple mathematical computations concurrently using asyncio tasks.


# Concurrent Futures: Sequential, Thread Pool, and Process Pool

## Description
This code demonstrates the difference between sequential execution, thread pool execution, and process pool execution using `concurrent.futures`.

## What This Code Does
- Creates a list of numbers from 1 to 10  
- Defines a heavy counting function  
- Executes tasks in three ways:
  - Sequential execution  
  - ThreadPoolExecutor  
  - ProcessPoolExecutor  
- Measures execution time for each method  

## Execution Flow
1. Create number list  
2. Define `count()` function for heavy computation  
3. Define `evaluate()` function  
4. Run sequential execution:
   - Process items one by one  
5. Run thread pool execution:
   - Execute tasks using threads  
6. Run process pool execution:
   - Execute tasks using processes  
7. Print execution time for each method  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python main.py
   ```

## End Use
Used for:
- Comparing execution models  
- Parallel and concurrent programming  
- Performance testing  

## When to Use
Use ThreadPoolExecutor when:
- Tasks are I/O-bound  
- Waiting operations are involved  

Use ProcessPoolExecutor when:
- Tasks are CPU-intensive  
- Heavy computation is required  

Avoid when:
- Tasks are very small  
- Parallel overhead is unnecessary  

## How to Use
1. Import `concurrent.futures`  
2. Create executor:
   - `ThreadPoolExecutor()`  
   - `ProcessPoolExecutor()`  
3. Submit tasks using `submit()`  
4. Measure execution time  

## Advantages
- Easy parallel programming  
- Faster execution for suitable tasks  
- Simple API for threads and processes  

## Disadvantages
- Threads affected by GIL for CPU tasks  
- Process creation overhead  
- More memory usage in multiprocessing  

## One-Line Summary
This program compares sequential, thread pool, and process pool execution performance in Python.
