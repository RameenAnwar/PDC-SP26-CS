# Chapter 03 – Process Based Parallelism

## 1) communicating_with_pipe.py
This file demonstrates inter-process communication using Pipes, where two processes pass data to each other through a connection.

- **Pipe**: A two-way communication channel between processes.
- `multiprocessing.Pipe(True)` creates a duplex pipe with two ends.
- `create_items` sends numbers 0–9 through the first pipe using `output_pipe.send(item)`.
- `multiply_items` reads from the first pipe, squares each number, and sends results through the second pipe.
- The main process reads and prints the final squared values from the second pipe.
- `EOFError` is used to detect when the pipe is closed and no more data is coming.

**Advantages:**
- Simple and efficient for direct communication between two processes.
- Faster than queues for one-to-one communication.
- Easy to set up with minimal code.

**Disadvantages:**
- Only works well for two-process communication, not multiple.
- If one end is not closed properly, processes may hang indefinitely.
- No built-in buffering like a queue.

**Time behavior:**
- Execution depends on how fast each process sends and receives data.
- Processes run concurrently so total time is less than sequential.


## 2) communicating_with_queue.py
This file demonstrates inter-process communication using a Queue, implementing a Producer-Consumer model between processes.

- **Queue**: A thread and process-safe data structure for sharing data between processes.
- `producer` class extends `multiprocessing.Process` and adds 10 random integers to the queue.
- `consumer` class extends `multiprocessing.Process` and removes items from the queue one by one.
- Producer adds an item every 1 second; consumer waits 2 seconds before removing.
- Consumer checks `self.queue.empty()` to know when to stop.
- Both processes are started and joined to ensure proper completion.

**Advantages:**
- Built-in process safety, no need for manual locks.
- Easy way to share data between processes.
- Naturally models producer-consumer problems.

**Disadvantages:**
- Consumer may exit early if it checks empty before producer finishes.
- Timing mismatch between producer and consumer can cause issues.
- Slightly more overhead than pipes.

**Time behavior:**
- Total time depends on producer speed since consumer waits for items.
- Processes run concurrently so some overlap occurs.


## 3) killing_processes.py
This file demonstrates how to forcefully terminate a running process using `terminate()`.

- **terminate()**: Immediately stops a process without letting it finish.
- A simple function `foo()` loops 10 times with 1-second sleep, simulating work.
- The process is created, started, and then immediately terminated.
- `p.is_alive()` is used before and after termination to check process status.
- `p.join()` is called after termination to clean up the process.
- `p.exitcode` shows the exit status — a negative value means it was killed by a signal.

**Advantages:**
- Useful for stopping runaway or unresponsive processes.
- Simple and direct way to manage process lifecycle.
- `exitcode` helps verify how a process ended.

**Disadvantages:**
- Abrupt termination may leave shared resources in an inconsistent state.
- No cleanup or graceful shutdown of the process.
- Can cause data loss if the process was mid-operation.

**Time behavior:**
- Process is killed almost instantly, so execution time is very short.
- No waiting for the process to finish naturally.


## 4) myFunc.py
This file defines a simple helper function used by other scripts in this chapter.

- **myFunc**: A standalone function that prints its process number and loops based on the argument `i`.
- Takes one argument `i` and prints values from 0 to i-1.
- Imported and reused in `spawning_processes_namespace.py` to demonstrate modular process functions.
- Demonstrates how functions can be separated into their own module for reuse.

**Advantages:**
- Promotes code reuse and clean separation of logic.
- Easy to import and use across multiple scripts.

**Disadvantages:**
- Very basic function with no real-world complexity.
- Only useful as a demonstration helper.

**Time behavior:**
- Execution is very fast since it only prints values.


## 5) naming_processes.py
This file demonstrates how to assign custom names to processes for easier identification and debugging.

- **Process name**: A label given to a process to identify it during execution.
- `multiprocessing.Process(name='myFunc process', target=myFunc)` creates a named process.
- A second process is created without a name, getting a default system-assigned name.
- Both processes run the same `myFunc()` which prints the process name using `current_process().name`.
- `join()` ensures main thread waits for both processes to finish.

**Advantages:**
- Makes debugging easier by identifying which process is doing what.
- Useful in programs with many processes running simultaneously.
- No performance cost to naming processes.

**Disadvantages:**
- Only useful for identification, names don't affect behavior.
- Easy to forget to name processes in large programs.

**Time behavior:**
- Both processes run concurrently with a 3-second sleep each.
- Total time ≈ 3 seconds due to parallel execution.


## 6) process_in_subclass.py
This file demonstrates how to create processes using a custom class that extends `multiprocessing.Process`.

- **Subclassing Process**: Creating a class that inherits from `multiprocessing.Process` and overrides `run()`.
- `MyProcess` class overrides `run()` which is automatically called when the process starts.
- 10 instances of `MyProcess` are created, started, and joined in a loop.
- Each process prints its own name using `self.name`.
- `join()` ensures each process finishes before the next one starts.

**Advantages:**
- Clean and organized way to define process behavior using OOP.
- Makes it easy to add state and methods to a process.
- Reusable class for repeated process creation.

**Disadvantages:**
- Processes run sequentially here due to `join()` inside loop, limiting parallelism.
- More boilerplate than a simple function-based approach.

**Time behavior:**
- Processes run one after another due to immediate `join()`.
- Total time ≈ sum of all process execution times.


## 7) process_pool.py
This file demonstrates parallel task execution using a Process Pool, distributing work across multiple processes.

- **Pool**: Manages a fixed number of worker processes to execute tasks in parallel.
- `multiprocessing.Pool(processes=4)` creates a pool with 4 worker processes.
- `pool.map(function_square, inputs)` distributes the input list across the 4 processes.
- Each worker computes the square of its assigned number.
- `pool.close()` stops accepting new tasks; `pool.join()` waits for all workers to finish.
- Results are returned in the same order as the input list.

**Advantages:**
- Efficiently distributes work across multiple CPU cores.
- Much faster than running tasks one by one for large inputs.
- `map()` handles task distribution and result collection automatically.

**Disadvantages:**
- Pool size must be chosen carefully — too many processes waste resources.
- Overhead of creating and managing the pool for small tasks.
- Not suitable for tasks that need shared state between processes.

**Time behavior:**
- With 4 processes and 100 inputs, workload is split into chunks.
- Faster than sequential execution for large datasets.


## 8) processes_barrier.py
This file demonstrates process synchronization using a Barrier, ensuring multiple processes reach a checkpoint before continuing.

- **Barrier**: Forces a set of processes to wait until all of them reach a specific point.
- `Barrier(2)` means 2 processes must call `wait()` before any of them proceed.
- `test_with_barrier()` uses `synchronizer.wait()` to pause until both processes arrive.
- `test_without_barrier()` runs freely with no synchronization.
- A `Lock` (serializer) is used to prevent overlapping print statements.
- The timestamps show that barrier processes print nearly the same time, while non-barrier ones differ.

**Advantages:**
- Guarantees synchronized start for a group of processes.
- Useful in parallel algorithms with multiple phases.
- Easy to implement with `multiprocessing.Barrier`.

**Disadvantages:**
- All processes must wait for the slowest one.
- If one process never reaches the barrier, others wait forever.
- Only useful when synchronization between processes is actually needed.

**Time behavior:**
- Barrier processes finish together, so total time = slowest process time.
- Non-barrier processes finish independently based on their own speed.


## 9) run_background_processes_no_daemons.py
This file demonstrates non-daemon processes, where background processes are allowed to fully complete even after the main process finishes.

- **daemon = False**: The process is not a daemon, so it runs to completion regardless of the main process.
- Two processes (`background_process` and `NO_background_process`) both have `daemon = False`.
- Each process checks its name and prints numbers in a loop with a 1-second sleep.
- Both processes run until they fully complete, even if the main process exits.
- This is the default behavior in Python's `multiprocessing`.

**Advantages:**
- Ensures all work is completed before the program fully exits.
- Safe for tasks that must not be interrupted.

**Disadvantages:**
- Main program won't exit until all non-daemon processes finish.
- Can delay program termination if processes are long-running.

**Time behavior:**
- Total time depends on how long each process runs.
- Both processes run concurrently, so time ≈ longest process duration.


## 10) run_background_processes.py
This file demonstrates daemon processes, where the background process is automatically killed when the main process exits.

- **daemon = True**: Marks a process as a daemon — it will be killed when the main process ends.
- `background_process.daemon = True` means it may not finish if main exits first.
- `NO_background_process.daemon = False` runs to completion normally.
- This is the key difference from the previous file — one process may be cut short.
- Useful for background tasks like logging or monitoring that shouldn't block program exit.

**Advantages:**
- Daemon processes don't prevent the program from exiting.
- Useful for background tasks that are not critical to complete.
- Automatically cleaned up when main process ends.

**Disadvantages:**
- Daemon process may be killed mid-execution, losing incomplete work.
- Not suitable for tasks that must finish fully.

**Time behavior:**
- Non-daemon process runs to completion; daemon may be cut short.
- Total program time is controlled by the non-daemon process.


## 11) spawning_processes_namespace.py
This file demonstrates spawning processes using a function imported from a separate module (`myFunc.py`).

- **Importing from module**: `myFunc` is imported from `myFunc.py` instead of being defined inline.
- 6 processes are created in a loop, each calling `myFunc` with a different argument.
- Each process is started and immediately joined, so they run sequentially.
- Demonstrates how to organize process functions into separate files for cleaner code.

**Advantages:**
- Encourages modular and clean code organization.
- Reusable function across multiple scripts.

**Disadvantages:**
- Sequential execution due to `join()` inside loop.
- No real parallelism demonstrated here.

**Time behavior:**
- Processes run one at a time, total time ≈ sum of all executions.


## 12) spawning_processes.py
This file demonstrates the basic way to spawn multiple processes using `multiprocessing.Process`.

- **Spawning**: Creating and starting a new process to run a function independently.
- `myFunc` is defined inline and prints values based on the argument `i`.
- 6 processes are created in a loop with `i` from 0 to 5.
- Each process is started with `start()` and waited on with `join()`.
- This is the most fundamental example of creating processes in Python.

**Advantages:**
- Simple and straightforward process creation.
- Good starting point for understanding multiprocessing.

**Disadvantages:**
- `join()` inside loop makes execution sequential, not parallel.
- No data sharing or synchronization demonstrated.

**Time behavior:**
- Sequential due to immediate `join()`, total time = sum of all process times.