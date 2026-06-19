# Chapter 03: Process-Based Parallelism in Python

## 1. communicating_with_pipe.py

### What I learned

This script shows how two processes can exchange data using a pipe. One process generates numbers, while the other receives them and computes their squares.

### How to run
python communicating_with_pipe.py
Purpose

Used for direct inter-process communication (IPC).

### When to use

Useful when two processes need a simple, direct channel to send and receive data via multiprocessing.Pipe().

### Overview

Demonstrates data exchange between processes using pipes.

### Benefits
Very fast communication between processes
Simple and lightweight IPC method
Limitations
Best suited only for two-process communication


## 2. communicating_with_queue.py

### What I learned

This program demonstrates communication between processes using a queue in a producer-consumer setup.

### How to run
python communicating_with_queue.py
### Purpose

Used for secure and structured data sharing between multiple processes.

### When to use

Ideal when several processes need to safely pass data using a shared queue.

### Overview

Illustrates process communication using a queue system.

### Benefits
Safe for multiple processes
Easy to implement and manage
Limitations
Slightly slower compared to pipes

## 3. killing_processes.py

### What I learned

This example shows how a running process can be forcefully stopped using the terminate() method.

### How to run
python killing_processes.py

### Purpose

Used to stop processes that are unresponsive or taking too long.

### When to use

Helpful when a process must be abruptly ended.

### Overview

Explains process lifecycle and forced termination.

### Benefits
Gives control over running processes

### Limitations
May cause loss of data if terminated suddenly

## 4. myFunc.py

### What I learned

This file contains a simple reusable function that prints output depending on the process it runs in.

### How to run

Not executed directly; imported in other scripts.

### Purpose

Acts as a helper module for multiprocessing examples.

### When to use

Used when shared logic is needed across multiple processes.

### Overview

A basic utility function for multiprocessing programs.

### Benefits
Reusable code component
Easy to integrate
Limitations
Very limited functionality

## 5. naming_processes.py
### What I learned

This program demonstrates how to assign custom names to processes for better identification.

### How to run
python naming_processes.py

### Purpose

Used to label processes for easier tracking and debugging.

### When to use

Helpful during debugging or monitoring of multiprocessing applications.

### Overview

Shows both default and user-defined process names.

### Benefits
Improves readability and debugging

### Limitations
Does not provide synchronization features

## 6. process_in_subclass.py

### What I learned

This script demonstrates creating processes by extending the multiprocessing.Process class.

### How to run
python process_in_subclass.py

### Purpose

Used for object-oriented process design.

### When to use

Suitable when process behavior needs to be encapsulated in a class structure.

### Overview

Implements multiprocessing using class inheritance.

### Benefits
Clean and structured code design
Highly reusable

### Limitations
Slightly harder for beginners

## 7. process_pool.py

### What I learned

This program demonstrates how a pool of processes can execute multiple tasks in parallel.

### How to run
python process_pool.py

### Purpose

Used for distributing workloads across multiple processes efficiently.

### When to use

Best when applying the same function to many inputs in parallel.

### Overview

Introduces multiprocessing Pool for task distribution.

### Benefits
Faster execution through parallelism
Efficient resource usage

### Limitations
Pool management can become complex

## 8. processes_barrier.py

### What I learned

This program demonstrates synchronization between processes using a Barrier.

### How to run
python processes_barrier.py

### Purpose

Ensures multiple processes reach a certain point before continuing execution.

### When to use

Used when strict coordination between processes is required.

### Overview

Shows synchronization using barriers.

### Benefits
Keeps processes in sync

### Limitations
Requires a fixed number of processes

## 9. run_background_processes_no_daemons.py

### What I learned

This script demonstrates how non-daemon background processes behave.

### How to run
python run_background_processes_no_daemons.py

### Purpose

Used for processes that should continue running independently of the main program.

### When to use

Useful for long-running background tasks.

### Overview

Explains behavior of non-daemon processes.

### Benefits
Runs independently of main program

### Limitations
May continue even after main program exits

## 10. run_background_processes.py

### What I learned

This program demonstrates daemon processes in multiprocessing.

### How to run
python run_background_processes.py

### Purpose

Used for background tasks that should stop when the main program ends.

### When to use

Suitable for lightweight background operations.

### Overview

Shows how daemon processes behave.

### Benefits
Automatically stops with main program

### Limitations
Cannot run independently

## 11. spawning_processes_namespace.py

### What I learned

This script demonstrates process creation using functions imported from external modules.

### How to run
python spawning_processes_namespace.py

### Purpose

Used for modular multiprocessing design.

### When to use

Helpful when separating process logic into different files.

### Overview

Shows multiprocessing with imported functions.

### Benefits
Clean modular structure
Better code organization

### Limitations
Depends on multiple files

## 12. spawning_processes.py
### What I learned

This program shows the simplest way to create new processes using multiprocessing.Process.

### How to run
python spawning_processes.py

### Purpose

Used to run tasks in separate processes for parallel execution.

### When to use

Ideal for basic multiprocessing tasks.

### Overview

Introduces fundamental process creation.

### Benefits
Simple to implement
Enables parallel execution

### Limitations
Higher memory usage compared to threads