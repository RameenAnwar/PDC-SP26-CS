# Chapter 3 – Process Based Parallelism

## Topic: communicating_with_pipe.py

### What I Learned
I learned how to use pipes in multiprocessing to communicate between different processes. One process sends data through a pipe, another process receives it, processes it, and sends the result through another pipe.

### How to Execute
```bash
python communicating_with_pipe.py
```

### Use / Output
This program sends numbers from 0 to 9 through a pipe. Another process receives each number, squares it, and sends the squared value back through another pipe.

Example output:

```text
0
1
4
9
16
25
36
49
64
81
End
```

### When to Use
Use pipes when two processes need to communicate directly with each other.

### Advantages
- Allows direct communication between processes
- Useful for producer-consumer style processing
- Good for passing data between related processes

### Disadvantages
- More complex than simple process execution
- Needs proper closing of pipe ends
- Can cause errors if pipe communication is not handled correctly

### Summary
Pipes allow processes to send and receive data directly. They are useful when one process produces data and another process processes that data.

---

## Topic: communicating_with_queue.py

### What I Learned
I learned how to use a multiprocessing queue to share data between producer and consumer processes.

### How to Execute
```bash
python communicating_with_queue.py
```

### Use / Output
The producer process generates random numbers and puts them into a queue. The consumer process removes items from the queue and displays them.

Example output:

```text
Process Producer : item 45 appended to queue producer-1
The size of queue is 1
Process Consumer : item 45 popped from by consumer-1
```

### When to Use
Use queues when multiple processes need to safely share data.

### Advantages
- Safe way to exchange data between processes
- Useful for producer-consumer problems
- Easier to manage than pipes for multiple items

### Disadvantages
- Queue timing can be tricky
- Consumer may stop early if the queue is temporarily empty
- More complex than normal function calls

### Summary
Queues are used for communication between processes. They are useful when one process produces data and another process consumes it.

---

## Topic: killing_processes.py

### What I Learned
I learned how to start, terminate, join, and check the status of a process using multiprocessing.

### How to Execute
```bash
python killing_processes.py
```

### Use / Output
This program starts a process, checks whether it is alive, terminates it, joins it, and then prints the exit code.

Example output:

```text
Process before execution: False
Process running: True
Process terminated: True
Process joined: False
Process exit code: -15
```

### When to Use
Use this when you need to stop a running process before it finishes naturally.

### Advantages
- Gives control over process execution
- Useful for stopping long-running tasks
- Helps manage system resources

### Disadvantages
- Terminating a process suddenly can cause incomplete work
- Data may be lost if the process is killed during execution
- Should be used carefully

### Summary
Process termination is used to stop a process manually. It is useful, but unsafe if the process is handling important data.

---

## Topic: myFunc.py

### What I Learned
I learned how to define a function in a separate file and reuse it in another Python program.

### How to Execute
This file is used as a module and can be imported into another Python file.

Example:

```bash
python spawning_processes_namespace.py
```

### Use / Output
The function prints the process number and outputs values based on the input number.

Example output:

```text
calling myFunc from process n°: 3
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
```

### When to Use
Use separate function files when you want to organize code and reuse functions in multiple programs.

### Advantages
- Improves code organization
- Makes code reusable
- Keeps main files cleaner

### Disadvantages
- Requires proper imports
- File path or module errors can occur
- Slightly harder for beginners to understand

### Summary
Using separate function files helps organize code and makes functions reusable across multiple programs.

---

## Topic: naming_processes.py

### What I Learned
I learned how to assign custom names to processes and how to get the current process name.

### How to Execute
```bash
python naming_processes.py
```

### Use / Output
This program creates one process with a custom name and another process with a default name. Both processes print their starting and ending messages.

Example output:

```text
Starting process name = myFunc process
Starting process name = Process-1
Exiting process name = myFunc process
Exiting process name = Process-1
```

### When to Use
Use process names when debugging or tracking multiple processes.

### Advantages
- Makes processes easier to identify
- Helpful during debugging
- Improves readability of output

### Disadvantages
- Naming does not affect performance
- Can be confusing if too many processes are running
- Requires careful tracking

### Summary
Naming processes helps identify and debug multiprocessing programs more easily.

---

## Topic: process_in_subclass.py

### What I Learned
I learned how to create a custom process by subclassing `multiprocessing.Process` and overriding the `run()` method.

### How to Execute
```bash
python process_in_subclass.py
```

### Use / Output
This program creates 10 custom process objects. Each process calls its own `run()` method and prints its process name.

Example output:

```text
called run method in MyProcess-1
called run method in MyProcess-2
```

### When to Use
Use process subclasses when you want to create custom process behavior using object-oriented programming.

### Advantages
- Organized process structure
- Useful for large applications
- Supports object-oriented design

### Disadvantages
- More complex than simple process functions
- Requires understanding of classes and inheritance
- May be unnecessary for small programs

### Summary
Subclassing `Process` allows custom process behavior by defining the `run()` method.

---

## Topic: process_pool.py

### What I Learned
I learned how to use a process pool to run tasks in parallel using multiple worker processes.

### How to Execute
```bash
python process_pool.py
```

### Use / Output
This program creates a pool of 4 processes and calculates the square of numbers from 0 to 99.

Example output:

```text
Pool : [0, 1, 4, 9, 16, 25, ...]
```

### When to Use
Use a process pool when you have many similar tasks that can run independently.

### Advantages
- Runs tasks in parallel
- Uses CPU cores efficiently
- Easier than manually creating many processes

### Disadvantages
- More memory usage
- Not useful for very small tasks
- Requires closing and joining the pool properly

### Summary
Process pools make it easier to run many tasks in parallel by managing multiple worker processes automatically.

---

## Topic: processes_barrier.py

### What I Learned
I learned how to use a barrier to synchronize multiple processes so they wait for each other before continuing.

### How to Execute
```bash
python processes_barrier.py
```

### Use / Output
Two processes wait at a barrier and continue together. Two other processes run without waiting.

Example output:

```text
process p1 - test_with_barrier ----> 2026-06-06 10:20:30
process p2 - test_with_barrier ----> 2026-06-06 10:20:30
process p3 - test_without_barrier ----> 2026-06-06 10:20:29
process p4 - test_without_barrier ----> 2026-06-06 10:20:29
```

### When to Use
Use barriers when multiple processes must reach the same point before continuing.

### Advantages
- Helps synchronize processes
- Prevents one process from moving too far ahead
- Useful in parallel algorithms

### Disadvantages
- Can cause waiting delays
- Incorrect barrier count can cause deadlock
- Adds complexity to the program

### Summary
A barrier is used to make processes wait until all required processes reach the same point.

---

## Topic: run_background_processes.py

### What I Learned
I learned about daemon processes and non-daemon processes in multiprocessing.

### How to Execute
```bash
python run_background_processes.py
```

### Use / Output
This program creates one daemon/background process and one normal process. The daemon process may stop when the main program exits, while the non-daemon process continues until it finishes.

Example output:

```text
Starting background_process
Starting NO_background_process
---> 0
---> 5
Exiting NO_background_process
```

### When to Use
Use daemon processes for background tasks that should not block the main program from exiting.

### Advantages
- Useful for background work
- Main program does not need to wait for daemon processes
- Good for helper tasks

### Disadvantages
- Daemon processes can stop suddenly
- Work may not complete
- Not suitable for important tasks

### Summary
Daemon processes run in the background and may end automatically when the main program finishes.

---

## Topic: run_background_processes_no_daemons.py

### What I Learned
I learned how non-daemon processes behave when both processes are set to run normally.

### How to Execute
```bash
python run_background_processes_no_daemons.py
```

### Use / Output
Both processes run as normal non-daemon processes, so the program waits for them to complete.

Example output:

```text
Starting background_process
Starting NO_background_process
---> 0
---> 5
Exiting background_process
Exiting NO_background_process
```

### When to Use
Use non-daemon processes when the task must complete before the program exits.

### Advantages
- Ensures process completion
- Safer for important tasks
- Prevents unfinished background work

### Disadvantages
- Main program may take longer to exit
- Can block program completion
- Requires proper process management

### Summary
Non-daemon processes continue running until they finish, even if the main program reaches the end.

---

## Topic: spawning_processes.py

### What I Learned
I learned how to create and start multiple processes using `multiprocessing.Process`.

### How to Execute
```bash
python spawning_processes.py
```

### Use / Output
This program creates six processes. Each process calls `myFunc()` with a different number.

Example output:

```text
calling myFunc from process n°: 3
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
```

### When to Use
Use process spawning when you want to run multiple tasks independently.

### Advantages
- Allows parallel execution
- Makes better use of CPU
- Good for independent tasks

### Disadvantages
- More memory usage than threads
- Process creation has overhead
- Requires proper start and join handling

### Summary
Spawning processes allows Python programs to run multiple independent tasks using separate processes.

---

## Topic: spawning_processes_namespace.py

### What I Learned
I learned how to import a function from another file and run it inside multiple processes.

### How to Execute
```bash
python spawning_processes_namespace.py
```

### Use / Output
This program imports `myFunc` from `myFunc.py` and uses it as the target function for multiple processes.

Example output:

```text
calling myFunc from process n°: 4
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
output from myFunc is :3
```

### When to Use
Use this method when your process function is stored in a separate module/file.

### Advantages
- Keeps code modular
- Reuses functions from other files
- Makes large projects cleaner

### Disadvantages
- Requires correct file structure
- Import errors can happen
- Slightly harder than writing everything in one file

### Summary
This program shows how multiprocessing can use functions imported from another file, making the code more modular and organized.

---

# Chapter 3 Summary

In this chapter, I learned about process-based parallelism in Python using the `multiprocessing` module. I practiced creating processes, naming processes, using daemon and non-daemon processes, terminating processes, subclassing processes, using process pools, and communicating between processes using pipes and queues.

This chapter also explained how synchronization works using barriers and how different processes can work together in parallel. Process-based parallelism is useful for CPU-heavy tasks because it can use multiple CPU cores.

## Main Concepts Covered

- Creating processes
- Running processes in parallel
- Naming processes
- Daemon and non-daemon processes
- Killing and joining processes
- Subclassing `multiprocessing.Process`
- Process pools
- Pipes for process communication
- Queues for process communication
- Barriers for synchronization

## Overall Advantages

- Improves performance for heavy tasks
- Uses multiple CPU cores
- Allows parallel task execution
- Helps build scalable programs
- Useful for CPU-bound operations

## Overall Disadvantages

- More complex than normal programming
- Uses more memory
- Requires careful process management
- Communication between processes can be difficult
- Debugging multiprocessing programs can be harder

## Final Summary

Chapter 3 explains how Python can run multiple processes at the same time using the `multiprocessing` module. It is useful for improving performance, especially for CPU-intensive tasks. However, multiprocessing requires careful handling of communication, synchronization, and process lifecycle.

---

# Important Code Note

In `communicating_with_queue.py`, the consumer checks `queue.empty()`. In real projects, this can be unreliable because the consumer may check the queue before the producer finishes adding items. A better method is to use a sentinel value such as `None` to tell the consumer when to stop.
