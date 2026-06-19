
# CHAPTER 3 — PROCESS BASED PARALLELISM (MULTIPROCESSING)

A collection of Python programs demonstrating multiprocessing concepts, including process creation, synchronization, communication, process pools, pipes, queues, and process lifecycle management.


--- 

## How to Run Any Program

```bash
python filename.py
```
---
| File | Concept |
|------|---------|
| `myFunc.py` | Basic function used in multiprocessing |
| `spawning_processes.py` | Creating multiple processes |
| `process_subclass.py` | Custom process class |
| `naming_processes.py` | Process naming and identification |
| `killing_process.py` | Process lifecycle management |
| `run_background_process.py` | Daemon processes |
| `run_background_process_non_da   emon.py` | Non-daemon processes |
| `process_pool.py` | Process pools |
| `communicating_with_pipe.py` | IPC using Pipes |
| `communicating_with_queue.py` | Producer-consumer using Queue |
| `process_barrier.py` | Barrier and Lock synchronization |

---
## communicating_with_pipe.py

**Description**
This program demonstrates inter-process communication using Pipes.

**Execution Method**
Run the command python communicating_with_pipe.py

**Use Case**

Useful for sending data between processes

**Observations**

Pipes provide two-way communication
Data flows between connected processes

**Advantages**

Simple communication method
Fast data transfer

**Disadvantages**

Limited to two endpoints
Requires careful synchronization
---

## communicating_with_queue.py

**Description:**
Producer-consumer problem using Queue.

**Execution Method:**

python communicating_with_queue.py

**Use Case:**

Safe data sharing between processes

**Observations:**

Producer uses put()
Consumer uses get()

**Advantages:**

Safe and easy
Supports multiple processes

**Disadvantages:**

Memory overhead possible

---
## killing_process.py

**Description:**
This program demonstrates process lifecycle including start, terminate, join, and exit code.

**Execution Method:**

python killing_process.py

**Use Case:**

Useful for controlling process execution

**Observations:**

start() begins execution
terminate() stops process forcefully
exitcode shows termination status

**Advantages:**

Full control over process execution
Useful for system-level programs

**Disadvantages:**

Force termination may leave incomplete execution
Debugging is difficult

---
## myFunc.py


**Description:**
This function is used in multiple multiprocessing programs. It prints the process name and generates output based on the input value.

**Execution Method:**
Run indirectly through multiprocessing scripts.

**Use Case:**

Used as a worker function for multiple processes
Helps understand parameter passing in multiprocessing

**Observations:**

Each process executes independently
Output depends on input argument

**Advantages:**

Simple reusable function
Useful for testing multiprocessing behavior

**Disadvantages:**

No return value handling
Output may be unordered in parallel execution

---

## naming_process.py

**Description:**
This program demonstrates assigning custom and default names to processes.

**Execution Method:**

python filename.py

**Use Case:**

Useful for debugging and identifying processes

**Observations:**

current_process().name retrieves process name
Custom and default naming supported

**Advantages:**

Improves debugging
Easier process tracking

**Disadvantages:**

Output order may vary

---

## process_subclass.py

**Description:**
This program demonstrates creating a custom process class by inheriting from multiprocessing.Process.

**Execution Method:**

python process_in_subclass.py

**Use Case:**

Useful for object-oriented multiprocessing design

**Observations:**

run() method defines process behavior
Each object acts as an independent process

**Advantages:**

Clean and structured design
Easy to extend functionality

**Disadvantages:**

Slightly more complex than function-based processes
Sequential execution if joined inside loop

---

## process_pool.py

**Description:**
This program demonstrates process pooling using multiprocessing.Pool.

**Execution Method:**

python process_pool.py

**Use Case:**

Useful for parallel execution of large datasets

**Observations:**

map() distributes work automatically
Results are returned in order

**Advantages:**

Easy parallel execution
Efficient resource usage

**Disadvantages:**

Less control over individual processes
---

## process_barrier.py

**Description:**
Demonstrates synchronization using Barrier and Lock.

**Execution Method:**

python process_barrier.py

**Use Case:**

Coordinating multiple processes

**Observations:**

Barrier synchronizes execution
Lock ensures safe output

**Advantages:**

Prevents race conditions

**Disadvantages:**

Risk of deadlock

---

## run_background_process.py

**Description:**
This program demonstrates the difference between daemon and non-daemon processes using the multiprocessing module. It shows how background processes behave differently from normal processes.

**Execution Method:**
Run the command python run_background_process.py

**Use Case:**

Useful for understanding background tasks in multiprocessing.
Demonstrates process lifecycle and termination behavior.

**Observations:**

A daemon process runs in the background and may terminate automatically when the main program ends.
A non-daemon process runs independently and completes its execution.
current_process().name is used to identify the running process.
Process behavior depends on the daemon flag.

**Advantages:**

Helps understand background vs foreground processing.
Useful for designing task management systems.
Demonstrates real multiprocessing behavior.

**Disadvantages:**

Daemon processes may terminate abruptly without completing tasks.
Can lead to incomplete output if not handled carefully.
Requires careful design to avoid unexpected termination.



---

## run_background_process_non_daemon.py

**Description:**
This program demonstrates multiprocessing using two non-daemon processes. Both processes run independently and complete their execution without being terminated by the main program.

**Execution Method:**
Run the command python filename.py

**Use Case:**

Useful for understanding normal process behavior in multiprocessing.
Demonstrates parallel execution without background termination.

**Observations:**

Non-daemon processes run independently and complete fully.
Both processes execute in parallel.
current_process().name helps identify running processes.
Execution order is not guaranteed due to concurrency.

**Advantages:**

Reliable execution of all processes.
No risk of premature termination.
Suitable for important tasks.

**Disadvantages:**

May consume more system resources.
Output order is unpredictable.
No automatic cleanup like daemon processes.

---

## spawning_processes.py

**Description:**
This program demonstrates process creation using the spawn method in Python's multiprocessing module. It creates multiple processes in a loop, each executing a function with different input values.

**Execution Method:**
Run the command python spawning_processes.py

**Use Case:**

Useful for understanding dynamic process creation.
Helps in learning how multiple processes are spawned and executed.

**Observations:**

Processes are created using a loop with multiprocessing.Process.
Each process receives a unique argument using args.
start() begins execution of each process.
join() ensures one process completes before the next starts.
Due to join() inside the loop, execution becomes sequential.

**Advantages:**

Simple way to understand process creation.
Demonstrates parameter passing to processes.
Good for learning multiprocessing basics.

**Disadvantages:**

No real parallel execution due to join() in loop.
Less efficient for large workloads.
Does not fully utilize multiprocessing power.

---
## spawning_namespace.py

**Description:**
This program demonstrates multiprocessing using an external function imported from another file. It creates multiple processes in a loop and executes the imported function with different arguments.

**Execution Method:**
Run the command python spawning_namespace.py

**Use Case:**

Useful for modular programming in multiprocessing.
Demonstrates how functions from external files can be used in processes.

**Concepts Learned/Observations:**

Functions can be imported from external modules for multiprocessing.
Each process runs independently using multiprocessing.Process.
start() begins execution of the process.
join() ensures one process finishes before the next begins.
Execution becomes sequential due to join() inside the loop.

**Advantages:**

Encourages modular and reusable code.
Easy to manage functions separately.
Useful for organizing large multiprocessing programs.

**Disadvantages:**

No parallel execution due to immediate join().
Depends on external file availability (myFunc.py).
Less efficient for large-scale processing.

---



