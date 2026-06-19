# Chapter # 01
This is an introductory chapter that covers the building blocks of Python programming.

## 1) classes.py
This file presents Object-oriented programming in a simple way. It shows how classes, objects, class variables
vs instance variables, and inheritance work in Python.
- Myclass is a class which has a shared variable 'common', 
while myvariable is an instance variable unique to each object.
- Demonstrates overriding (an instance or child class changing behavior without affecting others).
- Changing Myclass.common affects all instances, but changing instance.common only affects that one object.
- AnotherClass inherits from Myclass, so it can use parent methods like myfunction.
- It also shows Python’s flexibility by allowing you to add new attributes (instance.test) at runtime.

## 2) dir.py
This file demonstrates conditional statements (if-else) and loops in Python.
- The flow of any program is based on conditional statements.
- Example in the file: A simple if-else block is written to check whether a number n is positive, negative or zero.
- The second part of the file shows iteration logic.
- A for-loop is used to iterate over a list of numbers.
- It calculates the some of all elements by adding each value to a variable sum.

## 3) do_something.py
This file defines a simple Python function to generate random numbers.
- Utilizes the Python library 'random'
- The do_something function takes two parameters: count (numbers to generate) and out_list (a list to store them).
- It uses a for-loop to generate count random numbers between 0 and 1 using random.random().
- Each generated number is then appended to the list out_list.
- Demonstrates functions, loops, and list manipulation in Python.

## 4) file.py
This file demonstrates basic file handling in Python.
- First the program opens a file test.txt in write mode ('w') and writes two lines of text to it.
- Closes the file to save changes.
- Reopens the same file in read mode (default) and reads its content using f.read().
- Prints the content to the console.
- Shows how to create, write, read, and close files in Python.

## 5) flow.py
This file shows the flow control of program. An extended version of dir.py file with while loop.
- Uses an if-elif-else block to check whether a number is positive, negative, or zero.
- A for-loop iterates over a list to calculate the sum of all elements and store the sum in a variable.
- A while loop to compute the sum of natural numbers from 1 to n.
- Illustrates conditional logic, iteration, and accumulation in Python.

## 6) lists.py
This file introduces Python data structures and functions in Python.
- Lists: Defined using square brackets [] with items separated by commas, or by using the Python list() constructor.
- Lists are used to store multiple items in a single variable
- example and mylist are nested and mutable lists, and their elements are updated using indexing.
- Dictionaries:  Defined using curly brackets {}, are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered, changeable and do not allow duplicates.
- mydict is a dictionary with mixed key types and the program shows how to update dict values.
- Tuples:  Defined using small brackets (), are used to store multiple items in a single variable. 
- Shows a tuple mytuple, which is immutable and cannot be changed.
- Function: In Python, a function is a reusable block of code that performs a specific task and only runs when it is called.
- This example introduces functions as objects, e.g., assigning len to myfunc and using it to get the length of a list.
- Illustrates basic data manipulation and accessing elements in Python.

## 7) multiprocessing_test.py
This file demonstrates how to use multiprocessing to run tasks in parallel and measure execution time.
- multiprocessing: A Python module that allows running multiple processes simultaneously, each with its own Python interpreter and memory space.
- This is useful for CPU-bound tasks where parallel execution can speed up computation.
- Process: An independent unit of execution with its own memory; different from a thread which shares memory with other threads.
- imports do_something function: Generates random numbers and appends them to a list (from file do_something.py).
- start(): Begins execution of a process.
- join(): Waits for the process to finish before continuing.
- time.time(): Measures the time taken to execute the code.
Time taken = 11.794094800949097
This program demonstrates parallel list processing using 10 processes to generate 10 million random numbers each,
and prints the total execution time.

## 8) multithreading_test.py
This file demonstrates multithreading to perform tasks concurrently in the same process.
- threading: A Python module that allows running multiple threads within the same process.
- Threads share the same memory space, making it easy to share data but limited by Python’s GIL for CPU-heavy tasks.
- Thread: A smaller unit of execution within a process. Ideal for I/O-bound tasks, like reading/writing files.
- import do_something function: Generates random numbers and appends them to a list (from file do_something.py).
- start(): Begins thread execution.
- join(): Waits for a thread to finish before continuing.
- time.time(): Measures execution time to compare efficiency.
Time Taken = 13.778166770935059
In this program, CPU-bound tasks like generating large lists may not get much speed-up with threads because of the GIL;
multiprocessing is better for CPU-heavy tasks.

## 9) serial_test.py
This file runs tasks sequentially (one after another) in Python.
- Serial execution means each task must finish before the next starts.
- Uses the do_something function to generate random numbers in a list (from file do_something.py).
- Runs the function 10 times in a loop, each time creating a new list.
- Measures total time with time.time() to compare with multithreading and multiprocessing.
Time Taken = 13.574621200561523
Highlights how parallel execution (threads/processes) can speed up CPU-intensive tasks compared to serial execution.

## 10) thread_and_processes.py
This file demonstrates three ways to execute tasks in Python: serially, with threads, and with processes.
- Serial execution: Runs tasks one by one, measuring total time taken.
- Multithreading: Uses multiple threads in the same process.
- Threads share memory but may be limited by Python’s GIL, so CPU-heavy tasks don’t always speed up much.
- Multiprocessing: Uses multiple independent processes.
- Each has its own memory, bypassing the GIL, which makes it faster for CPU-intensive tasks like generating large lists.
- do_something generates random numbers and appends them to a list.
- The program measures and prints the time taken for each approach to illustrate the difference in performance.

Comparison of time taken:-
multiprocesses time= 11.794094800949097
multithreading time= 13.778166770935059
serial time = 13.574621200561523

- Serial execution takes the longest time because it runs tasks one by one, taking 13.57 seconds.
- Multithreading took slightly longer (13.77 seconds). This happens because threads share the same memory
and Python’s GIL limits true parallelism for CPU-bound tasks like generating random numbers.
- Multiprocessing was the fastest (11.79 seconds) as each process runs independently with its own memory,
bypassing the GIL, so CPU-heavy tasks benefit more from multiprocessing.

# Conclusion:-
For CPU-intensive tasks, multiprocessing gives better performance than both serial execution and multithreading.
For I/O-bound tasks, multithreading could still be effective.
The results illustrate how Python’s GIL affects multithreading, and why processes are preferred for heavy computations.