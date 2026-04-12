# Chapter 2 – Parallel Computing Concepts

In this chapter, I learned deeper concepts of parallel computing like CPU-bound and I/O-bound tasks, process pools, synchronization, and common problems like race conditions and deadlocks.

---

## Topic: cpu_bound.py

What I Learned  
I learned that CPU-bound tasks use a lot of processing power.

How to Execute  
python cpu_bound.py  

Use / Output  
Performs heavy calculations.

When to Use  
When dealing with complex computations.

Advantages  
Helps understand CPU usage  

Disadvantages  
Slow if not optimized  

Summary  
CPU-bound tasks need multiprocessing for better performance.

---

## Topic: io_bound.py

What I Learned  
I learned about tasks that wait for input/output operations.

How to Execute  
python io_bound.py  

Use / Output  
Simulates waiting operations.

When to Use  
When working with files or network.

Advantages  
Efficient with threading  

Disadvantages  
Not useful for heavy computation  

Summary  
I/O-bound tasks benefit from threading.

---

## Topic: pool_example.py

What I Learned  
I learned how process pools manage multiple processes.

How to Execute  
python pool_example.py  

Use / Output  
Runs tasks using a pool of workers.

When to Use  
When handling multiple tasks easily.

Advantages  
Cleaner code  

Disadvantages  
Hard to understand initially  

Summary  
Pools simplify multiprocessing.

---

## Topic: map_example.py

What I Learned  
I learned how to apply functions to multiple values using map.

How to Execute  
python map_example.py  

Use / Output  
Processes multiple inputs.

When to Use  
When same task is applied repeatedly.

Advantages  
Simple and efficient  

Disadvantages  
Less control  

Summary  
Map helps apply functions easily.

---

## Topic: async_example.py

What I Learned  
I learned about asynchronous programming.

How to Execute  
python async_example.py  

Use / Output  
Runs tasks without blocking.

When to Use  
In APIs or web tasks.

Advantages  
Faster response  

Disadvantages  
Hard to debug  

Summary  
Async allows non-blocking execution.

---

## Topic: timing_comparison.py

What I Learned  
I compared execution time of different methods.

How to Execute  
python timing_comparison.py  

Use / Output  
Shows which method is faster.

When to Use  
To analyze performance.

Advantages  
Helpful for decision making  

Disadvantages  
Depends on system  

Summary  
Different methods have different performance.

---

## Topic: chunking.py

What I Learned  
I learned how to divide tasks into smaller parts.

How to Execute  
python chunking.py  

Use / Output  
Processes data in chunks.

When to Use  
When dealing with large data.

Advantages  
Improves efficiency  

Disadvantages  
Needs planning  

Summary  
Chunking helps in better load distribution.

---

## Topic: synchronization.py

What I Learned  
I learned how to control access to shared data.

How to Execute  
python synchronization.py  

Use / Output  
Prevents conflicts between threads.

When to Use  
When multiple threads share data.

Advantages  
Prevents errors  

Disadvantages  
Slows execution  

Summary  
Synchronization ensures safe execution.

---

## Topic: race_condition.py

What I Learned  
I learned what happens when multiple threads access same data.

How to Execute  
python race_condition.py  

Use / Output  
Shows incorrect results.

When to Use  
To understand errors.

Advantages  
Helps debugging  

Disadvantages  
Causes unpredictable behavior  

Summary  
Race conditions cause wrong outputs.

---

## Topic: deadlock_example.py

What I Learned  
I learned about deadlocks where processes get stuck.

How to Execute  
python deadlock_example.py  

Use / Output  
Shows program getting stuck.

When to Use  
To understand system issues.

Advantages  
Improves understanding  

Disadvantages  
Hard to fix  

Summary  
Deadlocks stop program execution.

---

## Final Understanding

In this chapter, I learned how to improve performance using parallel computing and also understood common problems like race conditions and deadlocks.