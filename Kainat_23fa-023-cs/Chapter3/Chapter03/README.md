## communicating_with_pipe:

This program demonstrates inter-process communication using Pipes in Python multiprocessing.

The first process creates numbers from 0 to 9 and sends them through a pipe.

The second process receives these numbers from the first pipe, calculates the square of each number, and sends the results through another pipe.

The main process receives the squared values from the second pipe and prints them.

The multiprocessing.Pipe() function is used for communication between processes.

Important concepts in this program:
Process-based parallelism
Inter-process communication (IPC)
Pipes in multiprocessing
Sending and receiving data between processes

Pipes allow multiple processes to exchange data efficiently. One process can produce data while another process processes and transfers the results to the main program.

## communicating_with_queue:

This program demonstrates the Producer-Consumer problem using Python multiprocessing and queues.

A producer process generates random numbers and stores them in a shared queue.

A consumer process retrieves items from the queue and removes them one by one.

The multiprocessing.Queue() function is used for safe communication and data sharing between processes.

The producer continuously adds data to the queue, while the consumer reads and processes the data independently.

Important concepts in this program:
Process-based parallelism
Producer-Consumer model
Inter-process communication (IPC)
Shared queue in multiprocessing
Synchronization between processes

Queues allow multiple processes to safely exchange data. The producer adds items to the queue, and the consumer removes and processes them without directly sharing memory.

## killing_process

This program demonstrates process creation and termination using Python multiprocessing.

A separate process is created to execute the foo() function, which prints numbers from 0 to 9 with a delay.

The program checks the process status before execution, during execution, and after termination using the is_alive() method.

The terminate() function is used to stop the process before it finishes normally.

Finally, join() waits for the process to completely stop, and the exit code is displayed.

Important concepts in this program:
 Process creation
 Process execution
 Process termination
 Checking process status
 Joining processes

Processes can be controlled during execution using multiprocessing functions like start(), terminate(), and join(). The is_alive() method helps monitor whether a process is currently running or stopped.

## naming_processes

This program demonstrates how to create and manage processes with custom and default names in Python multiprocessing.

Two separate processes are created to execute the same function.

The first process is assigned a custom name, while the second process uses the default process name provided by Python.

The current_process().name function is used to display the name of the running process.

Each process starts, waits for 3 seconds, and then exits.

Important concepts in this program:
Process creation
Custom process naming
Default process naming
Current process identification
Process execution and joining

Processes in multiprocessing can be given custom names to make process management and debugging easier. Python also automatically assigns default names if no custom name is provided.

## process_pool

## USING A PROCESS POOL

This program demonstrates the use of a Process Pool in Python multiprocessing.

A pool of 4 worker processes is created to perform parallel computation.

The program calculates the square of numbers from 0 to 99 using the function_square() function.

The pool.map() method distributes the input data among multiple processes automatically and collects the results.

After completing the tasks, the pool is closed and joined properly.

Important concepts in this program:
 Process Pool
 Parallel task execution
 Worker processes
 Data distribution using map()
 Multiprocessing optimization

A Process Pool allows multiple tasks to run in parallel using a fixed number of worker processes. It simplifies parallel programming and improves performance for large computations.

## processes_barrier

This program demonstrates process synchronization using Barrier and Lock in Python multiprocessing.

Two processes use a Barrier object, which forces them to wait until both processes reach the synchronization point before continuing execution.

A Lock object is used to ensure that only one process prints output at a time, preventing mixed or overlapping text on the screen.

The other two processes execute without synchronization, so they run independently without waiting.

The program also displays the execution time of each process.

Important concepts in this program:
Process synchronization
Barrier in multiprocessing
Lock mechanism
Coordinated process execution
Parallel process behavior

A Barrier allows multiple processes to synchronize and continue execution together only after all required processes reach the same point. Locks help manage safe access to shared resources like console output.

## run_background_processes_no_daemons

This program demonstrates the difference between daemon-like behavior and normal processes using Python multiprocessing.

Two processes are created with different names: one acts like a background process and the other as a normal process.

Each process executes the same function but performs different loops based on its process name.

The program shows how processes can run independently and execute different logic depending on their identity.

Although the daemon attribute is set to False for both processes, the example is used to demonstrate how background-style execution can be simulated.

Important concepts in this program:
 Process creation with custom names
 Background vs normal process behavior
 Process identification using current_process().name
 Conditional execution in processes
 Multiprocessing execution flow

Processes can behave differently based on their role or name. Python allows customization of process behavior, and daemon processes (when used) run in the background without blocking the main program.

## run_background_process

This program demonstrates the concept of daemon and non-daemon processes in Python multiprocessing.

Two processes are created with different roles: one is set as a daemon process and the other as a normal (non-daemon) process.

The daemon process runs in the background and is terminated automatically when the main program finishes execution.

The non-daemon process runs independently and completes its execution normally.

Each process prints numbers based on its assigned name and shows how execution differs between background and normal processes.

Important concepts in this program:
 Daemon processes
 Non-daemon processes
 Background execution
 Process lifecycle control
 Process naming and identification

Daemon processes run in the background and do not block program termination, while non-daemon processes must complete before the program fully exits. This helps manage background tasks efficiently.

## spawning_process

## SPAWNING MULTIPLE PROCESSES

This program demonstrates how to spawn multiple processes using Python multiprocessing.

A function named myFunc is executed in separate processes, where each process receives a different input value.

Each process prints its process number and then runs a loop based on the given argument.

The program creates 6 processes using a loop, but each process is started and joined immediately.

Important concepts in this program:
 Process spawning
 Creating multiple processes using loops
 Passing arguments to processes
 Process execution flow
 Sequential execution using join()

Processes can be spawned dynamically to perform tasks independently, but using join() immediately after start() makes them run one by one instead of in parallel.

