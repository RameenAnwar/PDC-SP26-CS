# CHAPTER 1 --- README

A collection of Python programs demonstrating core programming concepts
including OOP, control flow, data structures, file handling, and
performance comparison using threading and multiprocessing.

------------------------------------------------------------------------

## How to Run Any Program

``` bash
python filename.py
```

> Make sure Python is installed on your device. Replace `filename` with
> the actual name of the file you want to run.

------------------------------------------------------------------------

## File Index

  File                      Concept
  ------------------------- --------------------------------
  classes.py                OOP, Classes & Inheritance
  dir.py                    If-Else & For Loop
  lists.py                  Data Structures
  file.py                   File Handling
  flow.py                   While Loop & Control Flow
  serial_test.py            Sequential Performance Testing
  thread_and_processes.py   Thread vs Process Comparison
  multiprocessing_test.py   Multiprocessing
  multithreading_test.py    Multithreading

------------------------------------------------------------------------

## classes.py

**Description:**
A class acts as a blueprint used to create objects. 
Inheritance is a fundamental concept in OOP that enables a derived class to reuse the attributes and methods of a base class. 
This code shows how classes are defined, how instance variables are used, and how inheritance works

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful when understanding how objects behave in object-oriented programming, it may be useful in understanding the basics of inheritance too.

**Observations:**
- Class variables are shared across all instances, while instance variables are unique to each object.
- Inheritance allows a subclass to reuse methods and properties from a parent class.

**Advantages:**
- A good example for beginners that are learning OOP.
- Shows practical use of inheritance.

**Disadvantages:**
- Overuse of inheritance can make code harder to follow.
- Debugging can be harder for beginners when variables change at different level.

---

## dir.py

**Description:**
This program demonstrates the use of conditional statements like if-else and loops(for loop) in python.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful when you need to filter out data based on a specific condition or need to practice iteration(a specified number of iterations take place).

## Observations
- Conditional statements allow programs to choose different execution paths.
- Loops enable repeated execution over a sequence of elements.

## Advantages
- Loops enable repeated execution over a sequence of elements.
- Forces beginners to build problem solving skills.

## Disadvantages
- Limited scope as input values are fixed.
- No input validation.

---

## lists.py

**Description:**
This implementation showcases how Python handles different data structures such as lists, dictionaries, and tuples.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful when working with collections of data, especially when storing, updating, or retrieving information.

**Observations:**
- Dictionaries store values using keys, enabling quick updates.
- List elements are updated using both positive and negative indexing.
- Tuple values remain constant throughout execution.

**Advantages:**
- This program covers multiple data structures in a single example.
- Demonstrates practical data manipulation techniques.

**Disadvantages:**
- Uses predefined values, limiting flexibility.
- Not designed for large-scale data handling.

---

## file.py

**Description:**
This programs shows how Python performs input and output operations on files.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful in applications where data needs to be stored and retrieved from files, such as logs, reports, or simple data storage.

**Observations:**
- Files should be properly closed after operations.
- Files can be opened in different modes such as write ('w') and read ('r')

**Advantages:**
- Demonstrates essential file handling operations.
- Useful for storing and retrieving data.

**Disadvantages:**
- No error handling.
- Not optimized for handling large files.

---

## flow.py

**Description:**
This program demonstrates the use of conditional statements like if-else and loops(while loop) in python.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful when you need to filter out data based on a specific condition or need to practice iteration(based on a specified condition).

**Observations:**
- Conditional statements allow programs to choose different execution paths.
- Loops enable repeated execution over a sequence of elements based on a specific condition in while loop.

**Advantages:**
- Loops enable repeated execution over a sequence of elements.
- Forces beginners to build problem solving skills.

**Disadvantages:**
- Limited scope as input values are fixed.
- No input validation.

---

## serial_test.py

**Description:**
This program evaluates how long it takes to process large datasets by repeatedly executing a function that fills a list, observing the performance behavior.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful in scenarios where performance analysis is required, especially when dealing with repeated operations on large amounts of data.

**Observations:**
- The time module is used to calculate execution duration.
- Performance depends on the size of the data being processed.

**Advantages:**
- Useful for benchmarking operations.
- it helps in analyzing the impact of large data sizes.

**Disadvantages:**
- It consumes significant memory due to large lists.
- Limited to basic performance measurement.

---

## thread_and_processes.py

**Description:**
This implementation compares thread-based and process-based execution by performing the same task of generating random values and measuring the time taken for each method.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful when evaluating different execution strategies for handling large workloads and understanding their performance behavior.

**Observations:**
- Execution time is measured to compare performance.
- Threads are created using the threading module to perform tasks.
- Processes are created using the multiprocessing module.

**Advantages:**
- This program helps in understanding performance differences and determine which is the better choice.
- Flexible for experimenting with different data sizes.

**Disadvantages:**
- Large data size increases memory usage significantly.
- No data validation included for incorrect or invalid entries.

---

## multiprocessing_test.py

**Description:**
This program illustrates how multiple processes can be used to perform repeated operations, where each process independently executes a function that generates data.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Suitable for scenarios where large tasks can be divided into separate units, allowing them to be executed simultaneously for better performance.

**Observations:**
- Processes are created using the multiprocessing module.
- Each process executes the same function independently.
- The start() method begins execution, while join() ensures completion.

**Advantages:**
- Efficient for handling large and repetitive tasks.
- This is useful for performance evaluation.

**Disadvantages:**
- Increased memory usage due to multiple processes.
- Additional overhead in process creation.
- Each process works on its own data, increasing resource usage.

---

## multithreading_test.py

**Description:**
This program illustrates how multiple threads can execute a function concurrently, with each thread independently performing a task of generating data and storing it in a list.

**Execution Method:**
Run the command "python filename.py"
Note: Replace filename with the name you used to save the file with.

**Use Case:**
- Useful for scenarios where tasks can be performed in parallel without interfering with each other, especially for repetitive or I/O-bound operations.

**Observations:**
- Threads are created using the threading.Thread class.
- Total execution time is recorded using time.time().
- The start() method begins execution, while join() ensures completion.

**Advantages:**
- Efficient for tasks that can run concurrently.
- Lower memory overhead compared to processes(unless creating too many threads).

**Disadvantages:**
- Multiple threads may increase memory usage.
- No error handling in the code.

---