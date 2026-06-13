# Chapter # 3

---

## 1. communicating_with_pipe.py

### Description:
Pipes are used for communication between two processes. One process sends numbers 0-9 through a pipe, another receives them, squares them, and sends results through a second pipe. EOFError signals when data transfer is complete.

### How it Works:
- `create_items` sends numbers 0-9 through pipe_1
- `multiply_items` receives from pipe_1, squares each number, sends to pipe_2
- Main process receives and prints squared values from pipe_2
- EOFError is caught to detect end of data

### Result:
Prints squared values of 0-9 (0, 1, 4, 9, 16... 81) then prints "End".

### Advantages:
- Fast and lightweight communication between two processes
- Simple to implement for linear data pipelines

### Disadvantages:
- Only works between two endpoints
- Not suitable for multiple processes sharing same pipe

### Where to Use:
- Data processing pipelines where one process feeds into another
- Any two-process communication scenario

---

## 2. communicating_with_queue.py

### Description:
A multiprocessing Queue is used for safe communication between Producer and Consumer processes. Producer adds random numbers to queue, Consumer removes them with timing delays to simulate real processing.

### How it Works:
- Producer generates 10 random integers (0-256) and puts them in queue
- Consumer checks if queue is empty — if not, pops items one by one
- Both run as separate processes simultaneously
- Queue size is printed after each addition

### Result:
Producer appends items and Consumer pops them, printing each action with process name and item value.

### Advantages:
- Process-safe — multiple producers/consumers can use it
- Built-in size checking prevents overflow

### Disadvantages:
- Slower than Pipe due to internal locking overhead
- Consumer may check queue before producer finishes adding items

### Where to Use:
- Task queues in web servers
- Data pipelines between multiple processes

---

## 3. killing_processes.py

### Description:
Demonstrates how to control a process lifecycle — starting, terminating, and checking its status using is_alive() and exitcode properties.

### How it Works:
- Process is created with `foo` as target function
- `p.start()` starts the process
- `p.terminate()` immediately kills it before loop finishes
- `p.join()` waits for cleanup
- exitcode -15 confirms forced termination

### Result:
Prints process status at each stage — before execution, running, terminated, and joined with exit code.

### Advantages:
- Full control over process lifecycle
- Can forcefully stop stuck or timed-out processes

### Disadvantages:
- Forceful termination may leave shared resources in inconsistent state
- No graceful cleanup of process tasks

### Where to Use:
- Stopping runaway processes in servers or schedulers
- Timeout handling in parallel applications

---

## 4. myFunc.py

### Description:
A simple reusable worker function that prints its process number and loops through a range based on the input argument. Used as a target function by other process files.

### How it Works:
- Takes integer `i` as argument
- Prints which process number called it
- Loops from 0 to i and prints each output value

### Result:
Prints process number and loop output values. No output when run alone — must be called by another file.

### Advantages:
- Reusable across multiple files without rewriting
- Clean separation of worker logic from process management

### Disadvantages:
- Produces no output when run alone
- Depends on being imported by another file

### Where to Use:
- As a worker function passed to spawned processes
- Reusable task function in multiprocessing projects

---

## 5. naming_processes.py

### Description:
Demonstrates how to assign custom names to processes and retrieve them during execution using current_process().name.

### How it Works:
- Two processes created — one with custom name `myFunc process`, one with default name
- Both run same `myFunc` function
- Each prints its name on start and exit with a 3 second sleep in between

### Result:
Prints starting and exiting messages with process names — one custom, one system-assigned default name.

### Advantages:
- Makes logs and debug output much clearer
- Easy to distinguish between multiple running processes

### Disadvantages:
- Names are only labels — do not affect process behavior or priority

### Where to Use:
- Debugging and logging in multi-process applications
- Identifying specific processes in complex parallel programs

---

## 6. process_in_subclass.py

### Description:
Demonstrates creating a custom process by subclassing multiprocessing.Process and overriding the run() method with custom behavior.

### How it Works:
- `MyProcess` class inherits from `multiprocessing.Process`
- `run()` method is overridden to print the process name
- 10 instances created in a loop, each started and joined one by one

### Result:
Prints "called run method in Process-N" for each of the 10 processes sequentially.

### Advantages:
- Clean OOP design — logic encapsulated in a class
- Easy to extend with additional attributes and methods

### Disadvantages:
- More boilerplate code than simple function-based processes
- join() inside loop makes execution sequential not parallel

### Where to Use:
- When each process needs its own encapsulated logic
- Complex worker types in distributed systems

---

## 7. process_pool.py

### Description:
Demonstrates multiprocessing.Pool to distribute a function across multiple worker processes and collect all results using pool.map().

### How it Works:
- `function_square` returns square of input
- Pool of 4 workers created
- `pool.map()` distributes inputs 0-99 across workers
- Results collected and printed as a list

### Result:
Prints a list of squared values from 0 to 9801 (squares of 0-99).

### Advantages:
- Efficient reuse of fixed number of processes
- Automatically handles task distribution and result collection

### Disadvantages:
- All inputs must be available upfront
- Not suitable for dynamic or streaming data

### Where to Use:
- Parallel data processing and transformations
- Applying same function to large datasets

---

## 8. processes_barrier.py

### Description:
Demonstrates Barrier synchronization — two processes wait for each other before printing timestamp, while two others run freely without waiting.

### How it Works:
- `synchronizer = Barrier(2)` created for 2 processes
- p1 and p2 call `synchronizer.wait()` — both wait until other arrives
- p3 and p4 run without barrier — print at different times
- Lock ensures timestamps are printed one at a time

### Result:
p1 and p2 print almost same timestamp. p3 and p4 print at different times showing no synchronization.

### Advantages:
- Guarantees synchronized execution at a checkpoint
- Useful for phased parallel tasks

### Disadvantages:
- If one process fails to reach barrier, all others wait indefinitely
- Not flexible for dynamic number of processes

### Where to Use:
- Parallel simulations where phases must complete together
- Scientific computing with staged calculations

---

## 9. run_background_processes.py

### Description:
Demonstrates non-daemon processes (daemon=False) — both processes run their full loops even after main program would otherwise exit.

### How it Works:
- Two processes created — both with daemon=False
- background_process prints 0-4, NO_background_process prints 5-9
- Both run simultaneously and complete fully
- Program only exits after both finish

### Result:
Both processes print their ranges completely with starting and exiting messages.

### Advantages:
- Guarantees all processes complete their work
- Safe for tasks that must not be interrupted

### Disadvantages:
- Main program cannot exit until all non-daemon processes finish
- May cause delays if processes take long

### Where to Use:
- Tasks that must complete fully like saving data or cleanup operations

---

## 10. run_background_processes_no_daemons.py

### Description:
Demonstrates daemon=True process — daemon process is automatically killed when main process ends, while non-daemon process completes fully.

### How it Works:
- background_process has daemon=True — killed when main exits
- NO_background_process has daemon=False — runs to completion
- Both start simultaneously but daemon may not finish its full loop

### Result:
NO_background_process completes fully. background_process may be killed mid-execution when main program exits.

### Advantages:
- Daemon processes clean up automatically — no manual termination needed
- Useful for optional background tasks

### Disadvantages:
- Daemon process may be killed mid-task risking incomplete execution
- Cannot guarantee daemon process completes its work

### Where to Use:
- Background monitoring or logging that should stop when app exits
- Optional helper processes that are not critical to complete

---

## 11. spawning_processes_namespace.py

### Description:
Demonstrates spawning multiple processes using a function imported from a separate file (myFunc.py), keeping logic and process management separated.

### How it Works:
- `myFunc` imported from myFunc.py
- Loop creates 6 processes, each with argument i (0 to 5)
- Each process starts and joins before next one begins

### Result:
Prints process number and loop output for each of 6 processes sequentially.

### Advantages:
- Clean code organization — worker logic in separate file
- Reusable function without rewriting code

### Disadvantages:
- File dependency — crashes if myFunc.py is missing
- join() inside loop prevents true parallelism

### Where to Use:
- Large projects with separate worker modules
- Reusable multiprocessing task functions

---

## 12. spawning_processes.py

### Description:
Demonstrates spawning multiple processes using a function defined in the same file, running the same task with different arguments.

### How it Works:
- `myFunc` defined in same file
- Loop creates 6 processes with arguments 0 to 5
- Each process started and joined one by one inside loop

### Result:
Prints process number and loop output for each of 6 processes from i=0 to i=5 sequentially.

### Advantages:
- Simple and self-contained — no external file dependencies
- Easy to understand for beginners

### Disadvantages:
- join() inside loop makes processes sequential not parallel
- Function must be redefined if used in another file

### Where to Use:
- Basic parallel task execution with different inputs
- Learning and testing multiprocessing concepts

---