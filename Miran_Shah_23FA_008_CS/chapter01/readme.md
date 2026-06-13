# Chapter 1

### Table of Contents
* [1. classes](#1-classes)
* [2. dir](#2-dir)
* [3. do_something](#3-do_something)
* [4. file](#4-file)
* [5. flow](#5-flow)
* [6. lists](#6-lists)
* [7. multiprocessing_test](#7-multiprocessing_test)
* [8. multithreading_test](#8-multithreading_test)
* [9. serial_test](#9-serial_test)
* [10. thread_and_processes](#10-thread_and_processes)

---

### 1. classes
* **What I Learned:** Learned how classes act as templates to create objects. Understood the difference between class variables (shared) and instance variables (separate for each object). Also learned basic inheritance.
* **How it Executes:** A class is defined, then multiple objects are created. Changing a class variable affects all objects, while changing an instance variable only affects one object. A child class inherits properties from the parent class.
* **End Use:** Useful for organizing complex data like user systems, applications, or structured programs.
* **Summary:** Introduces OOP concepts for better code structure and reuse.
* **Advantages:** Organized code, reusable structure  
* **Disadvantages:** Slightly complex for beginners  

---

### 2. dir
* **What I Learned:** Learned how to use conditions (if-else) and loops (for loop).
* **How it Executes:** Checks whether a number is positive, negative, or zero. Then loops through a list and calculates the total sum.
* **End Use:** Used in decision-making and processing collections of data.
* **Summary:** Demonstrates basic logic control using conditions and loops.
* **Advantages:** Simple and easy to understand  
* **Disadvantages:** Not efficient for large datasets  

---

### 3. do_something
* **What I Learned:** Learned how to create functions and use the random module.
* **How it Executes:** A function runs multiple times, generates random numbers, and stores them in a list.
* **End Use:** Useful for generating sample data, simulations, or testing.
* **Summary:** Shows how functions can automate repeated tasks.
* **Advantages:** Reusable and efficient  
* **Disadvantages:** Not secure for sensitive data  

---

### 4. file
* **What I Learned:** Learned how to write and read files.
* **How it Executes:** Opens a file in write mode, saves text, then reopens it in read mode and prints the content.
* **End Use:** Used for saving data like logs, reports, or user input.
* **Summary:** Basic file handling operations in Python.
* **Advantages:** Permanent data storage  
* **Disadvantages:** Risk of overwriting data if not careful  

---

### 5. flow
* **What I Learned:** Learned how program flow works using conditions and loops.
* **How it Executes:** Uses if condition, then a for loop to iterate over items, and a while loop that runs until a condition is met.
* **End Use:** Used to control how a program runs step by step.
* **Summary:** Controls execution flow using loops and conditions.
* **Advantages:** Automates repetitive tasks  
* **Disadvantages:** Infinite loop risk if condition is wrong  

---

### 6. lists
* **What I Learned:** Learned about lists, tuples, and dictionaries.
* **How it Executes:** Creates and modifies a list, accesses dictionary values using keys, and shows that tuples cannot be changed.
* **End Use:** Used for storing and managing collections of data.
* **Summary:** Demonstrates different data structures in Python.
* **Advantages:** Organized data storage  
* **Disadvantages:** Errors occur if wrong index or key is used  

---

### 7. multiprocessing_test
* **What I Learned:** Learned how to use multiple CPU cores using multiprocessing.
* **How it Executes:** Creates multiple processes that run tasks at the same time. The program waits until all processes finish.
* **End Use:** Used for heavy computations like data processing or calculations.
* **Summary:** Speeds up execution using parallel processing.
* **Advantages:** High performance for CPU tasks  
* **Disadvantages:** High memory usage  

---

### 8. multithreading_test
* **What I Learned:** Learned how threads work and how they share memory.
* **How it Executes:** Creates multiple threads that run tasks together, switching rapidly to simulate parallelism.
* **End Use:** Used in tasks like file handling, APIs, or network requests.
* **Summary:** Improves performance for tasks that involve waiting.
* **Advantages:** Lightweight and efficient  
* **Disadvantages:** Not useful for CPU-heavy tasks due to GIL  

---

### 9. serial_test
* **What I Learned:** Learned how normal sequential execution works.
* **How it Executes:** Runs tasks one by one in a loop, waiting for each to finish before starting the next.
* **End Use:** Used when tasks must follow a strict order.
* **Summary:** Baseline execution model for comparison.
* **Advantages:** Simple and predictable  
* **Disadvantages:** Slow for large workloads  

---

### 10. thread_and_processes
* **What I Learned:** Learned how to compare performance between execution methods.
* **How it Executes:** Runs the same task using serial execution, multithreading, and multiprocessing, then compares execution time.
* **End Use:** Used to decide the best method for performance optimization.
* **Summary:** Compares different execution techniques.
* **Advantages:** Helps choose the best approach  
* **Disadvantages:** Uses high CPU during testing  