# Chapter 03 Summary

# 1. communicating_with_pip:

## What I studied:
I studied how inter-process communication works using pipes in multiprocessing. I learned how two separate processes can exchange data in a structured way where one process sends data and the other receives it. I also understood how pipes help in building a communication channel between processes that do not share memory directly.

## Definition:
A pipe is a unidirectional or bidirectional communication mechanism in multiprocessing that provides two endpoints (send and receive) to transfer data between processes safely and efficiently.

## How I executed:
I created two pipes and multiple processes. In the first process, I sent numbers from 0 to 9 through a pipe. In the second process, I received those numbers, performed square operation, and sent the results through another pipe. The main process continuously received and printed the processed results until the pipe closed.

## End uses:
- Communication between multiple processes
- Data streaming in pipeline systems
- Parallel data processing workflows
- Parent-child process communication

## Advantages:
- Fast and direct communication
- Simple structure for data transfer
- Efficient for linear data pipelines
- Works well in producer-consumer models

## Disadvantages:
- Limited to connected processes only
- Not suitable for complex multi-process networks
- Harder to scale in large systems
- Requires careful handling of pipe closure


# 2. communicating_with_queue:

## What I studied:
I studied how a queue is used in multiprocessing for safe and structured communication between processes. I learned the producer-consumer model where one process generates data and another process consumes it. I also understood how queues handle synchronization automatically without manual locking.

## Definition:
A queue in multiprocessing is a FIFO (First In First Out) data structure that allows multiple processes to safely add and remove data while maintaining order and preventing data corruption.

## How I executed:
I created a producer process that generates random numbers and adds them into a shared queue. At the same time, a consumer process continuously checks the queue, retrieves items, and prints them until the queue becomes empty. I also added delays to simulate real-world processing behavior.

## End uses:
- Producer-consumer systems
- Task scheduling systems
- Load balancing in processes
- Real-time data processing pipelines

## Advantages:
- Safe for multiple processes
- Automatic synchronization
- Supports multiple producers and consumers
- Easy to implement in real systems

## Disadvantages:
- Slightly slower than direct communication
- It can become a bottleneck under heavy load
- Requires monitoring of queue size
- Memory usage can increase with large queues


# 3. killing_processes:

## What I studied:
I studied how a running process behaves in different states such as running, terminated, and completed. I learned how processes can be forcibly stopped and how the system handles this type of termination. I also understood the risks of interrupting a running process.

## Definition:
Process termination is the forced stopping of a process before it completes execution, which immediately halts all its operations regardless of its current state.

## How I executed:
I created a process that runs a loop printing numbers with delays. After starting the process, I immediately terminated it using the terminate() method. I then checked its status using is_alive() and exitcode to observe its state after termination.

## End uses:
- Stopping infinite loops or stuck processes
- System resource management
- Debugging and testing process behavior
- Controlling background tasks

## Advantages:
- Gives full control over processes
- Stops unwanted or faulty execution
- Helps to manage system performance
- Useful for debugging

## Disadvantages:
- It can cause incomplete operations
- Risk of data loss or corruption
- Unsafe for critical processes
- Sudden termination may leave resources uncleaned


# 4. myfunc:

## What I studied:
I studied how a simple function behaves when executed inside a separate process. I learned how multiprocessing allows functions to run independently in different memory spaces. I also understood how arguments are passed to processes.

## Definition:
A function is a reusable block of code that performs a specific task when called. Multiprocessing uses functions to run on its own in different memory areas.

## How I executed:
I defined a function that takes an integer input and prints values from 0 to that number. The function was executed inside a separate process, which demonstrated independent execution from the main program.

## End uses:
- Learning basic multiprocessing concepts
- Testing process execution behavior
- Running independent tasks in parallel
- Simple demonstrations of process creation

## Advantages:
- Very easy to implement
- Helps to understand multiprocessing basics
- Lightweight and fast execution
- No complex structure required

## Disadvantages:
- Limited functionality
- Not suitable for large systems
- No direct inter-process communication
- It lacks structure and scalability


# 5. naming_processes

## What I studied:
I studied how processes can be identified and managed using names in multiprocessing. I learned the difference between default system-generated process names and user-defined names. I also understood how naming helps in debugging and tracking processes.

## Definition:
Process naming is a feature in multiprocessing that allows assigning a custom name to a process so that it can be easily identified during execution and debugging.

## How I executed:
I created two processes. One process was given a custom name, while the other used the default system name. Both processes printed their names during execution to show how naming works in multiprocessing.

## End uses:
- Process monitoring and debugging
- Logging process activity
- Managing multiple concurrent processes
- Identifying process roles in systems

## Advantages:
- Improves debugging 
- It helps to track multiple processes
- Makes logs more readable
- Useful in large applications

## Disadvantages:
- Only useful for identification
- No effect on performance
- Optional feature, it is not required
- Can be ignored in small programs


# 6. processes_in_subclass

## What I studied:
I studied how multiprocessing can be implemented using object-oriented programming by creating custom process classes. I learned how the run() method defines the behavior of a process. I also understood how subclassing helps organize complex process logic.

## Definition:
A subclassed process is a custom class that inherits from multiprocessing.Process and overrides the run() method to define the specific behavior of that process.

## How I executed:
I created a custom class that inherits from the Process class and implemented the run() method. Then I created multiple objects of this class and executed them using start() and join() methods to run processes independently.

## End uses:
- Object-oriented multiprocessing design
- Large-scale application development
- Reusable process logic
- Structured parallel programming

## Advantages:
- Clean and organized code structure
- Easy to extend functionality
- Better for complex systems
- Supports reusable design

## Disadvantages:
- More complex than simple functions
- Requires OOP knowledge
- Slight overhead in design
- Not ideal for simple tasks


# 7. process_pool

## What I studied:
I studied how process pools are used to manage multiple worker processes efficiently. I learned how tasks are distributed among a fixed number of processes automatically. I also understood how this improves performance in parallel execution.

## Definition:
A process pool is a group of worker processes that execute tasks in parallel by distributing work among a fixed number of active processes.

## How I executed:
I created a pool of 4 processes and used the map() function to apply a square operation on numbers from 0 to 99. The pool automatically distributed tasks among available worker processes and collected the results.

## End uses:
- Parallel computation tasks
- Batch processing systems
- Data transformation operations
- CPU-intensive workloads

## Advantages:
- Efficient use of CPU resources
- Easy parallel execution
- Reduces process creation overhead
- Simple task distribution

## Disadvantages:
- Fixed number of workers
- Less control over individual tasks
- Not suitable for dynamic workloads
- Can block if tasks are uneven


# 8. process_barrier

## What I studied:
I studied how process synchronization works using barriers and locks. I learned how multiple processes can be made to wait for each other before continuing execution. I also understood how synchronization helps in coordinated parallel execution.

## Definition:
A barrier is a synchronization barirer that blocks processes until a specified number of processes have reached a certain point before allowing them to continue execution.

## How I executed:
I created multiple processes, where some used a barrier to synchronize their execution. These processes waited until all reached the barrier before continuing. I also used locks to make sure that output printing was not mixed between processes.

## End uses:
- Process synchronization
- Parallel execution coordination
- Performance testing
- Controlled execution of tasks

## Advantages:
- Ensures synchronized execution
- Prevents race conditions in timing
- Useful for coordinated tasks
- Improves testing accuracy

## Disadvantages:
- It can slow down execution
- It can have risk of deadlocks if misused
- Requires careful coordination
- Not needed for independent tasks


## 9. run_background_processes_nodaemons.py:

### What I Studied:  
I studied multiprocessing with non-daemon processes. I learned how processes are created using the multiprocessing module and how they run independently. I also understood that non-daemon processes continue execution until they complete their task, even if the main program finishes.

### Definition:  
A non-daemon process is a type of process that runs independently and continues execution until it completes its assigned task, even if the main program has already ended.

### How I Executed:  
I created two processes using multiprocessing.Process and assigned them different names. I set daemon = False for both processes. Each process executed the same function, which printed numbers based on its name and then exited after a delay.

### End Uses:  
- Used in file processing systems  
- Used in large data analysis tasks  
- Used in scientific simulations  
- Used in long-running CPU intensive operations  

### Advantages:  
- Processes run independently  
- Ensures complete execution of tasks  
- Suitable for long-running and CPU-heavy tasks  
- Reliable even if main program ends  

### Disadvantages:  
- Uses more memory and system resources  
- Process creation is slower than threads  
- Communication between processes is harder  
- Higher overhead compared to threading  


## 10. run_background_processes.py:

### What I Studied:  
I studied the concept of daemon and non-daemon processes in multiprocessing. I learned that daemon processes run in the background and automatically stop when the main program exits, unlike normal processes.

### Definition:  
A daemon process is a background process that runs independently but automatically terminates when the main program finishes execution.

### How I Executed:  
I created two processes, one with daemon = True and the other with daemon = False. Both ran the same function, but I observed that the daemon process may not complete execution if the main program finishes early.

### End Uses:  
- Used in logging systems  
- Used in monitoring services  
- Used in background helper tasks  
- Used in system maintenance processes  

### Advantages:  
- Runs in background without blocking main program  
- Lightweight and easy to manage  
- Automatically stops with main program  
- Useful for non-critical background tasks  

### Disadvantages:  
- May stop before completing execution  
- Not suitable for important tasks  
- Can cause incomplete results  
- Less control over execution lifecycle  


## 11. spawning_processes_namespace.py:

### What I Studied:  
I studied how to create multiple processes using functions imported from another module. I learned how multiprocessing works in a modular structure and how code can be separated into different files.

### Definition:  
Process spawning with namespaces is the creation of multiple processes that execute imported functions from other modules to support modular programming.

### How I Executed:  
I imported a function from another file and used a loop to create multiple processes. Each process executed the function with a different argument. I used start() and join() to control execution.

### End Uses:  
- Used in modular software systems  
- Used in large-scale applications  
- Used in reusable code structures  
- Used in distributed task execution  

### Advantages:  
- Promotes modular programming  
- Code is reusable and organized  
- Easy to maintain large projects  
- Supports separation of concerns  

### Disadvantages:  
- Requires correct file structure  
- Import errors can occur  
- Debugging across files is harder  
- Slightly more complex setup  


## 12. spawning_processes.py:

### What I Studied:  
I studied the basic concept of process spawning in multiprocessing. I learned how multiple processes can run the same function with different inputs to achieve parallel execution.

### Definition:  
Process spawning is the creation of multiple independent processes that run in parallel to execute tasks simultaneously.

### How I Executed:  
I created a loop that generated multiple processes. Each process called the same function with a different value and printed output independently. I used start() and join() to manage execution.

### End Uses:  
- Used in parallel computing tasks  
- Used in batch processing systems  
- Used in simulations and modeling  
- Used in big data processing  

### Advantages:  
- Enables true parallel execution  
- Improves CPU utilization  
- Simple implementation  
- Independent task execution  

### Disadvantages:
- High memory usage  
- Process creation overhead  
- Difficult data sharing between processes  
- Harder debugging process  
