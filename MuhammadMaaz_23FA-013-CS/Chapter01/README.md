Chapter 01 Summary

1. classes.py
What I studied: I studied classes, instance vs class variables, methods, and inheritance.  
How I executed: I ran the class `Myclass` with instance and class variables. I also studied and called methods, updated class variables, and ran the class `AnotherClass` which inherits from `Myclass`. I created instances and saw how variables and methods behave.  
End uses: It is used to model real world things like users, products, or objects in programs. It also helps to oragnize and re use code. Used in Object Oriented Programming.  
Advantages: Organizes code, reusable, easy to extend with inheritance, models real world objects.   
Disadvantages: Class variables can cause bugs and inheritance can complicate code. We Also need to carefully manage instance vs class variables.

2. dir.py
What I studied: I studied `if/elif/else` and `for` loops.  
How I executed: I checked if a number is positive, zero, or negative, and calculated the sum of a list of numbers using a `for` loop.  
End uses: Decision making, calculations, and validations.  
Advantages: Simple, easy to read, foundational for all programs.  
Disadvantages: Repetitive if overused. They can be basic for larger programs.

3. do_something.py
What I studied: I studied how to create reusable functions.  
How I executed: I read the function in the file and ran it, function generates random numbers and appends them to a list.  
End uses: Can be imported by other programs. They are useful for repeated tasks.  
Advantages: It keeps code reusable and simple.  
Disadvantages: It can cause issues with concurrency or threads.

4. file.py
What I studied: I studied reading and writing files in Python.  
How I executed: I wrote and ran two lines to `test.txt` then read them back, and printed the content.  
End uses: Storing logs, program output, short storage, memory.  
Advantages: Data storage, simple API. It works with many file types.  
Disadvantages: Manual `close()` can cause leaks, also can have errors if file is missing. Different data types can cause errors.

5. flow.py
What I studied: I studied `if/elif/else`, `for` loops, and `while` loops.  
How I executed: I checked number signs with `if'. I summed a list with `for` loop and added natural numbers with `while`.  
End uses: Main logic for almost any program: decision-making, iteration, calculations.  
Advantages: It is easy to read, flexible, used everywhere in programming. It supports all logic flows.  
Disadvantages: `while` loops can run infinitely if not careful, syntax errors possible.

6. lists.py
What I studied: I studied lists, dictionaries, tuples, indexing, updating values, and assigning functions to variables.  
How I executed: I created a list, dictionary, and tuple, updated values, and used `len()` to check length.  
End uses: Managing ordered data (lists), key-value mapping (dicts), and fixed collections (tuples) in programs.  
Advantages: Flexible, fast lookups with dictionaries, easy to manipulate lists, tuples are less resource taking.  
Disadvantages: Dicts use more memory, tuples cannot be modified, mistakes in indexing can cause errors.

7. multiprocessing_test.py
What I studied: I studied running multiple processes for parallel execution.  
How I executed: I ran 10 processes using `multiprocessing.Process` and ran the `do_something` function in each and measured execution time.  
End uses: CPU-heavy tasks, simulations, large data processing.  
Advantages: True parallelism, faster for CPU tasks, predictable memory per process.  
Disadvantages: It uses more memory, each process has separate memory which mean sharing data is difficult.

8. multithreading_test.py
What I studied: I studied running multiple threads concurrently for I/O-bound tasks.  
How I executed: I ran 10 threads using `threading.Thread` to run `do_something` and measured execution time.  
End uses: I/O-heavy tasks like file reading/writing, web requests, or network tasks.  
Advantages: Lightweight, shared memory, faster I/O tasks, simple to start.  
Disadvantages: race conditions possible, function references must be correct or can have errors.

9. serial_test.py 
What I studied: I studied sequential execution of tasks.  
How I executed: I ran `do_something` 10 times one after another and measured execution time.  
End uses:It can be used for comparision with parallel approaches, simple predictable execution.  
Advantages: It is easy to debug, predictable, no concurrency issues.  
Disadvantages: It is the slowest approach, no parallelism, not suitable for large CPU-heavy tasks.

10. thread_and_processes.py
What I studied: I studied and compared serial, multithreading, and multiprocessing approaches.  
How I executed: I ran all three approaches (serial, then threading, then multiprocessing) on the same workload and measured execution times.  
End uses: end uses for serial, multithreading and multiprocessing are respectively: simple to run, faster for cpu tasks, faster for i/o tasks.  
Advantages: By this file i understood side-by-side comparison.
Disadvantages: race condition possible for threading, multiprocessing uses more memory, serial is slowest approach.
