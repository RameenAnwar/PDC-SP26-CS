# 📚 Parallel & Distributed Computing – Assignment Summary (Chapter 1)

---

# 📄 Class.py

## 🔹 What we studied
- Classes & Objects (OOP)  
- Instance vs Class variables  
- Inheritance  

## 🔹 How to execute
- Create object: `instance = Myclass()`  
- Call function: `instance.myfunction()`  

## 🔹 End Use / When to use
- Large projects  
- Organizing data + functions  
- Reusable code  

## 🔹 Advantages
- Reusable  
- Organized  
- Easy maintenance  

## 🔹 Disadvantages
- Complex for small programs  
- Higher memory usage  

---

# 📄 dir.py

## 🔹 What we studied
- If-Else conditions  
- For loop  
- List iteration  
- Sum calculation  

## 🔹 How to execute
- Condition check: `if num > 0`  
- Loop: `for val in numbers`  

## 🔹 End Use / When to use
- Decision making  
- Data processing  

## 🔹 Advantages
- Easy logic building  
- Flexible  

## 🔹 Disadvantages
- Slow for large data  

---

# 📄 do_something.py

## 🔹 What we studied
- Function creation  
- Random number generation  

## 🔹 How to execute
- Call function: `do_something(count, out_list)`  

## 🔹 End Use / When to use
- Data generation  
- Testing parallel programs  

## 🔹 Advantages
- Reusable  
- Simple  

## 🔹 Disadvantages
- Not real-world logic  

---

# 📄 file.py

## 🔹 What we studied
- File handling (read/write)  

## 🔹 How to execute
- Open → Write → Close → Read  

## 🔹 End Use / When to use
- Store data  
- Logging  

## 🔹 Advantages
- Permanent storage  
- Easy  

## 🔹 Disadvantages
- Must close file  
- Slower than memory  

---

# 📄 flow.py

## 🔹 What we studied
- IF condition  
- FOR loop  
- WHILE loop  

## 🔹 How to execute
- Sequential execution (top to bottom)  

## 🔹 End Use / When to use
- Logic building  
- Iterations  

## 🔹 Advantages
- Easy  
- Fundamental concept  

## 🔹 Disadvantages
- Infinite loop risk  
- Slow for large loops  

---

# 📄 list.py

## 🔹 What we studied
- List, Tuple, Dictionary  
- Indexing & updating  
- Built-in functions  

## 🔹 How to execute
- Access: `mylist[0]`  
- Update: `mydict["pi"] = 3.15`  

## 🔹 End Use / When to use
- Data storage & manipulation  

## 🔹 Advantages
- Flexible  
- Easy access  

## 🔹 Disadvantages
- Mutable errors (list)  
- Tuple cannot change  

---

# 📄 multiprocessing_test.py

## 🔹 What we studied
- Multiprocessing  
- Parallel execution  

## 🔹 How to execute
- `multiprocessing.Process(...)`  

## 🔹 End Use / When to use
- CPU-intensive tasks  

## 🔹 Advantages
- Fast  
- True parallelism  

## 🔹 Disadvantages
- High memory usage  
- Complex  

---

# 📄 multithreading_test.py

## 🔹 What we studied
- Multithreading  

## 🔹 How to execute
- `threading.Thread(...)`  

## 🔹 End Use / When to use
- I/O tasks  

## 🔹 Advantages
- Lightweight  
- Faster for I/O  

## 🔹 Disadvantages
- GIL issue  
- Slow for CPU tasks  

---

# 📄 serial_test.py

## 🔹 What we studied
- Sequential execution  

## 🔹 How to execute
- Functions run one by one  

## 🔹 End Use / When to use
- Simple tasks  
- Debugging  

## 🔹 Advantages
- Simple  
- Easy debugging  

## 🔹 Disadvantages
- Slow  
- No parallelism  

---

# 📄 thread_and_processes.py

## 🔹 What we studied
- Comparison:
  - Serial  
  - Multithreading  
  - Multiprocessing  

## 🔹 How to execute
- Threads + Processes run together  

## 🔹 End Use / When to use
- Performance comparison  
- Optimization  

## 🔹 Advantages
- Clear comparison  
- Performance analysis  

## 🔹 Disadvantages
- Complex  
- Hard to debug  

---

# Final Summary

| File | Concept |
|------|--------|
| Class.py | OOP |
| dir.py / flow.py | Logic & Loops |
| list.py | Data Structures |
| file.py | File Handling |
| do_something.py | Helper Function |
| serial_test.py | Slow execution |
| multithreading_test.py | Fast I/O |
| multiprocessing_test.py | Fast CPU |

---