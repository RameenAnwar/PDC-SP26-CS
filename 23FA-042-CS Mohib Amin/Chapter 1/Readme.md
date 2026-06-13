
CHAPTER 1

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: classes.py

## Description
A class is a blueprint or template for creating objects.
Inheritance is a pillar of oop which is used to allow a child class to inherit the attributes and behavior of as parent class.
This code demonstrates the creation of classes, the use of instance variables and also shows a key pillar of object oriented programming "Inheritance".

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
Execute this program when practising basic object-oriented programming concepts.

## What We Learned
- How to create classes and instance variables.
- The concept of inheritance.

## Advantages
- Code reusability increases and code becomes easy to read.
- This code helps understand some of the core OOP concepts clearly.

## Disadvantages
- Inheritance can introduce complexity if overused.
- Requires careful tracking of where variables are defined.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: dir.py

## Description
This program demonstrates the use of conditional statements and for loop in python.

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when making decisions based on conditions such as marking grades(it has a specified criteria).
It can also be used when u need to perform any task requiring iteration.

## What We Learned
- How to use if-else and eilf for multiple conditions
- The working of "for" loop.

## Advantages
- Improves logical and critical thinking.
- Simple and easy to understand and implement.

## Disadvantages
- No error handling incase of any invalid entries.
- Works only for predefined values (no user input).

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: lists.py

## Description
This program demonstrates the use of lists,dictionary and tuples in python.

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when working with practising list, dictionary or tuple operations like accessing, updating, and retrieving values.

## What We Learned
- A list is not limited to one data type, can handle different data types being in the same list.
- The concept of nested lists.
- Usage of different built in functions for lists, tuples and dictionary.

## Advantages
- Shows working of different data structures in the same program.
- Shows the usage of different built-in functions.

## Disadvantages
- Static data is used (no user input).
- Not suitable for processing large or complex data.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: do_something.py

## Description
This program demonstrates the use of functions and lists in Python.  
It defines a function that generates a specified number of random values and appends them to a list using a loop.

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when you need to generate and store random data for testing, simulations, or simple data processing.

## What We Learned
- How to define and use a function with parameters.
- How to use the random module to generate values. 

## Advantages
- It is useful for generating test or sample data. 
- This program helps understand list manipulation.

## Disadvantages
- Not suitable for complex data generation tasks.
- No validation for input parameters.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: file.py

## Description
This program demonstrates basic file handling in Python.  

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when working with file operations such as storing data permanently or retrieving saved information.

## What We Learned
- How to open files in read-only/write mode. 
- Importance of closing files after operations. 

## Advantages
- Simple and clear demonstration of file handling. 
- Useful for storing data permanently and applicable in small scale working platforms like a mini mart or such.

## Disadvantages
- No error handling if file operations fail.
- Read-write over specific portion of file becomes difficult if the data in file is too big.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: flow.py

## Description
This program demonstrates the use of conditional statements and while loop in python.

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when making decisions based on conditions such as marking grades(it has a specified criteria).
It can also be used when u need to perform any task requiring iteration based on condition

## What We Learned
- How to use if-else and eilf for multiple conditions.
- The working of "while" loop.

## Advantages
- Improves logical and critical thinking.
- Simple and easy to understand and implement.

## Disadvantages
- No error handling incase of any invalid entries.
- Works only for predefined values (no user input).

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: serial_test.py

## Description
This program demonstrates **measuring execution time** for a function that processes large data.  
It repeatedly calls a function do_something() to fill a list with a large number of elements and calculates the total time taken for execution.

## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when you want to analyze performance or execution time of operations involving  data processing.

## What We Learned
- How to measure execution time using the time module.
- How large data operations affect program performance.

## Advantages
- Simple structure and easy to modify.
- Useful for performance analysis of functions.

## Disadvantages
- High memory usage due to large list creation. 
- No error handling for large data processing.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: thread_and_processes.py

## Description
This program demonstrates the use of multithreading and multiprocessing in Python.
By using both, random values are generated and appended to a list and than the time taken by both is compared.


## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when comparing different execution approaches for handling large tasks and analyzing their performance.

## What We Learned
- How to create and run threads using the threading module.
- How to create and run processes using the multiprocessing module.
- How execution time differs between threading and multiprocessing.

## Advantages
- Demonstrates both threading and multiprocessing in one program.
- Easy to modify for testing different workloads
- Useful for comparing execution times.

## Disadvantages
- High memory usage due to large list operations. 
- No error handling.
- Output may vary depending on system performance.  

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: multiprocessing_test.py

## Description
This program demonstrates the use of multiprocessing in Python to execute a task multiple times.  
It creates several processes, each running a function do_something() which generates values and stores them in a list, and then measures the total execution time.


## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This program is executed when handling large tasks that can be divided into multiple independent processes.

## What We Learned
- How to create processes using the multiprocessing module.  
- How to assign tasks to multiple processes using a loop. 
- How execution time can be measured for multiprocessing tasks.

## Advantages
- Allows execution of tasks using multiple processes.
- Helps improve performance for repeated operations.

## Disadvantages
- Overhead of creating and managing processes.
- No error handling included. 

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: multithreading_test.py

## Description
This program demonstrates the use of multithreading in Python to execute a task multiple times.  
It creates several threads, each running a function do_something() which generates values and stores them in a list, and then measures the total execution time.


## How and When to Execute
Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)
This is executed when tasks can be divided into smaller concurrent units that can run simultaneously in threads.

## What We Learned
- How to create processes using the threading module.  
- How to start threads with `start()` and wait for completion with `join()`

## Advantages
- Threads can run concurrently, potentially improving performance.
- Helps improve performance for repeated operations.

## Disadvantages
- High memory usage if many threads are created.
- Performance improvements are not guaranteed for CPU-intensive tasks.

--------------------------------------------------------------------------------------------------------------------------------------------------