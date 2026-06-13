 # Chapter 03 - Process Based Parallelism

## 1. spawning_processes.py

**Topic:** Spawning Processes

**What is happening?**
Creates 6 separate processes using `multiprocessing.Process`. Each process runs `myFunc` which prints output based on its process number. Process 0 prints nothing, process 1 prints one line, process 2 prints two lines, and so on.

**How to run:**
python spawning_processes.py

**When to use:**
When you need to run the same function multiple times simultaneously as separate processes.

**Advantages:**
- Each process runs independently with its own memory
- True parallelism — not limited by Python's GIL

**Disadvantages:**
- More memory usage than threads — each process gets its own memory space
- Slower to start than threads

**End use:**
Foundation of multiprocessing — used when tasks are CPU-heavy and need to run truly in parallel.

---

## 2. spawning_processes_namespace.py

**Topic:** Process Namespace

**What is happening?**
Demonstrates how to pass shared data between processes using `multiprocessing.Manager` namespace — a shared memory space that multiple processes can read and write.

**How to run:**
python spawning_processes_namespace.py

**When to use:**
When multiple processes need to share and modify the same variables.

**Advantages:**
- Simple way to share data between processes
- Manager handles synchronization automatically

**Disadvantages:**
- Slower than direct memory access
- Adds overhead due to manager process

**End use:**
Used when parallel processes need to communicate results back to the main program.

---

## 3. process_in_subclass.py

**Topic:** Process as Subclass

**What is happening?**
Instead of passing a function to `Process`, a custom class inherits from `multiprocessing.Process` and overrides the `run()` method. This gives more control over process behavior.

**How to run:**
python process_in_subclass.py

**When to use:**
When your process logic is complex enough to need its own class with attributes and methods.

**Advantages:**
- Cleaner code structure for complex processes
- Can store state inside the class

**Disadvantages:**
- More boilerplate than simple function-based processes
- Overkill for simple tasks

**End use:**
Used in larger applications where processes need their own configuration and state.

---

## 4. naming_processes.py

**Topic:** Naming Processes

**What is happening?**
Assigns custom names to processes using the `name` parameter. Makes it easier to identify and debug which process is doing what in the output logs.

**How to run:**
python naming_processes.py

**When to use:**
When running multiple processes and you need to track which one is doing what — especially for debugging.

**Advantages:**
- Makes logs and debugging much clearer
- No performance overhead

**Disadvantages:**
- Just a label — doesn't change process behavior

**End use:**
Best practice in any multiprocessing application with more than 2-3 processes.

---

## 5. run_background_processes.py

**Topic:** Daemon Processes

**What is happening?**
Creates processes with `daemon=True`. A daemon process runs in the background and is automatically killed when the main program ends — it does not block the program from exiting.

**How to run:**
python run_background_processes.py

**When to use:**
For background tasks like logging, monitoring, or cleanup that should not keep the program alive.

**Advantages:**
- Program exits cleanly without waiting for background tasks
- Good for non-critical background work

**Disadvantages:**
- Daemon process is killed abruptly — cannot finish its work if main program exits
- Not suitable for tasks that must complete

**End use:**
Monitoring threads, background loggers, heartbeat signals in servers.

---

## 6. run_background_processes_no_daemons.py

**Topic:** Non-Daemon Processes

**What is happening?**
Same as above but `daemon=False` (default). The main program waits for all non-daemon processes to finish before exiting.

**How to run:**
python run_background_processes_no_daemons.py

**When to use:**
When background tasks must complete before the program can safely exit.

**Advantages:**
- Guarantees all processes finish their work
- Safe for critical tasks

**Disadvantages:**
- Program cannot exit until all processes are done
- Can hang if a process gets stuck

**End use:**
File processing, data writing, any task where incomplete work = data loss.

---

## 7. killing_processes.py

**Topic:** Terminating Processes

**What is happening?**
Shows how to forcefully stop a process using `process.terminate()`. The process is killed immediately regardless of what it was doing.

**How to run:**
python killing_processes.py

**When to use:**
When a process is stuck, taking too long, or its result is no longer needed.

**Advantages:**
- Immediate control over runaway processes
- Prevents resource waste

**Disadvantages:**
- Abrupt kill — process cannot clean up or save state
- Can cause data corruption if process was writing to a file

**End use:**
Timeout mechanisms, cancelling tasks when user requests stop, error recovery.

---

## 8. myFunc.py

**Topic:** Helper Function

**What is happening?**
A simple helper function imported and used by other files in this chapter to simulate workload inside a process.

**How to run:**
python myFunc.py
(No output — meant to be imported)

**When to use:**
Not run directly — imported by spawning_processes.py and others.

**Advantages:**
- Reusable across multiple files
- Keeps code organized

**Disadvantages:**
- No standalone use

**End use:**
Simulates a task for demonstrating process creation and management.

---

## 9. processes_barrier.py

**Topic:** Process Barrier

**What is happening?**
A `Barrier` forces multiple processes to wait at a checkpoint until ALL processes reach that point. Only then do they all continue together — like a sync point.

**How to run:**
python processes_barrier.py

**When to use:**
When parallel processes must complete a phase before any of them can move to the next phase — like all threads finishing data loading before processing starts.

**Advantages:**
- Ensures synchronization between processes
- Prevents one fast process from moving ahead while others are still working

**Disadvantages:**
- All processes are blocked waiting for the slowest one
- Can cause delays if one process is significantly slower

**End use:**
Scientific simulations, parallel data pipelines, any phase-based parallel work.

---

## 10. process_pool.py

**Topic:** Process Pool

**What is happening?**
`multiprocessing.Pool` creates a fixed number of worker processes. Tasks are distributed among them automatically — instead of creating a new process for every task, the pool reuses existing ones.

**How to run:**
python process_pool.py

**When to use:**
When you have many small tasks to run in parallel and don't want the overhead of creating a new process for each one.

**Advantages:**
- Efficient — processes are reused, not recreated
- Simple API with `pool.map()`
- Automatically distributes work

**Disadvantages:**
- Fixed pool size — may under or over-utilize resources
- All tasks must be defined before pool starts

**End use:**
Image processing, data transformation, any task where you apply the same function to a large list of items.

---

## 11. communicating_with_pipe.py

**Topic:** Inter-Process Communication — Pipe

**What is happening?**
Two processes communicate through a `Pipe` — a direct two-way connection. One process sends data, the other receives it. Like a phone call between two processes.

**How to run:**
python communicating_with_pipe.py

**When to use:**
When exactly two processes need to exchange data directly.

**Advantages:**
- Fast and simple for two-process communication
- Low overhead

**Disadvantages:**
- Only works between two processes
- If one end doesn't read, the other blocks

**End use:**
Producer-consumer patterns, data streaming between two stages of a pipeline.

---

## 12. communicating_with_queue.py

**Topic:** Inter-Process Communication — Queue

**What is happening?**
Multiple processes share a `Queue` to pass data safely. Producers put items in, consumers get items out. Queue handles synchronization automatically.

**How to run:**
python communicating_with_queue.py

**When to use:**
When multiple processes need to share data — more flexible than a pipe.

**Advantages:**
- Works with multiple producers and consumers
- Thread and process safe
- FIFO order guaranteed

**Disadvantages:**
- Slightly more overhead than a pipe
- Queue can fill up if consumers are slow

**End use:**
Task queues, work distribution systems, any pipeline with multiple workers.
