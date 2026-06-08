# Python Fundamentals and Parallel Programming

## Student Information
**Name:** Shameer Waqar  
**Roll Number:** 23FA-011-CS  

---

## Overview
This repository serves as an introduction to core Python programming constructs and the transition into parallel execution. The objective is to establish a strong programming foundation while demonstrating how performance can be significantly optimized using multithreading and multiprocessing techniques.

---

## Core Fundamentals

### Classes and Objects (`classes.py`)
* **Description:** An introduction to Object-Oriented Programming (OOP). Covers class creation, inheritance, and the distinction between instance and class variables.
* **Execution:** `python classes.py`
* **Use Case:** Essential for designing structured, scalable, and modular applications.
* **Pros & Cons:** Promotes code reusability and organization, but requires a solid grasp of OOP paradigms.

### Conditional Statements and Loops (`dir.py`, `flow.py`)
* **Description:** Explores the core control flow mechanisms of Python, including decision-making conditions and iterative loops.
* **Execution:** `python dir.py` & `python flow.py`
* **Use Case:** Used to enforce logic, automate repetitive tasks, and control execution paths.
* **Pros & Cons:** Fundamental for logic building; however, poor implementation can lead to infinite loops or logical errors.

### Data Structures (`lists.py`)
* **Description:** A practical look at Python's built-in collections, specifically focusing on lists, dictionaries, and tuples.
* **Execution:** `python lists.py`
* **Use Case:** Applied whenever complex, grouped, or sequential data needs to be stored and manipulated.
* **Pros & Cons:** Highly flexible and dynamic, but requires understanding mutability and performance implications.

### File Handling (`file.py`)
* **Description:** Demonstrates how to programmatically interact with the file system to read, write, and append data.
* **Execution:** `python file.py`
* **Use Case:** Vital for scripts that require permanent data persistence, logging, or configuration management.
* **Pros & Cons:** Allows for permanent storage, but improper handling can result in data corruption or loss.

### Functions (`do_something.py`)
* **Description:** Focuses on encapsulating logic into isolated, reusable function blocks to clean up the main execution thread.
* **Use Case:** Used universally to simplify programs and avoid code duplication.

---

## Execution Models

### Serial Execution (`serial_test.py`)
* **Description:** Demonstrates the default execution model where tasks are processed sequentially, one strictly after the other.
* **Pros & Cons:** Highly predictable and easy to debug, but inherently slower for large-scale operations.

### Multithreading (`multithreading_test.py`)
* **Description:** Introduces concurrency by allowing multiple threads to overlap task execution within a single process.
* **Pros & Cons:** Excellent for I/O-bound tasks, but limited by Python's Global Interpreter Lock (GIL) for heavy computations.

### Multiprocessing (`multiprocessing_test.py`)
* **Description:** Bypasses the GIL by spawning entirely independent processes, achieving true parallelism.
* **Pros & Cons:** The best solution for CPU-bound, heavy computational tasks, though it consumes significantly more memory.

### Threading vs Multiprocessing (`thread_and_processes.py`)
* **Description:** A direct performance benchmark comparing multithreading and multiprocessing side-by-side.
* **Use Case:** Used as a reference guide to determine which parallel execution method is appropriate for a specific problem.

---

## Conclusion
This chapter successfully bridged the gap between basic Python programming and advanced execution strategies. By mastering OOP, data structures, and the distinct advantages of both multiprocessing and multithreading, I am better equipped to write highly efficient, scalable, and optimized Python applications.