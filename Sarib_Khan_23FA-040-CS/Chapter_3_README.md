# Chapter 3 – Process Management in Parallel Computing

In this chapter, I learned different ways of creating and managing processes in Python. I also learned communication between processes using pipes and queues, background processes, barriers, and process pools.

---

## Topic: spawning_processes.py

What I Learned
I learned how to create and start multiple processes in Python.

How to Execute
python spawning_processes.py

Use / Output
Creates processes and runs tasks separately.

When to Use
When multiple tasks need to run at the same time.

Advantages
Improves performance
Runs tasks independently

Disadvantages
Uses more system resources

Summary
Processes allow tasks to run in parallel.

---

## Topic: spawning_processes_namespace.py

What I Learned
I learned how namespaces work with processes and how variables behave separately.

How to Execute
python spawning_processes_namespace.py

Use / Output
Shows process-specific data handling.

When to Use
When processes need separate data storage.

Advantages
Better isolation

Disadvantages
Can become difficult to manage

Summary
Each process has its own memory space.

---

## Topic: process_in_subclass.py

What I Learned
I learned how to create processes using subclassing.

How to Execute
python process_in_subclass.py

Use / Output
Runs processes through custom classes.

When to Use
When creating reusable process logic.

Advantages
Better code organization

Disadvantages
Slightly difficult for beginners

Summary
Subclassing makes process management cleaner.

---

## Topic: naming_processes.py

What I Learned
I learned how to assign names to processes.

How to Execute
python naming_processes.py

Use / Output
Displays process names while running.

When to Use
When tracking multiple processes.

Advantages
Easy debugging
Better readability

Disadvantages
Extra setup needed

Summary
Naming helps identify processes easily.

---

## Topic: killing_processes.py

What I Learned
I learned how to terminate or stop processes.

How to Execute
python killing_processes.py

Use / Output
Starts and kills running processes.

When to Use
When a process needs to stop forcefully.

Advantages
Prevents unnecessary execution

Disadvantages
May lose unfinished work

Summary
Processes can be terminated when required.

---

## Topic: communicating_with_pipe.py

What I Learned
I learned how processes communicate using pipes.

How to Execute
python communicating_with_pipe.py

Use / Output
Sends data between processes.

When to Use
When two processes need communication.

Advantages
Simple communication method

Disadvantages
Limited flexibility

Summary
Pipes allow direct communication between processes.

---

## Topic: communicating_with_queue.py

What I Learned
I learned how queues are used for process communication.

How to Execute
python communicating_with_queue.py

Use / Output
Transfers data safely between processes.

When to Use
When multiple processes share data.

Advantages
Safe and organized communication

Disadvantages
Can slow execution slightly

Summary
Queues are useful for sharing data between processes.

---

## Topic: process_pool.py

What I Learned
I learned how process pools manage multiple workers automatically.

How to Execute
python process_pool.py

Use / Output
Executes tasks using worker processes.

When to Use
When many tasks need parallel execution.

Advantages
Cleaner code
Efficient management

Disadvantages
Less control over processes

Summary
Process pools simplify multiprocessing.

---

## Topic: processes_barrier.py

What I Learned
I learned about barriers and synchronization between processes.

How to Execute
python processes_barrier.py

Use / Output
Makes processes wait until all reach a point.

When to Use
When synchronization is required.

Advantages
Prevents timing issues

Disadvantages
Can slow overall execution

Summary
Barriers synchronize processes.

---

## Topic: run_background_processes.py

What I Learned
I learned about daemon/background processes.

How to Execute
python run_background_processes.py

Use / Output
Runs processes in background.

When to Use
When tasks should run silently in background.

Advantages
Useful for background services

Disadvantages
Stops when main program exits

Summary
Daemon processes work in the background.

---

## Topic: run_background_processes_no_daemons.py

What I Learned
I learned the difference between daemon and non-daemon processes.

How to Execute
python run_background_processes_no_daemons.py

Use / Output
Shows non-daemon process behavior.

When to Use
When processes must complete before program exits.

Advantages
Ensures task completion

Disadvantages
Program may take longer to close

Summary
Non-daemon processes continue until finished.

---

## Topic: myFunc.py

What I Learned
I learned how helper functions are reused in multiprocessing programs.

How to Execute
Used with other files.

Use / Output
Provides reusable functions.

When to Use
When common functionality is needed.

Advantages
Code reuse
Cleaner structure

Disadvantages
Can be confusing if separated too much

Summary
Helper functions improve organization.

---

## Final Understanding

In this chapter, I learned how processes are created, managed, synchronized, and communicated in parallel computing. I also understood process pools, barriers, pipes, queues, and background processes.