# Chapter 01 - Python Parallel Programming Basics

## 1. classes.py

**Topic:** Classes, Instance Variables, Inheritance

**What is happening?**
Two instances share a class variable `common`. When `Myclass.common` is changed, both instances reflect the change because they share it. But when `instance.common` is set directly, it creates its own copy and disconnects from the class variable.

**How to run:**
python classes.py

**When to use:**
When multiple objects need to share some data but also have their own individual data.

**Advantages:**
- Shared data is easy to manage through class variables
- Code reuse through inheritance (AnotherClass gets Myclass functions automatically)

**Disadvantages:**
- Shared class variables can cause unexpected bugs in parallel programs if multiple threads change them simultaneously

**End use:**
In parallel programming, understanding shared vs individual data is critical — threads share memory, so knowing this difference prevents data conflicts. 

## 2. dir.py

**Topic:** Conditionals and Loops

**What is happening?**
Two basic programs — first checks if a number is positive, negative, or zero using if/elif/else. Second iterates over a list and calculates the sum of all numbers.

**How to run:**
python dir.py

**When to use:**
Conditionals when you need decision making in code. Loops when you need to process every item in a collection.

**Advantages:**
- Simple and readable control flow
- Loops avoid writing repetitive code

**Disadvantages:**
- Simple if/else doesn't scale well for complex conditions
- Basic for loop is sequential — not suitable for parallel processing of large lists

**End use:**
These are building blocks of any program. In parallel programming, loops are often the part that gets parallelized to speed up processing.

## 3. do_something.py

**Topic:** Random Number Generation / Helper Function

**What is happening?**
A helper function that generates `count` number of random values and appends them to `out_list`. This function is used in other files like serial_test.py, multithreading_test.py, and multiprocessing_test.py to simulate a workload.

**How to run:**
python do_something.py
(No output — this is a helper function, meant to be imported)

**When to use:**
When you need to simulate work/load for testing serial vs parallel execution.

**Advantages:**
- Reusable function — imported wherever needed
- Simple way to simulate real workload

**Disadvantages:**
- No output on its own — only useful when called from another file

**End use:**
Used to compare how long the same task takes in serial vs multithreading vs multiprocessing.

## 4. file.py

**Topic:** File Handling

**What is happening?**
The program demonstrates basic file operations. It opens a file, writes data into it, then reads the same data. This shows how data can be stored and retrieved using files.

**How to run:**
python file.py

**When to use:**
When data needs to be stored permanently or read from external files.

**Advantages:**
- Data is stored permanently
- Useful for saving results and logs

**Disadvantages:**
- Slower than in-memory operations
- In parallel programming, multiple threads accessing the same file can cause data conflicts

**End use:**
In parallel programming, file handling is used for storing outputs and logs, but requires proper synchronization to avoid errors.

## 5. flow.py

**Topic:** Control Flow and Functions

**What is happening?**
The program demonstrates how functions are defined and called, and how the execution of a program flows step by step. It shows how control moves between different parts of the code.

**How to run:**
python flow.py

**When to use:**
When organizing code into smaller reusable parts and controlling execution flow.

**Advantages:**
- Improves readability
- Code becomes reusable
- Easier debugging

**Disadvantages:**
- Too many functions can make the program harder to follow
- Slight overhead due to function calls

**End use:**
In parallel programming, tasks are divided into functions and assigned to threads or processes for execution.

## 6. lists.py

**Topic:** Lists (Data Structure)

**What is happening?**
The program demonstrates basic list operations such as creating a list, adding and removing elements, and iterating through the list using loops.

**How to run:**
python lists.py

**When to use:**
When storing and managing multiple values in a single variable.

**Advantages:**
- Dynamic and flexible in size
- Easy to iterate and manipulate
- Provides built-in methods for operations

**Disadvantages:**
- Not thread-safe in parallel programming
- Concurrent modifications can lead to inconsistent data

**End use:**
In parallel programming, lists are used to store tasks and collect results, but require proper synchronization when accessed by multiple threads or processes.
## 7. serial_test.py

**Topic:** Serial Execution

**What is happening?**
The program executes a task multiple times in a sequential manner using the do_something function. Each task runs one after another, and the total execution time is measured.

**How to run:**
python serial_test.py

**When to use:**
When tasks need to be executed in order or when parallel execution is not required.

**Advantages:**
- Simple and easy to understand
- No synchronization or race condition issues
- Predictable execution

**Disadvantages:**
- Slow for large workloads
- Does not utilize multiple CPU cores efficiently

**End use:**
Used as a baseline to compare performance with multithreading and multiprocessing in parallel programming.

## 8. multithreading_test.py

**Topic:** Multithreading

**What is happening?**
The program creates multiple threads to execute tasks simultaneously using the do_something function. Each thread runs independently but shares the same memory space. The total execution time is measured.

**How to run:**
python multithreading_test.py

**When to use:**
When dealing with I/O-bound tasks such as file handling, network requests, or waiting operations.

**Advantages:**
- Faster execution for I/O-bound tasks
- Lightweight and efficient
- Easy to implement

**Disadvantages:**
- Global Interpreter Lock (GIL) limits true parallelism in Python
- Risk of race conditions due to shared memory
- Debugging can be difficult

**End use:**
Used in applications like web servers, file downloading, and handling multiple user requests where tasks involve waiting.

## 9. multiprocessing_test.py

**Topic:** Multiprocessing

**What is happening?**
The program creates multiple processes to execute tasks in parallel using the do_something function. Each process runs independently with its own memory space, and the total execution time is measured.

**How to run:**
python multiprocessing_test.py

**When to use:**
When dealing with CPU-intensive tasks that require true parallel execution.

**Advantages:**
- Achieves true parallelism using multiple CPU cores
- No limitation of Global Interpreter Lock (GIL)
- Faster for heavy computational tasks

**Disadvantages:**
- Higher memory usage
- Process creation is more expensive than threads
- Data sharing between processes is complex

**End use:**
Used in data processing, machine learning, and scientific computations where performance is critical.

## 10. thread_and_processes.py

**Topic:** Threads vs Processes

**What is happening?**
The program compares multithreading and multiprocessing by executing similar tasks using both approaches and measuring their performance.

**How to run:**
python thread_and_processes.py

**When to use:**
When deciding whether to use multithreading or multiprocessing for a specific problem.

**Advantages:**
- Provides a clear comparison between threads and processes
- Helps in understanding performance differences
- Assists in decision making

**Disadvantages:**
- Results may vary depending on system and workload
- Requires understanding of both threading and multiprocessing

**End use:**
Helps in selecting the appropriate approach: multithreading for I/O-bound tasks and multiprocessing for CPU-bound tasks.