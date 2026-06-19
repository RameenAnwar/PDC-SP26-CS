# 📚 Parallel & Distributed Computing – Assignment Summary(Chapter 2)

This repository contains summaries of different Python programs related to threading, synchronization, and basic concepts.

---

# 📄 Barrier.py

## 🔹 What we studied
- Barrier synchronization  
- Threads wait until all reach same point  

## 🔹 How to execute
- Threads run → `wait()` → all threads pause → then continue  

## 🔹 End Use / When to use
- When multiple threads must complete a phase before moving forward  

## 🔹 Advantages
- Simple synchronization  
- Ensures all threads finish phase  

## 🔹 Disadvantages
- Deadlock risk  
- Fixed number of threads  

---

# 📄 condition.py

## 🔹 What we studied
- Condition variable  
- Producer–Consumer problem  

## 🔹 How to execute
- `wait()` → thread sleeps  
- `notify()` → wakes another thread  

## 🔹 End Use / When to use
- When threads share resources and need coordination  

## 🔹 Advantages
- Efficient communication  
- Avoids busy waiting  

## 🔹 Disadvantages
- Complex  
- Deadlock possible  

---

# 📄 event.py

## 🔹 What we studied
- Event signaling between threads  

## 🔹 How to execute
- `event.set()` → signal  
- `event.wait()` → wait for signal  

## 🔹 End Use / When to use
- Simple thread communication  

## 🔹 Advantages
- Easy  
- Lightweight  

## 🔹 Disadvantages
- Limited control  

---

# 📄 myThreadclass.py

## 🔹 What we studied
- Custom thread class  
- Thread execution  

## 🔹 How to execute
- Create object → `.start()`  

## 🔹 End Use / When to use
- Running tasks in parallel  

## 🔹 Advantages
- Organized  
- Reusable  

## 🔹 Disadvantages
- No synchronization  
- Race conditions  

---

# 📄 myThreadclass_lock.py

## 🔹 What we studied
- Lock (mutual exclusion)  

## 🔹 How to execute
- `acquire()` → critical section → `release()`  

## 🔹 End Use / When to use
- Protect shared resources  

## 🔹 Advantages
- Prevents data corruption  

## 🔹 Disadvantages
- Slower  
- Deadlock risk  

---

# 📄 myThreadclass_lock2.py

## 🔹 What we studied
- Partial locking  

## 🔹 How to execute
- Lock only critical part → rest runs parallel  

## 🔹 End Use / When to use
- Improve performance with safety  

## 🔹 Advantages
- Faster  
- Better concurrency  

## 🔹 Disadvantages
- Risky if misused  

---

# 📄 Rlock.py

## 🔹 What we studied
- Reentrant Lock (RLock)  

## 🔹 How to execute
- Same thread can lock multiple times  

## 🔹 End Use / When to use
- Nested locking scenarios  

## 🔹 Advantages
- Prevents self-deadlock  

## 🔹 Disadvantages
- Slower  
- Complex  

---

# 📄 Semaphore.py

## 🔹 What we studied
- Semaphore (limited access control)  

## 🔹 How to execute
- `acquire()` → wait  
- `release()` → allow next  

## 🔹 End Use / When to use
- Limited resources (DB, connections)  

## 🔹 Advantages
- Controls resource usage  

## 🔹 Disadvantages
- Hard to debug  

---

# 📄 Thread_defination.py

## 🔹 What we studied
- Basic thread creation  

## 🔹 How to execute
- Create → start → join  

## 🔹 End Use / When to use
- Simple parallel tasks  

## 🔹 Advantages
- Easy  

## 🔹 Disadvantages
- Not truly parallel (due to join in loop)  

---

# 📄 Thread_determine.py

## 🔹 What we studied
- Thread naming  

## 🔹 How to execute
- Threads print start & exit  

## 🔹 End Use / When to use
- Debugging threads  

## 🔹 Advantages
- Easy tracking  

## 🔹 Disadvantages
- No synchronization  

---

# 📄 Thread_name_and_class_processes.py

## 🔹 What we studied
- Thread class with names  

## 🔹 How to execute
- Threads start → print names  

## 🔹 End Use / When to use
- Identify threads  

## 🔹 Advantages
- Clean structure  

## 🔹 Disadvantages
- Basic use  

---

# 📄 Threading_with_queue.py

## 🔹 What we studied
- Queue (thread-safe)  
- Producer–Consumer  

## 🔹 How to execute
- `put()` → add item  
- `get()` → remove item  

## 🔹 End Use / When to use
- Safe data sharing  

## 🔹 Advantages
- No manual locking  
- Thread-safe  

## 🔹 Disadvantages
- Slight overhead  
- Infinite loop risk  

---

# Final Summary

| Concept | Use |
|--------|-----|
| Barrier | Wait for all threads |
| Condition | Producer–Consumer |
| Event | Signal |
| Lock | Protect data |
| RLock | Nested locks |
| Semaphore | Limited access |
| Queue | Safe sharing |

---