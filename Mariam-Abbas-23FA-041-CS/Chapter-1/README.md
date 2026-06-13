# classes

*Description:*
A class is a blueprint for creating objects. It can have shared (class-level) and individual (instance-level) variables. One class can inherit from another.

*How it Works:*
Myclass created with common (shared) and myvariable (instance) variable
2 instances created — instance and instance2
Changing common at class level affects all instances
AnotherClass inherits from Myclass

*Result:*
Shows difference between class variable and instance variable, and how inherited class can use parent's function.

*Advantages:*
Code is reusable
Easy to model real world things
Inheritance reduces code repetition

*Disadvantages:*
Difficult for beginners
Overkill for small/simple problems

*Where to Use:*
Large projects like Hospital System, Banking App
When multiple objects of same type are 


# dir

*Description:*
Basic control flow in Python — using if/elif/else to check conditions and for loop to iterate over a list.

*How it Works:*
Checks if a number is positive, negative, or zero using if/elif/else
Iterates over a list of numbers using for loop and calculates their sum

*Result:*
Prints whether number is positive/negative/zero, and outputs the sum of all list elements.

*Advantages:*
Simple and readable syntax
Handles multiple conditions easily
Loops reduce repetitive code

*Disadvantages:*
Too many elif conditions make code messy
for loop not suitable when index control is needed

*Where to Use:*
Validating user input
Processing lists/arrays of data
Any decision-making logic in a program


# do_something
*Description:*
A function that generates random numbers and appends them to a list using Python's random module.

*How it Works:*
do_something(count, out_list) takes a count and a list as input
Runs a loop count times
Each iteration appends a random float (0 to 1) to out_list

*Result:*
A list filled with count number of random float values between 0 and 1.

*Advantages:*
Reusable function — call it multiple times with different lists
Simple and clean code

*Disadvantages:*
No return value — modifies list directly (can be confusing)
No validation if count is negative or zero

*Where to Use:*
Generating test/sample data
Simulations and random sampling
Testing parallel/multithreading performance with random data


# file

*Description:*
Basic file handling in Python — writing text to a file and then reading it back.

*How it Works:*
Opens test.txt in write mode 'w' and writes two lines
Closes the file
Opens same file again in read mode and prints its content

*Result:*
Creates test.txt with two lines and prints them on screen.

*Advantages:*
Simple way to store data permanently
Easy to read and write files in Python

*Disadvantages:*
'w' mode overwrites existing file content
No error handling if file doesn't exist or path is wrong

*Where to Use:*
Saving program output to a file
Reading config or data files
Logging results


# flow

*Description:*
Demonstrates three basic control flow structures in Python — if/elif/else, for loop, and while loop.

*How it Works:*
if/elif/else — checks if number is positive, negative, or zero
for loop — iterates over a list and calculates sum
while loop — adds natural numbers from 1 to n until condition is false

*Result:*
Prints number type, sum of list elements, and sum of natural numbers up to 10.

*Advantages:*
Covers all basic decision and looping structures
Easy to understand and implement
while loop useful when iterations are unknown

*Disadvantages:*
while loop can cause infinite loop if condition never becomes false
for loop not suitable when index manipulation is needed

*Where to Use:*
Decision making in any program
Processing lists and sequences
Repeating tasks until a condition is met


# lists

*Description:*
Demonstrates Python's core data structures — lists, dictionaries, and tuples, and how to access/modify them.

*How it Works:*
List — ordered, mutable, accessed by index (positive & negative)
Dictionary — key-value pairs, values updated by key
Tuple — ordered, immutable, cannot be changed after creation
len function assigned to a variable and used to get list length

*Result:*
Prints modified list elements, updated dictionary value, tuple, and length of list.

*Advantages:*
Lists and dicts are flexible and dynamic
Tuples are faster and safer (immutable)
Dictionary gives fast key-based lookup

*Disadvantages:*
Lists are slower than tuples
Dictionary keys must be unique
Tuples cannot be modified once created

*Where to Use:*
Lists — storing collections of items
Dictionaries — storing structured data like student records
Tuples — storing fixed data like coordinates or RGB values


# multiprocessing_test

*Description:*
Demonstrates Python multiprocessing — running multiple processes simultaneously to generate random numbers faster using all CPU cores.

*How it Works:*
Imports do_something function which generates random numbers
Creates 10 separate processes, each generating 10 million random numbers
All processes start together with j.start()
j.join() waits for all processes to finish
Records total execution time

*Result:*
Prints total time taken to complete all processes — faster than serial execution because processes run in parallel on multiple CPU cores.

*Advantages:*
True parallelism — uses multiple CPU cores
Much faster for CPU-heavy tasks
Bypasses Python's GIL (Global Interpreter Lock)

*Disadvantages:*
Higher memory usage — each process has its own memory
More overhead to create processes than threads
Inter-process communication is complex

*Where to Use:*
Heavy computation tasks (image processing, data analysis)
When tasks are CPU-bound
Scientific simulations


# multithreading_test

*Description:*
Demonstrates Python multithreading — running multiple threads to generate random numbers and comparing execution time with multiprocessing and serial execution.

*How it Works:*
Creates 10 threads, each running do_something with 10 million random numbers
All threads start with j.start()
j.join() waits for all threads to finish
Records total execution time

*Result:*
Prints total time taken — slower than multiprocessing because of Python's GIL which prevents true parallel execution of threads.

*Advantages:*
Lightweight — threads share same memory space
Good for I/O-bound tasks (file reading, network calls)
Less overhead than multiprocessing

*Disadvantages:*
GIL prevents true parallelism for CPU-bound tasks
Harder to debug — race conditions possible
Not efficient for heavy computation

*Where to Use:*
Web scraping
File downloading/uploading
Database queries
Any I/O-bound operations


# serial_test

*Description:*
Demonstrates serial (sequential) execution — running do_something one by one without any parallelism, used as a baseline to compare with multithreading and multiprocessing.

*How it Works:*
Runs do_something 10 times in a simple for loop
Each execution generates 10 million random numbers
One task completes before the next starts
Records total execution time

*Result:*
Prints total time taken — slowest among the three (serial, multithreading, multiprocessing) because tasks run one after another.

*Advantages:*
Simplest to write and debug
No race conditions or synchronization issues
Predictable execution order

*Disadvantages:*
Slowest — does not use multiple cores or threads
Not suitable for large scale or time-sensitive tasks

*Where to Use:*
Small simple scripts
When task order matters strictly
As a baseline to measure parallel performance


# thread_and_processes

*Description:*
Combines serial, multithreading, and multiprocessing in one file to compare their execution times for generating random numbers.

*How it Works:*
do_something generates 10 million random numbers
Serial (commented out) — runs tasks one by one
Multithreading — runs 10 threads simultaneously
Multiprocessing — runs 10 processes simultaneously
Records and prints time for each approach

*Result:*
Multiprocessing is fastest, multithreading is in between, serial is slowest — clearly shows performance difference between all three approaches.

*Advantages:*
All three approaches in one file for easy comparison
Shows real performance difference
Reusable do_something function

*Disadvantages:*
Threads affected by GIL — not truly parallel for CPU tasks
Multiprocessing uses more memory
Serial approach is too slow for large data

*Where to Use:*
Benchmarking parallel vs serial performance
Choosing best approach for a task
Learning difference between threading and multiprocessing


