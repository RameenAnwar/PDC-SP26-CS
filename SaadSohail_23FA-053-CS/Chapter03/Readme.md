# Chapter 03 : Process Based Parallelism in Python

---

## 1. communicating_with_pipe.py

### What I learned

This program demonstrates communication between processes using pipes. One process creates numbers while another process receives and squares them.

### How to execute

```bash
python communicating_with_pipe.py
```

### End use

Used for inter-process communication (IPC).

### When and how to use

Used when two processes need to exchange data directly using multiprocessing.Pipe().

### Summary

Shows process communication using pipes.

### Advantages

* Fast communication between processes
* Simple IPC mechanism

### Disadvantages

* Suitable mainly for two-way communication

---

## 2. communicating_with_queue.py

### What I learned

This program demonstrates producer-consumer communication using multiprocessing queues.

### How to execute

```bash
python communicating_with_queue.py
```

### End use

Used for safe data sharing between processes.

### When and how to use

Used when multiple processes need to exchange data safely.

### Summary

Demonstrates queue-based communication.

### Advantages

* Thread-safe and process-safe
* Easy data transfer

### Disadvantages

* Slightly slower than pipes

---

## 3. killing_processes.py

### What I learned

This program demonstrates how a process can be terminated using terminate().

### How to execute

```bash
python killing_processes.py
```

### End use

Used to stop unwanted or long-running processes.

### When and how to use

Used when a process needs to be forcefully stopped.

### Summary

Shows process lifecycle and termination.

### Advantages

* Useful for process control

### Disadvantages

* Force termination may lose data

---

## 4. myFunc.py

### What I learned

This file contains a simple function that prints output based on the process number.

### How to execute

This file is imported into other programs.

### End use

Used as a helper function for multiprocessing examples.

### When and how to use

Used when reusable process logic is required.

### Summary

Simple reusable multiprocessing function.

### Advantages

* Reusable code
* Easy to understand

### Disadvantages

* Limited functionality

---

## 5. naming_processes.py

### What I learned

This program demonstrates assigning custom names to processes.

### How to execute

```bash
python naming_processes.py
```

### End use

Used for identifying processes during execution.

### When and how to use

Used in debugging and monitoring multiprocessing applications.

### Summary

Shows custom and default process names.

### Advantages

* Improves readability and debugging

### Disadvantages

* No synchronization mechanism

---

## 6. process_in_subclass.py

### What I learned

This program demonstrates process creation using class inheritance from multiprocessing.Process.

### How to execute

```bash
python process_in_subclass.py
```

### End use

Used in object-oriented multiprocessing applications.

### When and how to use

Used when process behavior needs to be organized inside classes.

### Summary

Class-based process implementation.

### Advantages

* Better code organization
* Reusable structure

### Disadvantages

* Slightly complex for beginners

---

## 7. process_pool.py

### What I learned

This program demonstrates the use of a process pool to execute tasks in parallel.

### How to execute

```bash
python process_pool.py
```

### End use

Used for parallel execution of multiple tasks.

### When and how to use

Used when the same operation needs to run on many inputs.

### Summary

Shows multiprocessing using Pool.

### Advantages

* Efficient parallel processing
* Reduces execution time

### Disadvantages

* Pool management can be complex

---

## 8. processes_barrier.py

### What I learned

This program demonstrates synchronization of processes using a Barrier.

### How to execute

```bash
python processes_barrier.py
```

### End use

Used when processes must wait for each other before continuing.

### When and how to use

Used in synchronized multiprocessing tasks.

### Summary

Shows process synchronization using barriers.

### Advantages

* Ensures coordination

### Disadvantages

* Fixed number of processes required

---

## 9. run_background_processes_no_daemons.py

### What I learned

This program demonstrates non-daemon background processes.

### How to execute

```bash
python run_background_processes_no_daemons.py
```

### End use

Used when background processes should continue independently.

### When and how to use

Used for long-running background tasks.

### Summary

Shows non-daemon process behavior.

### Advantages

* Runs independently

### Disadvantages

* May continue after main program exits

---

## 10. run_background_processes.py

### What I learned

This program demonstrates daemon processes in multiprocessing.

### How to execute

```bash
python run_background_processes.py
```

### End use

Used for lightweight background tasks.

### When and how to use

Used when processes should stop automatically with the main process.

### Summary

Shows daemon process execution.

### Advantages

* Automatically terminates with main process

### Disadvantages

* Cannot run independently

---

## 11. spawning_processes_namespace.py

### What I learned

This program demonstrates spawning processes using an external function from another file.

### How to execute

```bash
python spawning_processes_namespace.py
```

### End use

Used in modular multiprocessing applications.

### When and how to use

Used when process logic is separated into modules.

### Summary

Shows multiprocessing with imported functions.

### Advantages

* Modular and organized code

### Disadvantages

* Requires multiple files

---

## 12. spawning_processes.py

### What I learned

This program demonstrates basic process spawning using multiprocessing.Process.

### How to execute

```bash
python spawning_processes.py
```

### End use

Used for running tasks in separate processes.

### When and how to use

Used when parallel execution is required.
