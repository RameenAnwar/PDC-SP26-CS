# Chapter 1 – Python Basics and Introduction to Parallel Computing

In this chapter, I learned basic Python concepts like classes, loops, lists, and file handling. It also introduced different ways of running programs like serial execution, multithreading, and multiprocessing.

---

## Topic: classes.py

What I Learned  
I learned how classes and objects work in Python. I also understood the difference between class variables and instance variables. Inheritance was also introduced.

How to Execute  
python classes.py  

Use / Output  
It creates objects and shows how variables behave inside a class. It also shows inheritance between classes.

When to Use  
When we want to design programs using real-world objects.

Advantages  
Code becomes organized  
Reusability of code  

Disadvantages  
Concept is a bit confusing at start  

Summary  
Classes help in structuring programs using objects.

---

## Topic: dir.py and flow.py

What I Learned  
I learned how to use if-else conditions and loops like for loop and while loop.

How to Execute  
python dir.py  
python flow.py  

Use / Output  
Checks whether number is positive or negative and performs loops on data.

When to Use  
Used in almost every program where decisions or repetition is needed.

Advantages  
Very important for logic building  
Easy to understand  

Disadvantages  
Can become confusing in complex cases  

Summary  
Conditions and loops control the flow of a program.

---

## Topic: do_something.py

What I Learned  
I learned how to define functions and generate random numbers.

How to Execute  
Used with other files (not always run alone)

Use / Output  
Generates a list of random numbers.

When to Use  
When we need reusable code or repeated operations.

Advantages  
Code reuse  
Better organization  

Disadvantages  
Sometimes hard to trace errors  

Summary  
Functions make code reusable and clean.

---

## Topic: file.py

What I Learned  
I learned file handling like reading and writing data into files.

How to Execute  
python file.py  

Use / Output  
Creates a file, writes data, and reads it back.

When to Use  
When working with permanent data storage.

Advantages  
Easy data storage  
Useful in real applications  

Disadvantages  
Need proper handling  
Risk of losing data  

Summary  
File handling is used to store and retrieve data.

---

## Topic: lists.py

What I Learned  
I learned about lists, tuples, and dictionaries.

How to Execute  
python lists.py  

Use / Output  
Stores and manipulates different types of data.

When to Use  
Lists → changeable data  
Tuples → fixed data  
Dictionary → key-value data  

Advantages  
Flexible and useful  

Disadvantages  
Can be confusing at first  

Summary  
Different data structures are used for different purposes.

---

## Topic: serial_test.py

What I Learned  
I learned that tasks run one by one in serial execution.

How to Execute  
python serial_test.py  

Use / Output  
Shows execution time of tasks.

When to Use  
When tasks depend on each other.

Advantages  
Simple  
Easy to debug  

Disadvantages  
Slow for large tasks  

Summary  
Serial execution is simple but slow.

---

## Topic: multithreading_test.py

What I Learned  
I learned how threads allow multiple tasks to run at the same time.

How to Execute  
python multithreading_test.py  

Use / Output  
Runs tasks faster compared to serial in some cases.

When to Use  
When tasks are independent.

Advantages  
Improves speed  

Disadvantages  
More complex  
Not always fully parallel in Python  

Summary  
Multithreading helps in running tasks simultaneously.

---

## Topic: multiprocessing_test.py

What I Learned  
I learned how multiple processes use CPU cores for parallel execution.

How to Execute  
python multiprocessing_test.py  

Use / Output  
Executes tasks faster using multiple CPUs.

When to Use  
For heavy computations.

Advantages  
Faster than threading  

Disadvantages  
Uses more memory  

Summary  
Multiprocessing provides true parallel execution.

---

## Topic: thread_and_processes.py

What I Learned  
I understood the difference between serial execution, threading, and multiprocessing.

How to Execute  
python thread_and_processes.py  

Use / Output  
Compares execution time of different methods.

When to Use  
When deciding which method to use.

Advantages  
Helps in optimization  

Disadvantages  
Slightly complex  

Summary  
Different execution methods affect performance differently.

---

## Final Understanding

In this chapter, I learned basic Python and different execution methods. I understood that serial execution is slow, threading is useful for some tasks, and multiprocessing is best for heavy work.