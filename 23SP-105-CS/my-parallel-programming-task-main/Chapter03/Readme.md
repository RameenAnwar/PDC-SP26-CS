# Chapter 3 – Multiprocessing Concepts with GCD & LCM

## Overview

This project demonstrates various multiprocessing concepts in Python by implementing **Greatest Common Divisor (GCD)** and **Least Common Multiple (LCM)** computations. The objective is to understand process creation, communication, synchronization, and management through practical examples.

Each multiprocessing technique is applied to the same GCD/LCM computation problem, making it easier to compare different approaches and understand their behavior.

---

## Concepts Implemented

### 1. Communication with Pipe

* Uses `multiprocessing.Pipe()` for inter-process communication.
* One process computes the LCM value and sends it through a pipe.
* Another process receives and displays the result.

### 2. Communication with Queue

* Demonstrates the Producer-Consumer pattern using `multiprocessing.Queue()`.
* Processes safely exchange LCM results through a shared queue.

### 3. Killing Processes

* Shows how to terminate a running process using `terminate()`.
* Useful for stopping unnecessary or long-running tasks.

### 4. Naming Processes

* Assigns custom names to processes.
* Uses `multiprocessing.current_process().name` for identification and debugging.

### 5. Process Subclassing

* Creates a custom class by inheriting from `multiprocessing.Process`.
* Overrides the `run()` method to perform LCM calculations.
* Demonstrates an object-oriented multiprocessing approach.

### 6. Process Pool

* Uses `multiprocessing.Pool` to execute multiple computations concurrently.
* Efficient for handling batch tasks and workload distribution.

### 7. Process Barrier

* Implements synchronization using `multiprocessing.Barrier()`.
* Ensures all processes reach a checkpoint before continuing execution.

### 8. Background Process (Non-Daemon)

* Runs a process in the background with `daemon=False`.
* The main program waits for the process to complete.

### 9. Background Process (Daemon)

* Runs a process with `daemon=True`.
* The process executes in the background and terminates automatically when the main program exits.

### 10. Shared Namespace

* Uses `multiprocessing.Manager().Namespace()`.
* Allows processes to share and update common variables.

### 11. Shared Manager List

* Uses `multiprocessing.Manager().list()`.
* Multiple processes store computation results safely in a shared list.

---

## Project Structure

| File Name                 | Description                          |
| ------------------------- | ------------------------------------ |
| pipe_lcm.py               | Communication using Pipe             |
| queue_lcm.py              | Communication using Queue            |
| kill_process_lcm.py       | Process Termination                  |
| name_process_lcm.py       | Process Naming                       |
| subclass_process_lcm.py   | Process Subclassing                  |
| pool_lcm.py               | Process Pool                         |
| barrier_process_lcm.py    | Process Synchronization with Barrier |
| background_process_lcm.py | Background Process (Non-Daemon)      |
| daemon_process_lcm.py     | Background Process (Daemon)          |
| namespace_lcm.py          | Shared Namespace                     |
| manager_list_lcm.py       | Shared Manager List                  |

---

## Execution Time Measurement

Each program records execution time using Python's `time` module.

```python
start = time.time()
# LCM/GCD computation
end = time.time()

print("Execution Time:", end - start)
```

This helps analyze the performance impact of different multiprocessing techniques.

---

## Example Output

```text
Task 0 -> LCM = 36 | Time = 0.0000012 sec
Task 1 -> LCM = 36 | Time = 0.0000011 sec
Task 2 -> LCM = 36 | Time = 0.0000013 sec
```

---

## Learning Objectives

By completing this project, you will learn:

* Process creation and execution
* Process naming and identification
* Inter-process communication using Pipe and Queue
* Shared memory using Manager objects
* Process synchronization using Barrier
* Background process execution
* Daemon vs Non-Daemon processes
* Process termination techniques
* Performance measurement and analysis

---

## Requirements

* Python 3.8+
* multiprocessing module (built-in)
* time module (built-in)

---

## How to Run

Clone the repository and execute any Python file:

```bash
python pipe_lcm.py
```

Example:

```bash
python pool_lcm.py
python queue_lcm.py
python barrier_process_lcm.py
```

---

## Future Enhancements

* Hybrid Threading + Multiprocessing applications
* Large-scale GCD/LCM computations on datasets
* Performance benchmarking of different multiprocessing models
* Distributed processing across multiple machines
* Real-time process monitoring dashboard

---

## Author

Huzaifa Alim

Computer Science Student
Usman Institute of Technology (UIT)

