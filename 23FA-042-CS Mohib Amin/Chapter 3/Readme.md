
CHAPTER 3

## How To Execute : Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)


--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: spawning_processes.py / spawning_processes_namespace.py

## Description
This script demonstrates the basic spawning of multiple processes. 
It uses a loop to create and start separate process instances that execute a specific function with varying arguments.

## When to Execute
Execute this to understand the fundamental lifecycle of a process, including creation (Process), execution (start), and waiting for completion (join).

## What We Learned
- How to pass arguments to a process using the args parameter.
- The use of process.join() to ensure the main program waits for a process to finish before continuing.

## Advantages
- Simple syntax for offloading tasks to different CPU cores.
- join() provides a clean way to synchronize process completion.

## Disadvantages
- Spawning and joining in a strict loop results in sequential execution rather than true parallelism.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: process_pool.py

## Description
This code utilizes a Process Pool to handle data parallelism.
It distributes a list of input values across a fixed number of worker processes (4) to perform calculations (squaring numbers) concurrently.

## When to Execute
Use this when you have a large dataset and a uniform function to apply to every element.

## What We Learned
- How to use multiprocessing.Pool and the map function.
- Managing a pool with close() and join().

Advantages
- Highly efficient for batch processing.
- Automatically handles the distribution of tasks among available workers.

Disadvantages
- High memory overhead if the input data or returned results are exceptionally large.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: communicating_with_pipe.py

## Description
This script demonstrates communication between processes using Pipes. 
It creates a pipeline where one process generates data, a second process transforms it by multiplying items, and the main process receives and prints the result.

## How and When to Execute
Run the program using "python communicating_with_pipe.py". Execute this when you need a direct, synchronized communication link between two specific process endpoints.

## What We Learned
- How to initialize a multiprocessing.Pipe and handle its connection objects.
- Sending and receiving data using the send() and recv() methods.
- The importance of closing unused pipe ends to avoid any issues.

## Advantages
- Provides a very fast, low-latency communication channel for point-to-point data transfer.
- Simple to implement for solving a basic producer-consumer problem.
- Supports duplex communication if the Pipe is initialized as True.

## Disadvantages
- Not thread-safe; data may become corrupted if two processes try to read from or write to the same end at once.
- Limited to communication between only two endpoints.
- Can lead to deadlocks if a process tries to read from an empty pipe or write to a full one without proper synchronization.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: communicating_with_queue.py

## Description
This script implements a Producer-Consumer pattern using a Queue. 
A producer process appends random integers to the queue, while a consumer process pops and prints them.

## How and When to Execute
Run the program using "python communicating_with_queue.py". Execute this when multiple processes need to share data safely without manual locking.

## What We Learned
- How to use multiprocessing.Queue to share data between processes.
- Implementing process logic within the run() method of a subclassed Process.
- Using put() and get() to manage shared data flow.

## Advantages
- Queues are both thread and process safe, handling internal locking automatically.
- Easily scales to handle multiple producers and multiple consumers.
- Helps decouple the data generation logic from the data processing logic.

## Disadvantages
- Higher overhead compared to pipes due to the internal synchronization and locking mechanisms.
- Can consume significant memory if the producer outpaces the consumer and the queue grows unchecked.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: killing_processes.py

## Description
This code demonstrates how to monitor and forcefully terminate a running process. 
It starts a function, checks its status, and then kills it immediately using the terminate method.

## How and When to Execute
Run the program using "python killing_processes.py". Execute this when you need to programmatically stop a process that is no longer needed or is hanging.

## What We Learned
- How to use the terminate() method to stop a process.
- Using is_alive() to check the current state of a process.
- Inspecting the exitcode to see how a process ended.

## Advantages
- Provides a way to stop "runaway" processes or tasks that have exceeded their time limit.
- Allows the main program to regain control over system resources quickly.

## Disadvantages
- Abrupt termination can leave shared resources (like locks) in a corrupted or "stuck" state.
- Does not allow the child process to perform any cleanup or "exit" logic.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: naming_processes.py

## Description
This script shows how to assign custom names to processes for easier identification. 
It creates one process with a specific name and another with a default system-generated name.

## How and When to Execute
Run the program using "python naming_processes.py". Execute this when building complex systems where tracking which process is doing what is essential for debugging.

## What We Learned
- How to use the 'name' argument in the Process constructor.
- Retrieving the current process name using multiprocessing.current_process().name.

## Advantages
- Significantly improves logs and makes debugging much easier by identifying specific tasks.
- Helps in monitoring system resources by associating PIDs with readable names.

## Disadvantages
- Names are not unique; multiple processes can share the same name, which may cause confusion.
- Adds a small amount of extra boilerplate code for each process creation.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: process_in_subclass.py

## Description
This code demonstrates how to create a process by subclassing the multiprocessing.Process class. 
It overrides the run() method to define the task the process will execute.

## How and When to Execute
Run the program using "python process_in_subclass.py". Execute this when you want to use an object-oriented approach to manage complex process logic and state.

## What We Learned
- How to inherit from multiprocessing.Process.
- The importance of the run() method as the entry point for the process.

## Advantages
- Encourages clean, modular code by encapsulating process logic within a class.
- Makes it easier to maintain internal state or variables specific to a single process.

## Disadvantages
- Slightly more complex and verbose than passing a target function to a standard Process object.
- Can lead to confusion regarding which variables are shared and which are local to the process.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: processes_barrier.py

## Description
This script demonstrates the use of a Barrier to synchronize multiple processes. 
It forces specific processes to wait until a required number of them have reached the barrier before allowing them to proceed together.

## How and When to Execute
Run the program using "python processes_barrier.py". Execute this when concurrent tasks must be strictly aligned in time before starting a new phase of execution.

## What We Learned
- Using multiprocessing.Barrier to manage process synchronization.
- Using a Lock (serializer) to prevent multiple processes from printing to the console at the same time.

## Advantages
- Ensures that all parallel components of a task are ready before the next step begins.
- Useful for parallel algorithms that operate in discrete, synchronized stages.

## Disadvantages
- Risks a deadlock if one process crashes or fails to reach the barrier, as all others will wait indefinitely.
- Can decrease performance if processes have highly variable execution times (the fastest must wait for the slowest).

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: run_background_processes.py / run_background_processes_no_daemons.py

## Description
This script explains the concept of Daemon processes. 
It compares a background (daemon) process, which exits when the main program stops, with a non-daemon process that continues until its task is done.

## How and When to Execute
Run the program using "python run_background_processes.py". Execute this when you have background tasks (like logging or monitoring) that shouldn't block the program from closing.

## What We Learned
- How to set the daemon attribute to True or False.
- How the lifecycle of the main process affects daemonized child processes.

## Advantages
- Prevents "zombie" processes from staying alive after the main application has closed.
- Ideal for non-critical services that only need to run while the main app is active.

## Disadvantages
- Daemon processes are killed instantly without executing 'finally' blocks or closing files properly.
- Cannot be used for tasks that must guarantee data integrity or completion.