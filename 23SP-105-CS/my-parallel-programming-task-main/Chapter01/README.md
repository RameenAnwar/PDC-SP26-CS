# Chapter 1: Python Basics & Introduction to Parallel Programming

This folder contains the introductory code files for understanding basic Python concepts and evaluating the performance differences between Serial Execution, Multithreading, and Multiprocessing in Python.

## 📂 File Overview

### 1. Python Basics
These scripts cover the fundamental concepts of Python programming:
* **`flow.py` & `dir.py`**: Demonstrates basic control flow statements including `if/elif/else` conditions, `for` loops, and `while` loops.
* **`lists.py`**: Shows how to work with core Python data structures like Lists, Dictionaries, and Tuples.
* **`classes.py`**: An introduction to Object-Oriented Programming (OOP) in Python. It covers creating classes, object instances, instance vs. class variables, and basic inheritance.
* **`file.py` & `test.txt`**: Demonstrates basic File I/O operations (writing to and reading from `test.txt`).

### 2. Parallel Programming & Performance Testing
These scripts compare the execution time of a heavy task using different execution models:
* **`do_something.py`**: Contains a helper function `do_something(count, out_list)` that generates random numbers and appends them to a list. This acts as our "heavy task" for performance testing.
* **`serial_test.py`**: Runs the `do_something` function sequentially (one after another) in a single process/thread.
* **`multithreading_test.py`**: Executes the same task concurrently using Python's `threading` module to create 10 separate threads.
* **`multiprocessing_test.py`**: Executes the task using Python's `multiprocessing` module, spawning 10 separate processes to bypass the Global Interpreter Lock (GIL) and utilize multiple CPU cores.

## 🚀 How to Run the Performance Tests

To see the difference in execution times, run the test files from your terminal/command prompt:

```bash
# Run the serial execution test
python serial_test.py

# Run the multithreading test
python multithreading_test.py

# Run the multiprocessing test
python multiprocessing_test.py
```

## 👨‍💻 Author
**Huzaifa Alim** - Computer Science Student @ Usman Institute of Technology

## 📜 License
This project is open source and available under the MIT License.

