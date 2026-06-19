# Chapter 3 – Process Based Parallelism

---

# communication_with_pipe.py

## 🔹 What we studied
- Pipes (Inter-process communication)  
- Data transfer between processes  

## 🔹 How to execute
- Create pipe → `Pipe()`  
- Send → `send()`  
- Receive → `recv()`  

## 🔹 End Use / When to use
- When 2 processes need to communicate  

## 🔹 Advantages
- Fast  
- Simple  

## 🔹 Disadvantages
- Limited processes  
- Blocking risk  

---

# communicating_with_queue.py

## 🔹 What we studied
- Queue (IPC)  
- Producer–Consumer using processes  

## 🔹 How to execute
- Create queue → `Queue()`  
- Add → `put()`  
- Remove → `get()`  

## 🔹 End Use / When to use
- Multiple process communication  

## 🔹 Advantages
- Safe  
- Easy  

## 🔹 Disadvantages
- Slower than pipe  
- Overhead  

---

# killing_process.py

## 🔹 What we studied
- Process termination  

## 🔹 How to execute
- `process.start()`  
- `process.terminate()`  
- `process.join()`  

## 🔹 End Use / When to use
- Stop unwanted process  

## 🔹 Advantages
- Quick stop  

## 🔹 Disadvantages
- Data loss risk  

---

# myFunc.py

## 🔹 What we studied
- Function for process execution  

## 🔹 How to execute
- Pass in process → `target=myFunc`  

## 🔹 End Use / When to use
- Task execution in processes  

## 🔹 Advantages
- Simple  

## 🔹 Disadvantages
- Limited logic  

---

# naming_process.py

## 🔹 What we studied
- Process naming  

## 🔹 How to execute
- `Process(name="...")`  

## 🔹 End Use / When to use
- Debugging  

## 🔹 Advantages
- Easy identification  

## 🔹 Disadvantages
- No functional impact  

---

# process_in_subclass.py

## 🔹 What we studied
- Custom Process class  

## 🔹 How to execute
- Inherit `Process`  
- Override `run()`  

## 🔹 End Use / When to use
- Complex process logic  

## 🔹 Advantages
- Organized  

## 🔹 Disadvantages
- More code  

---

# process_pool.py

## 🔹 What we studied
- Process Pool  

## 🔹 How to execute
- `Pool()`  
- `pool.map()`  

## 🔹 End Use / When to use
- Parallel execution of many tasks  

## 🔹 Advantages
- Efficient  

## 🔹 Disadvantages
- Less control  

---

# process_barrier.py

## 🔹 What we studied
- Barrier in multiprocessing  

## 🔹 How to execute
- Processes wait using barrier  

## 🔹 End Use / When to use
- Synchronization  

## 🔹 Advantages
- Ensures sync  

## 🔹 Disadvantages
- Deadlock risk  

---

# run_background_process.py

## 🔹 What we studied
- Daemon processes  

## 🔹 How to execute
- `process.daemon = True`  

## 🔹 End Use / When to use
- Background tasks  

## 🔹 Advantages
- Auto stop with main program  

## 🔹 Disadvantages
- Not independent  

---

# run_background_process_no_daemons.py

## 🔹 What we studied
- Non-daemon processes  

## 🔹 How to execute
- Default (`daemon = False`)  

## 🔹 End Use / When to use
- Independent execution  

## 🔹 Advantages
- Runs independently  

## 🔹 Disadvantages
- Manual management  

---

# spawning_process.py

## 🔹 What we studied
- Process creation (spawning)  

## 🔹 How to execute
- `Process(target=func)`  
- `start()` → `join()`  

## 🔹 End Use / When to use
- Run multiple processes  

## 🔹 Advantages
- Simple  

## 🔹 Disadvantages
- Overhead  

---

# spawning_process_namespace.py

## 🔹 What we studied
- Import function in multiprocessing  

## 🔹 How to execute
- Import → `from myFunc import myFunc`  
- Use in process  

## 🔹 End Use / When to use
- Modular programming  

## 🔹 Advantages
- Clean code  

## 🔹 Disadvantages
- Dependency management  

---

# Final Summary

| Concept | Use |
|--------|-----|
| Pipe | Process communication |
| Queue | Safe communication |
| Terminate | Stop process |
| Pool | Parallel execution |
| Barrier | Synchronization |
| Daemon | Background |
| Spawn | Create processes |

---