# Chapter 05 

# 1. asyncio_and_futures.py
## Overview
This project demonstrates **asynchronous programming in Python** using the `asyncio` module. It runs two coroutines concurrently:

1. **First Coroutine** → Counts numbers from `1` to `N`
2. **Second Coroutine** → Calculates the factorial of a number

The program uses **Future objects** and **callbacks** to display results.
## Requirements
* Python 3.x
* `asyncio` module (built-in)

## How to Run
### Step 1: Open Terminal in VS Code

Open terminal from:

```bash
Terminal → New Terminal
```

### Step 2: Run the Program

```bash
python asyncio_and_futures.py <number1> <number2>
```

### Example

```bash
python asyncio_and_futures.py 5 4
```

### Output

```text
First coroutine (sum of N ints) result = 5
Second coroutine (factorial) result = 24
```

---

## How to Use

The program takes **two inputs**:

| Argument      | Purpose                 |
| ------------- | ----------------------- |
| First Number  | Used in first coroutine |
| Second Number | Used for factorial      |

Example:

```bash
python asyncio_and_futures.py 7 6
```

---

## Advantages

* Runs tasks concurrently
* Efficient resource usage
* Good for waiting tasks (API, files, networking)
* Easy to scale

## Disadvantages

* Uses old async syntax (`yield from`)
* Hard for beginners
* Not ideal for CPU-heavy tasks
* No input validation
## Conclusion
This project helps understand **async programming in Python** using coroutines, Future objects, and callbacks for concurrent execution.


# 2. asyncio_coroutine.py

## Overview

This project demonstrates a **Finite State Machine (FSM)** using Python’s `asyncio` module. The program simulates transitions between different states based on random values.

The states included are:

* **Start State**
* **State 1**
* **State 2**
* **State 3**
* **End State**

The program moves from one state to another until it reaches the **End State**.

## Requirements

* Python 3.x
* `asyncio` module (built-in)

## How to Run
### Step 1: Open Terminal in VS Code

Open terminal from:

```bash
Terminal → New Terminal
```

### Step 2: Run the Program

```bash
python filename.py
```

Replace `filename.py` with your actual file name.

## How to Use

* Run the program in terminal.
* The system randomly chooses transitions between states.
* Execution continues until the **End State** is reached.

### Example Output

```text
Finite State Machine simulation with Asyncio Coroutine

Start State called

...evaluating...
...evaluating...
...stop computation...
```

## Advantages

* Demonstrates **Finite State Machine (FSM)** concept
* Shows use of **asyncio coroutines**
* Simulates random state transitions
* Useful for learning state-based systems

## Disadvantages

* Uses older async syntax (`yield from`)
* Output changes every run due to randomness
* Harder for beginners to understand
* No user input or error handling

## Conclusion
This project helps understand **Finite State Machines (FSM)** and **asynchronous programming** in Python by simulating transitions between multiple states until reaching the final state.

# 3.asyncio_event_loop.py

## Overview
This program demonstrates how Python’s **asyncio event loop** can schedule and manage multiple tasks using `call_later()` and `call_soon()` functions.
It simulates a cycle of three tasks:

* Task A
* Task B
* Task C

These tasks keep calling each other in a loop until a time limit is reached.

---

## Concept

This program is based on the **event-driven programming model**, where:

* Tasks are scheduled instead of executed immediately
* The **event loop** controls execution order
* Functions are triggered after a delay or at a scheduled time

---

## How It Works

### Task A

* Prints a message
* Waits for a random delay
* Schedules **Task B**
* Stops the loop if time limit is reached

---

### Task B

* Prints a message
* Waits for a random delay
* Schedules **Task C**
* Stops the loop if time limit is reached

---

### Task C

* Prints a message
* Waits for a random delay
* Schedules **Task A**
* Continues the cycle until time ends

---

## Event Loop Behavior

The program uses:

* `loop.call_soon()` → Starts Task A immediately
* `loop.call_later()` → Schedules next tasks with delay
* `loop.run_forever()` → Keeps program running
* `loop.stop()` → Stops execution after time limit

---

## Execution Flow

1. Task A starts first
2. It schedules Task B
3. Task B schedules Task C
4. Task C schedules Task A again
5. This cycle continues
6. After 60 seconds, the loop stops

---

## Time Control

```python
end_loop = loop.time() + 60
```

* Program runs for **60 seconds**
* After that, the event loop stops automatically

---

## Requirements

* Python 3.x
* `asyncio` module (built-in)

---

## How to Run
### Step 1: Open Terminal in VS Code

```bash
Terminal → New Terminal
```

### Step 2: Run the Program

```bash
python filename.py
```

## Example Output

```text
task_A called
task_B called
task_C called
task_A called
task_B called
...
```

(Output continues in cycle until time limit is reached)

## Advantages

* Demonstrates **event loop working mechanism**
* Shows task scheduling using `call_soon` and `call_later`
* Helps understand **asynchronous task switching**
* Good for learning event-driven programming

## Disadvantages

* Uses `time.sleep()` which blocks execution (not ideal for asyncio)
* Output is random due to `random.randint`
* No structured async/await usage
* Hard to control execution order precisely
* Not suitable for real-world production systems

## Conclusion
This program helps understand how Python’s **asyncio event loop** schedules and manages tasks. It demonstrates cyclic task execution and basic event-driven behavior using manual scheduling functions.

# 4. asyncio_task_manipulation.py

## Overview
This program demonstrates the use of **`asyncio.Task`** to run multiple functions in parallel. It executes three mathematical operations concurrently:

* Factorial
* Fibonacci series
* Binomial coefficient

Each function runs as a separate asynchronous task using Python’s **asyncio event loop**.

## Concept

The main idea of this program is:

* Multiple tasks can run **concurrently**
* The event loop manages execution
* Each task pauses using `asyncio.sleep()` to allow switching between tasks

This improves understanding of **parallel execution using coroutines**.

## Functions

### 1. Factorial Function

Calculates the factorial of a number.

Example:

```
5! = 5 × 4 × 3 × 2 × 1
```

It prints intermediate steps while computing the result.

### 2. Fibonacci Function

Generates Fibonacci numbers up to a given limit.

Sequence example:

```
0, 1, 1, 2, 3, 5, 8, 13...
```

Each iteration updates values and prints progress.

---

### 3. Binomial Coefficient Function

Calculates:

```
nCk = n! / (k!(n-k)!)
```

It computes the result step by step using an iterative formula.

---

## Asyncio Task Usage

The program uses:

```python id="gk2v3n"
asyncio.Task()
```

Each function is converted into a task so that:

* All three functions run at the same time
* The event loop switches between them during `await` (yield)

---

## Execution Flow

1. Three tasks are created:

   * factorial(10)
   * fibonacci(10)
   * binomial_coefficient(20, 10)

2. All tasks are scheduled together using:

   ```python id="w2qv1a"
   asyncio.wait(task_list)
   ```

3. The event loop runs until all tasks complete.

## Requirements

* Python 3.x
* `asyncio` module (built-in)

## How to Run
### Step 1: Open Terminal in VS Code

```bash id="a91m0p"
Terminal → New Terminal
```

### Step 2: Run the Program

```bash id="k8p4qx"
python filename.py
```

## Example Output (Simplified)

```text id="m4n8c1"
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)

Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756
```

## Advantages

* Runs multiple tasks **concurrently**
* Efficient use of event loop
* Good for learning asynchronous execution
* Improves understanding of task scheduling
* Simulates parallel computation


## Disadvantages

* Uses old syntax (`@asyncio.coroutine`, `yield from`)
* Not true parallel processing (only concurrency)
* Can be confusing for beginners
* Not optimized for CPU-heavy calculations
* Output order is not fixed

## Conclusion
This program demonstrates how **asyncio.Task** can be used to execute multiple mathematical functions concurrently. It helps in understanding how Python manages multiple coroutines using a single-threaded event loop.


## 5. concurrent_futures_pooling.py
## Overview

This Python program demonstrates different ways of executing tasks:

* Sequential Execution
* Thread Pool Execution
* Process Pool Execution

It uses the `concurrent.futures` module to compare performance between these execution models.

The program processes a list of numbers and performs a CPU-heavy computation on each item.

## Objective

The main goal of this program is to understand:

* Difference between sequential and concurrent execution
* Use of **ThreadPoolExecutor**
* Use of **ProcessPoolExecutor**
* Performance comparison of different execution methods

## Program Description

### Input Data

The program uses a list:

```text id="xq8v3d"
number_list = [1, 2, 3, ..., 10]
```

Each number is processed using a function that performs heavy computation.

### 1. Sequential Execution
In this method:

* Tasks are executed one by one
* Each function call completes before the next starts
* No parallelism is used

Execution time is measured using a timer.

### 2. Thread Pool Execution

In this method:

* Multiple threads are used
* Tasks run concurrently in a thread pool
* Managed by `ThreadPoolExecutor`

This is useful for **I/O-bound tasks** (e.g., file handling, network requests).

### 3. Process Pool Execution

In this method:

* Multiple processes are created
* Each process runs independently
* Managed by `ProcessPoolExecutor`

This is suitable for **CPU-heavy tasks** like calculations.

## Function Explanation

### count(number)

* Performs a heavy loop operation
* Simulates CPU-intensive work
* Returns computed result based on input number

### evaluate(item)
* Calls the `count()` function
* Prints the result for each item

## Performance Measurement

The program measures execution time for:

* Sequential execution
* Thread pool execution
* Process pool execution

This helps compare efficiency between methods.

## Requirements

* Python 3.x
* `concurrent.futures` module (built-in)

## How to Run
### Step 1: Open Terminal in VS Code

```bash id="l0k9p2"
Terminal → New Terminal
```
### Step 2: Run the Program

```bash id="v7q3mx"
python filename.py
```

## Expected Output

```text id="c1n9p5"
Item 1, result ...
Item 2, result ...
...
Sequential Execution in X.XX seconds
Thread Pool Execution in X.XX seconds
Process Pool Execution in X.XX seconds
```

## Advantages
### 1. Sequential Execution
* Simple and easy to understand
* No concurrency issues

### 2. Thread Pool
* Efficient for I/O-bound tasks
* Reuses threads (better performance than sequential)

### 3. Process Pool
* Best for CPU-intensive tasks
* Uses multiple CPU cores
* Faster execution for heavy computations

## Disadvantages

### 1. Sequential Execution
* Slow for large workloads
* No parallelism

### 2. Thread Pool
* Limited performance for CPU-heavy tasks
* Python GIL restricts true parallel execution

### 3. Process Pool
* Higher memory usage
* Overhead of creating processes

## Conclusion
This program compares **sequential, thread-based, and process-based execution** using Python’s `concurrent.futures` module. It clearly shows how different execution models affect performance depending on the type of task.
