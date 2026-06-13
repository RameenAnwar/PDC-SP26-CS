# PDC-SP26-CS
Chapter 1:

Code:1 multiprocessing_test

This program shows Parallel Computing using multiprocessing library in Python.

The program creates 10 processes. Each process performs a task using the function do_something.

Instead of executing the task sequentially, multiple processes run simultaneously on different cores.

This reduces execution time  and improves performance.

The program also measures total execution time using time library.

Parallel processing divides a large task into smaller tasks and runs them at the same time. Using multiple processes can reduce execution time compared to serial execution.


Code:2 multithreading_test

This program demonstrates Multithreading using threading library in Python.

The program creates 10 threads. Each thread runs the function do_something.

All threads execute simultaneously and share the same memory space.

The program calculates execution time to show performance improvement.

Threads allow multiple tasks to run at the same time inside one program.

Threads share memory, so they are faster to create than processes.


Code:3 Serial

This program demonstrates Serial Computing.

The function do_something is executed 10 times sequentially using a single CPU.

Each task waits for the previous task to finish before starting.

The program measures total execution time using time library.

Serial computing executes tasks one after another.

It takes more time compared to parallel methods.
