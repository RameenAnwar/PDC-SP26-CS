# README - Python Topics Study Guide

## 1. Classes (Object Oriented Programming)

### What I Learned
- Creating classes and objects
- Constructor (`__init__`) method
- Instance methods and attributes
- Class variables vs instance variables
- Inheritance and method overriding
- Encapsulation (private/protected members)
- Polymorphism

### Advantages
- Code reusability through inheritance
- Better organization of code
- Data hiding and security
- Easy maintenance and debugging
- Real-world modeling

### Disadvantages
- Performance overhead compared to procedural code
- Steep learning curve for beginners
- Can be overkill for simple programs
- More memory consumption

### Real-world Applications
- Game development (characters, enemies)
- Banking systems (accounts, transactions)
- Student management systems
- GUI applications

---

## 2. Directory Operations (os/shutil/pathlib)

### What I Learned
- Creating, deleting, renaming directories
- Listing directory contents
- Navigating file system (absolute/relative paths)
- Recursive directory traversal (`os.walk`)
- Checking file/directory existence
- Getting file properties (size, modification time)

### Advantages
- Automate file system tasks
- Cross-platform compatibility
- Batch processing of multiple files
- Safe operations with existence checks

### Disadvantages
- Platform differences (path separators)
- Permission errors on protected directories
- Race conditions possible
- Slow with thousands of files

### Real-world Applications
- Backup automation scripts
- File organization tools
- Log file management
- Installation scripts

---

## 3. Functions & Utilities (do_something)

### What I Learned
- Function definition and calling
- Parameters and return values
- Default arguments and keyword arguments
- Variable arguments (`*args`, `**kwargs`)
- Lambda functions
- Decorators for function enhancement
- Error handling with try-except

### Advantages
- Code reusability
- Modular programming
- Easier testing and debugging
- Reduced code duplication

### Disadvantages
- Function call overhead
- Stack memory usage
- Can become complex with nested functions

### Real-world Applications
- Utility libraries
- API wrappers
- Data processing pipelines
- Automation scripts

---

## 4. File Handling

### What I Learned
- Reading files (text and binary)
- Writing and appending to files
- Different file modes (r, w, a, rb, wb)
- CSV file parsing
- JSON file operations
- Context managers (`with` statement)
- Exception handling for I/O errors

### Advantages
- Persistent data storage
- Handle large datasets
- Data sharing between programs
- Multiple format support (CSV, JSON, XML)

### Disadvantages
- Slower than RAM operations
- Disk space requirements
- I/O errors possible
- No built-in querying capability

### Real-world Applications
- Configuration files
- Data logging
- Report generation
- Data import/export tools

---

## 5. Control Flow (if/else, loops)

### What I Learned
- Conditional statements (if, elif, else)
- For loops and while loops
- Loop control (break, continue, pass)
- Nested loops
- List comprehensions
- Ternary operators

### Advantages
- Decision making in code
- Repetitive task automation
- Cleaner and more readable code
- Efficient iteration over data

### Disadvantages
- Infinite loop risk
- Nested loops can be slow
- Complex conditions hard to debug

### Real-world Applications
- User input validation
- Data filtering
- Search algorithms
- Game logic

---

## 6. Lists & Data Structures

### What I Learned
- List creation and manipulation
- List methods (append, extend, insert, remove)
- List slicing and indexing
- List comprehensions
- Tuples (immutable sequences)
- Dictionaries (key-value pairs)
- Sets (unique elements)

### Advantages
- Flexible data storage
- Built-in sorting and searching
- Memory efficient
- Fast operations

### Disadvantages
- Lists can be slow for large data
- No type enforcement
- Dictionary memory overhead

### Real-world Applications
- Shopping carts
- Student records
- Cache implementations
- Data aggregation

---

## 7. Multiprocessing

### What I Learned
- Creating multiple processes
- Process synchronization (Locks, Queues)
- Inter-process communication (Pipe, Queue)
- Process Pool for task management
- Shared memory (Value, Array)
- CPU-bound task optimization

### Advantages
- True parallel execution (No GIL limitation)
- Full multi-core CPU utilization
- Separate memory space (no race conditions)
- Process crash doesn't affect others

### Disadvantages
- High memory overhead
- Slow inter-process communication
- Complex data sharing
- Process creation overhead
- Platform dependent behavior

### Real-world Applications
- Image processing
- Video encoding
- Scientific computing
- Data analysis

---

## 8. Multithreading

### What I Learned
- Creating and managing threads
- Thread synchronization (Locks, RLocks)
- Race conditions and solutions
- Daemon threads for background tasks
- Thread Pool (concurrent.futures)
- GIL (Global Interpreter Lock) limitations

### Advantages
- Lightweight (less memory than processes)
- Shared memory access
- Responsive GUI applications
- Efficient for I/O bound tasks

### Disadvantages
- GIL limits CPU-bound performance
- Race conditions risk
- Debugging complexity
- Deadlock possibilities

### Real-world Applications
- Web scraping
- File downloading
- Chat applications
- Database operations

---

## 9. Serial vs Parallel vs Distributed Computing

### What I Learned
- **Serial Computing**: One instruction at a time, single processor
- **Parallel Computing**: Multiple instructions simultaneously, multiple cores
- **Distributed Computing**: Multiple computers working together
- Amdahl's Law (speedup limitations)
- When to use each approach

### Advantages of Parallel
- Faster execution
- Solve larger problems
- Better resource utilization

### Disadvantages of Parallel
- Communication overhead
- Synchronization complexity
- Not all problems can be parallelized

### Real-world Applications
- Weather forecasting (Parallel)
- Google Search (Distributed)
- Basic calculators (Serial)

---

## 10. Threads vs Processes Comparison

### What I Learned

| Feature | Threads | Processes |
|---------|---------|-----------|
| Memory | Shared | Separate |
| Creation | Fast | Slow |
| Communication | Easy (shared memory) | Complex (IPC) |
| GIL affected | Yes | No |
| Best for | I/O tasks | CPU tasks |
| Crash impact | All threads crash | Only that process |

### When to Use Threads
- Web scraping multiple websites
- File I/O operations
- Network requests
- GUI applications

### When to Use Processes
- Image/video processing
- Mathematical computations
- Machine learning training
- Data analysis

---

## Quick Reference Table

| Topic | Best For | Main Advantage | Main Disadvantage |
|-------|----------|----------------|-------------------|
| Classes | Large programs | Code reusability | Overhead |
| Multiprocessing | CPU tasks | True parallelism | Memory heavy |
| Multithreading | I/O tasks | Lightweight | GIL limitation |
| File Handling | Data storage | Persistence | Slow |
| Lists | Data collection | Flexible | No type safety |

