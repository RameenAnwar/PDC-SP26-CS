# Chapter 2 – Parallel Programming in Python

## Student Information

**Name:** Uzair
**Roll Number:** 23FA-034-CS

---

## Overview

This chapter introduces parallel programming concepts in Python, focusing on serial execution, multithreading, and multiprocessing to improve performance and efficiency.

---

## Serial Execution (serial_test.py)

### Learning Outcome

Learned that tasks execute one after another in a sequence.

### Execution

```
python serial_test.py
```

### Use Case

Used in simple programs where concurrency is not required.

### Summary

Sequential execution model.

### Pros

* Easy to implement

### Cons

* Slower performance

---

## Multithreading (multithreading_test.py)

### Learning Outcome

Understood how multiple threads run concurrently within a program.

### Execution

```
python multithreading_test.py
```

### Use Case

Used for I/O-bound tasks.

### Summary

Concurrent execution using threads.

### Pros

* Improves responsiveness

### Cons

* Limited by Global Interpreter Lock (GIL)

---

## Multiprocessing (multiprocessing_test.py)

### Learning Outcome

Learned how processes run independently to achieve true parallelism.

### Execution

```
python multiprocessing_test.py
```

### Use Case

Used for CPU-intensive tasks.

### Summary

Parallel execution using multiple processes.

### Pros

* Utilizes multiple CPU cores

### Cons

* Higher memory usage

---

## Threading vs Multiprocessing (thread_and_processes.py)

### Learning Outcome

Compared performance and use cases of threading and multiprocessing.

### Execution

```
python thread_and_processes.py
```

### Use Case

Helps in selecting the appropriate execution model.

### Summary

Performance comparison of concurrency techniques.

---

## Final Summary

This chapter introduced different execution models in Python and demonstrated how performance can be optimized using parallel programming techniques.

---

## Conclusion

Through this chapter, I gained a clear understanding of how to execute tasks efficiently using threading and multiprocessing, and when to apply each approach.
