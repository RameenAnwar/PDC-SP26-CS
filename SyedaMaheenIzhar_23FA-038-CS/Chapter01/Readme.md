# CHAPTER 1

## Classes.py  — Object-Oriented Programming in Python

### Description

This program demonstrates the basic concepts of Object-Oriented Programming (OOP) in Python. It covers class creation, object instantiation, class variables, instance variables, and inheritance.

### How it works

A class `Myclass` is defined with a shared class variable `common` and an instance variable `myvariable`. Two objects are created to observe how class variables behave when modified at both class and instance levels.

The program then defines another class `AnotherClass` that inherits from `Myclass`. It shows how child classes can reuse methods and properties from the parent class while adding their own functionality.

### Result

The output shows:

* Instance variables remain unique to each object
* Class variables are shared across objects unless overridden
* Changes at class level affect all instances
* Inheritance allows reuse of methods from the parent class

### Advantages

* Simple and clear demonstration of OOP basics
* Helps understand class vs instance variables
* Shows practical use of inheritance

### Disadvantages

* Covers only basic concepts
* Does not include advanced OOP features like polymorphism or encapsulation

### Where it can be used

* Beginner-level Python projects
* Learning OOP concepts
* Building structured applications like management systems or simulations


## dir.py Conditional & Loop Example — Python Basics

### Description

This program demonstrates basic Python concepts including conditional statements (`if-elif-else`) and loops. It checks whether a number is positive, negative, or zero, and also calculates the sum of elements in a list.

### How it works

First, a variable `num` is used to determine whether the number is positive, zero, or negative using conditional statements.

Next, a list of numbers is defined, and a `for` loop is used to iterate through each value and calculate the total sum by adding each element to a variable.

### Result

The output shows:

* Whether the given number is positive, negative, or zero
* The total sum of all numbers in the list

### Advantages

* Easy to understand basic programming concepts
* Demonstrates use of conditions and loops
* Useful for beginners learning Python

### Disadvantages

* Very basic example with limited functionality
* Does not handle user input or edge cases

### Where it can be used

* Learning Python fundamentals
* Simple calculations and data processing
* Beginner-level programming practice


## do_something.py Random Number Generator Function — Python

### Description

This code defines a function that generates random numbers and stores them in a list. It uses Python’s built-in `random` module.

### How it works

A function `do_something(count, out_list)` is created, which takes a number (`count`) and a list (`out_list`) as input.

The function runs a loop `count` times, and during each iteration, it generates a random floating-point number between 0 and 1 using `random.random()` and appends it to the list.

### Result

After calling the function, the list will contain `count` number of randomly generated values.

### Advantages

* Simple way to generate random data
* Demonstrates use of functions and loops
* Useful for simulations or testing

### Disadvantages

* Generates only floating-point numbers between 0 and 1
* No control over range or distribution

### Where it can be used

* Simulations and probability experiments
* Testing applications with random inputs
* Basic data generation tasks

## file.py File Handling Example — Reading & Writing in Python

### Description

This program demonstrates basic file handling in Python, including writing data to a file and then reading it back.

### How it works

First, a file `test.txt` is opened in write mode (`'w'`). Two lines of text are written into the file using the `write()` method, and the file is then closed.

After that, the same file is opened again in read mode (default mode), and its content is read using the `read()` method and printed on the screen.

### Result

The program creates a file and displays its contents:

* first line of file
* second line of file

### Advantages

* Demonstrates basic file operations (write and read)
* Simple and easy to understand
* Useful for beginners learning file handling

### Disadvantages

* Does not use `with` statement (which is safer for file handling)
* No error handling included

### Where it can be used

* Saving and reading data from files
* Logging information
* Basic file-based applications


## flow.py Control Flow Example — If, For, While in Python

### Description

This program demonstrates the use of basic control flow statements in Python, including `if-elif-else`, `for` loop, and `while` loop.

### How it works

* **If Statement:**
  A variable `num` is checked to determine whether it is positive, negative, or zero using conditional statements.

* **For Loop:**
  A list of numbers is iterated using a `for` loop to calculate the sum of all elements.

* **While Loop:**
  A `while` loop is used to calculate the sum of natural numbers from 1 up to a given number `n`.

### Result

The output shows:

* Whether the number is positive, negative, or zero
* The sum of all elements in the list
* The sum of natural numbers from 1 to `n`

### Advantages

* Covers multiple fundamental concepts in one program
* Easy to understand and beginner-friendly
* Demonstrates practical use of loops and conditions

### Disadvantages

* Uses basic logic without optimization
* No user input or error handling

### Where it can be used

* Learning Python control structures
* Basic problem-solving and practice
* Simple mathematical calculations


## list.py Data Types Example — Lists, Dictionary, Tuple in Python

### Description

This program demonstrates different built-in data types in Python, including lists, dictionaries, tuples, and basic function usage.

### How it works

* **List:**
  A list is created with mixed data types. Elements are accessed and modified using indexing, including negative indexing.

* **Dictionary:**
  A dictionary is defined with key-value pairs. Values are accessed and updated using keys.

* **Tuple:**
  A tuple is created and printed. It shows an immutable data structure (cannot be changed).

* **Function Usage:**
  The built-in function `len` is assigned to a variable and used to find the length of a list.

### Result

The output shows:

* Updated list elements after modification
* Dictionary values before and after update
* Tuple contents
* Length of the list using a function

### Advantages

* Demonstrates multiple data types in one example
* Shows mutability (list, dictionary) vs immutability (tuple)
* Simple and easy to understand

### Disadvantages

* Basic example without advanced operations
* No user interaction or validation

### Where it can be used

* Learning Python data structures
* Beginner-level programming practice
* Handling collections of data in applications


## multiprocessing_test.py   Multiprocessing Example — Parallel Execution in Python

### Description

This program demonstrates the use of multiprocessing in Python to run tasks in parallel. It uses multiple processes to execute a function that generates random numbers.

### How it works

The program imports the function `do_something` and creates multiple processes using the `multiprocessing` module.

* A large number (`size`) defines how many random values each process will generate
* `procs` defines how many processes will run simultaneously
* Each process runs the same function independently
* All processes are started using `start()` and then synchronized using `join()`

The execution time is measured using the `time` module.

### Result

The output shows:

* Confirmation message after all processes complete
* Total time taken to execute all processes in parallel

### Advantages

* Improves performance by utilizing multiple CPU cores
* Efficient for large computations or data processing
* Demonstrates real-world parallel programming concept

### Disadvantages

* More complex than single-threaded programs
* Higher memory usage due to multiple processes
* Sharing data between processes is not straightforward

### Where it can be used

* Large-scale data processing
* Scientific computations
* Performance-critical applications
* Parallel simulations and workloads


## multithreading_test.py  Multithreading Example — Concurrent Execution in Python

### Description

This program demonstrates the use of multithreading in Python to perform tasks concurrently. It runs a function multiple times using threads to improve execution speed.

### How it works

The program imports the function `do_something` and creates multiple threads using the `threading` module.

* `size` defines how many random values each thread will generate
* `threads` specifies the number of threads to run
* Each thread executes the same function
* Threads are started using `start()` and synchronized using `join()`

Execution time is measured using the `time` module.

### Result

The output shows:

* A message after all threads complete execution
* Total time taken using multithreading

### Advantages

* Allows concurrent execution of tasks
* Useful for I/O-bound operations
* Easier to implement than multiprocessing

### Disadvantages

* Limited performance improvement for CPU-bound tasks due to GIL (Global Interpreter Lock)
* Threads share memory, which can cause synchronization issues

### Where it can be used

* I/O operations (file handling, network requests)
* Lightweight concurrent tasks
* Applications requiring responsiveness


## serial_test.py  Serial Execution Example — Sequential Processing in Python

### Description

This program demonstrates serial (sequential) execution in Python, where tasks are performed one after another without any parallelism.

### How it works

The program imports the function `do_something` and executes it multiple times in a loop.

* `size` defines how many random values are generated in each execution
* `n_exec` specifies how many times the function runs
* A new list is created for each execution
* The function runs sequentially, meaning each iteration waits for the previous one to complete

Execution time is measured using the `time` module.

### Result

The output shows:

* A message after all executions are completed
* Total time taken for sequential processing

### Advantages

* Simple and easy to understand
* No complexity of threads or processes
* No synchronization or memory-sharing issues

### Disadvantages

* Slower for large workloads
* Does not utilize multiple CPU cores
* Inefficient for performance-critical tasks

### Where it can be used

* Small-scale programs
* Simple data processing tasks
* Situations where parallelism is not required


## thread_and_processes.py Performance Comparison — Serial, Multithreading & Multiprocessing in Python

### Description

This program compares three different execution approaches in Python: serial execution, multithreading, and multiprocessing. It measures the time taken by each approach to perform the same task.

### How it works

A function `do_something` generates a large number of random values and appends them to a list. The program executes this function using:

* **Serial Execution (commented out):** Runs the function sequentially in a loop.
* **Multithreading:** Uses the `threading` module to run multiple threads concurrently.
* **Multiprocessing:** Uses the `multiprocessing` module to run multiple processes in parallel.

Each approach runs the same workload (`NUM_WORKERS` times), and execution time is measured using the `time` module.

### Result

The program outputs:

* Execution time for multithreading
* Execution time for multiprocessing
* (Optional) Execution time for serial execution if enabled

This allows comparison of performance between the three approaches.

### Advantages

* Provides a clear comparison between execution models
* Demonstrates real-world use of threading vs multiprocessing
* Helps understand performance trade-offs

### Disadvantages

* Code complexity increases when using parallel approaches
* Shared data handling can be problematic
* Multithreading may not improve CPU-bound tasks due to GIL

### Where it can be used

* Performance analysis of Python programs
* Learning concurrency and parallelism concepts
* Choosing the right execution model for applications
