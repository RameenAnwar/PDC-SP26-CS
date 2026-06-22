**************************************************************************************************
**Chapter: 01       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## Multiprocessing
Multiprocessing is a technique in Python that allows a program to execute multiple processes simultaneously. Unlike threading, multiprocessing uses separate memory spaces and fully utilizes multiple CPU cores, making it ideal for CPU-bound tasks.

### Process
A process is an independent execution unit with its own memory space.

### Parallel Execution
Multiple processes run at the same time, improving performance for heavy computations.

### Multiprocessing Module
Python provides the multiprocessing module to create processes, start execution and synchronize completion.

### Code Interpretation
*Importing Modules*
- multiprocessing => for parallel processing
- time => for performance measurement
- do_something => user-defined function executed by each process

*Main Execution Block*
if __name__ == "__main__":
- It prevents unintended recursive process creation.
- Required for multiprocessing (especially on Windows).

*Creating Processes*
process = multiprocessing.Process(target=do_something, args=(size, out_list))
- Defines a process.
- Assigns a function (do_something) to run.
- Passes arguments to that function.

*Starting Processes*
j.start() **Begins execution of each process.**
*Synchronization*
j.join() **Ensures the main program waits until all processes complete.**

*Performance Measurement*
start_time = time.time()
end_time = time.time()
**Used to calculate total execution time i.e. (start_time - end_time).**

* out_list = list()
Creates an empty list to store output from the process.
*Note* 
This list is not shared across processes (each process gets its own copy). To share data between processes, queue or pipe can be used.

### Advantages of Multiprocessing
- Parallelism (uses multiple CPU cores)
- Faster execution for CPU-bound tasks
- Better performance for larger computations

### Limitations
- Higher memory usage
- Inter-process communication is complex
- Overhead of process creation

**************************************************************************************************

## Multithreading
Multithreading is a technique in Python that allows a program to execute multiple threads concurrently within a single process. Threads share the same memory space, making communication between them faster, but it is mainly suitable for I/O-bound tasks.

### Thread
A thread is the smallest unit of execution within a process. Multiple threads exist inside a single process and share resources.

### Concurrent Execution
Multiple threads run concurrently (not truly parallel in CPython due to GIL), improving performance for tasks like file handling, network calls, etc.

### GIL (Global Interpreter Lock)
In Python, only one thread executes Python bytecode at a time
So threads don’t fully use multiple CPU cores

### Threading Module
Python provides the threading module for creating threads.

### Code Interpretation
*Importing Modules*
- threading => for concurrent execution using threads
- time => for performance measurement
- do_something => user-defined function executed by each thread

*Main Execution Block*
if __name__ == "__main__":
- Ensures the code runs only when executed directly
- Prevents unwanted behavior when importing modules

*Creating Threads*
thread = threading.Thread(target=do_something, args=(size, out_list))
- Defines a thread
- Assigns a function (do_something) to run
- Passes arguments to that function

*Starting Threads*
j.start() **Begins execution of each thread.**
*Synchronization*
j.join() **Ensures the main program waits until all threads complete.**

*Performance Measurement*
start_time = time.time()
end_time = time.time()
**Used to calculate total execution time i.e. (end_time - start_time).**

* out_list = list()
Creates an empty list to store output from the thread.

### Advantages of Multithreading
- Shared memory (easy data sharing)
- Lightweight (less overhead than processes)
- Faster for I/O-bound tasks

### Limitations
- Affected by Global Interpreter Lock (GIL)
- Not efficient for CPU-bound tasks
- Risk of race conditions

**************************************************************************************************

## Serial Execution
Serial execution is the simplest way of running a program where tasks are executed one after another in a sequential manner. In this approach, only one task runs at a time, and the next task starts only after the previous one finishes.

### Sequential Execution
Tasks are performed step-by-step in a fixed order. There is no parallelism or concurrency involved.

### Single Process Execution
The entire program runs within a single process and uses a single CPU core.

### Code Interpretation
*Importing Modules*
time => for performance measurement
do_something => user-defined function executed repeatedly

*Main Execution Block*
if name == "main":
- Ensures the code runs only when executed directly
- Standard practice for structured Python programs

*Loop Execution*
for i in range(0, n_exec):
- Repeats the task multiple times (n_exec times)
- Each iteration runs after the previous one completes

*Function Call*
do_something(size, out_list)
- Calls the function directly
- Executes the task sequentially
- No parallelism or threading involved

*List Initialization*
* out_list = list()
Creates a new empty list for each iteration.
Each execution uses its own list and does not share data.

*Performance Measurement*
start_time = time.time()
end_time = time.time()
**Used to calculate total execution time i.e. (end_time - start_time).**

### Advantages of Serial Execution
- Simple and easy to understand
- No synchronization issues
- No overhead of thread/process creation

### Limitations
- Slow for large tasks
- Does not utilize multiple CPU cores
- Inefficient for CPU-intensive operations

### Comparison 
This approach is useful as a baseline to compare performance with multithreading and multiprocessing.
*Main Points*
- Serial execution takes the maximum time
- Multithreading improves performance for I/O-bound tasks
- Multiprocessing performs best for CPU-bound tasks

**************************************************************************************************