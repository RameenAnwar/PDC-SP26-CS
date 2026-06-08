# Chapter 4 – Message Passing Interface (MPI)

## Topic: alltoall.py

### What I Learned
I learned how to use `Alltoall` communication in MPI. In this method, every process sends data to every other process and also receives data from every other process.

### How to Execute
```bash
mpiexec -n 4 python alltoall.py
```

### Use / Output
Each process creates an array based on its rank and sends parts of that data to all other processes. Every process receives one value from each process.

Example output:
```text
process 0 sending [0 0 0 0] receiving [...]
process 1 sending [0 2 4 6] receiving [...]
process 2 sending [0 3 6 9] receiving [...]
process 3 sending [0 4 8 12] receiving [...]
```

### When to Use
Use `Alltoall` when every process needs to exchange data with every other process.

### Advantages
- Allows full data exchange between processes
- Useful in distributed computing
- Good for parallel algorithms where every process needs data from others

### Disadvantages
- Can become expensive with many processes
- Communication overhead is high
- More difficult to understand than simple send/receive

### Summary
`Alltoall` communication allows all MPI processes to send and receive data from each other.

---

## Topic: broadcast.py

### What I Learned
I learned how to broadcast data from one root process to all other processes using MPI.

### How to Execute
```bash
mpiexec -n 4 python broadcast.py
```

### Use / Output
Process 0 creates a variable with value `100`. This value is then shared with all other processes.

Example output:
```text
process = 0 variable shared = 100
process = 1 variable shared = 100
process = 2 variable shared = 100
process = 3 variable shared = 100
```

### When to Use
Use broadcast when one process has data that all other processes need.

### Advantages
- Simple way to share data
- Efficient for one-to-many communication
- Useful for sharing configuration or starting values

### Disadvantages
- Only one root process sends the original data
- Not suitable when every process has different data to share
- Requires all processes to participate

### Summary
Broadcast sends the same data from one root process to all other MPI processes.

---

## Topic: deadLockProblems.py

### What I Learned
I learned how deadlock can happen in MPI when processes wait for each other incorrectly.

### How to Execute
```bash
mpiexec -n 6 python deadLockProblems.py
```

### Use / Output
Process 1 waits to receive data from process 5 before sending data. Process 5 sends data to process 1 and then waits to receive data from process 1.

Example output:
```text
my rank is 1
my rank is 5
sending data b to process 1
data received is = b
```

### When to Use
This example is useful for learning what deadlock is and why send/receive order matters.

### Advantages
- Helps understand MPI communication problems
- Shows why process coordination is important
- Useful for debugging parallel programs

### Disadvantages
- Can freeze the program if communication order is wrong
- Difficult to debug in large MPI programs
- Requires careful planning of send and receive operations

### Summary
Deadlock happens when processes wait for each other and no process can continue. MPI programs must be designed carefully to avoid this issue.

---

## Topic: gather.py

### What I Learned
I learned how to collect data from multiple MPI processes into one root process using `gather`.

### How to Execute
```bash
mpiexec -n 4 python gather.py
```

### Use / Output
Each process calculates the square of its rank plus one. The root process collects all values.

Example output:
```text
rank = 0 ...receiving data to other process
process 0 receiving 4 from process 1
process 0 receiving 9 from process 2
process 0 receiving 16 from process 3
```

### When to Use
Use gather when every process has a result and one root process needs to collect all results.

### Advantages
- Easy way to collect results
- Useful for parallel calculations
- Root process can process final data

### Disadvantages
- Root process can become overloaded
- Not ideal for very large data
- All processes must participate

### Summary
`gather` collects data from all processes and stores it in the root process.

---

## Topic: hello.py

### What I Learned
I learned how to create a basic MPI program and get the rank of each process.

### How to Execute
```bash
mpiexec -n 4 python hello.py
```

### Use / Output
Each MPI process prints a hello message with its process rank.

Example output:
```text
hello world from process 0
hello world from process 1
hello world from process 2
hello world from process 3
```

### When to Use
Use this as the first program to test whether MPI and `mpi4py` are working correctly.

### Advantages
- Simple MPI starting point
- Helps understand process rank
- Useful for testing MPI setup

### Disadvantages
- Does not perform real computation
- Only demonstrates basic MPI execution
- Output order may be different each time

### Summary
This program introduces MPI process ranks and confirms that multiple processes are running.

---

## Topic: pointToPointCommunication.py

### What I Learned
I learned how point-to-point communication works in MPI using `send()` and `recv()`.

### How to Execute
```bash
mpiexec -n 9 python pointToPointCommunication.py
```

### Use / Output
Process 0 sends data to process 4. Process 1 sends data to process 8. Processes 4 and 8 receive and print the data.

Example output:
```text
my rank is : 0
sending data 10000000 to process 4
my rank is : 4
data received is = 10000000
my rank is : 1
sending data hello to process 8
my rank is : 8
data1 received is = hello
```

### When to Use
Use point-to-point communication when one specific process needs to send data to another specific process.

### Advantages
- Direct communication between two processes
- Useful for targeted data transfer
- Gives control over sender and receiver

### Disadvantages
- Can cause deadlock if send/receive order is wrong
- Hard to manage with many processes
- Requires correct process ranks

### Summary
Point-to-point communication allows one process to send data directly to another process.

---

## Topic: reduction.py

### What I Learned
I learned how to use `Reduce` in MPI to combine data from multiple processes into one result.

### How to Execute
```bash
mpiexec -n 4 python reduction.py
```

### Use / Output
Each process creates an array. The `Reduce` function adds arrays from all processes and stores the final result in the root process.

Example output:
```text
process 0 sending [0 1 2 3 4 5 6 7 8 9]
process 1 sending [0 2 4 6 8 10 12 14 16 18]
on task 0 after Reduce: data = [...]
```

### When to Use
Use reduction when results from many processes need to be combined into one result, such as sum, maximum, or minimum.

### Advantages
- Useful for combining distributed results
- Supports operations like sum, max, and min
- Efficient for parallel calculations

### Disadvantages
- Final result is only available at root process
- Requires compatible data types
- Can be confusing for beginners

### Summary
`Reduce` combines values from all MPI processes into one final result using an operation such as sum.

---

## Topic: scatter.py

### What I Learned
I learned how to use `scatter` to divide data from one root process and send one part to each process.

### How to Execute
```bash
mpiexec -n 10 python scatter.py
```

### Use / Output
Process 0 creates a list of 10 values. Each process receives one value from the list.

Example output:
```text
process = 0 variable shared = 1
process = 1 variable shared = 2
process = 2 variable shared = 3
process = 3 variable shared = 4
```

### When to Use
Use scatter when one process has a collection of data and each process needs a separate part of that data.

### Advantages
- Divides work between processes
- Useful for parallel processing
- Reduces manual data distribution

### Disadvantages
- Number of data items should match the number of processes
- Root process must prepare the data
- Not suitable if all processes need the full data

### Summary
`scatter` distributes different pieces of data from the root process to all MPI processes.

---

## Topic: virtualTopology.py

### What I Learned
I learned how to create a virtual Cartesian topology in MPI and find neighboring processes.

### How to Execute
```bash
mpiexec -n 4 python virtualTopology.py
```

### Use / Output
The program creates a grid topology and assigns each process a row and column. It also finds the neighboring processes in the up, down, left, and right directions.

Example output:
```text
Building a 2 x 2 grid topology:
Process = 0
row = 0
column = 0
neighbour_processes[UP] = ...
neighbour_processes[DOWN] = ...
neighbour_processes[LEFT] = ...
neighbour_processes[RIGHT] = ...
```

### When to Use
Use virtual topology when processes need to be arranged logically in a grid or network structure.

### Advantages
- Helps organize processes in a structured way
- Useful for grid-based computations
- Makes neighbor communication easier

### Disadvantages
- More advanced MPI concept
- Requires understanding of Cartesian grids
- Can be confusing with process reordering

### Summary
Virtual topology allows MPI processes to be arranged in a logical grid and makes it easier to find neighboring processes.

---

# Chapter 4 Summary

In this chapter, I learned about MPI-based parallel programming using the `mpi4py` library. MPI allows multiple processes to communicate with each other while running in parallel.

This chapter covered basic MPI concepts such as process rank, communicator, point-to-point communication, collective communication, broadcasting, scattering, gathering, reduction, all-to-all communication, deadlock problems, and virtual topology.

## Main Concepts Covered

- MPI communicator
- Process rank
- Process size
- Point-to-point communication
- Send and receive
- Broadcast
- Scatter
- Gather
- Reduce
- All-to-all communication
- Deadlock problems
- Virtual Cartesian topology

## Overall Advantages

- Supports parallel programming
- Works well for distributed systems
- Allows processes to communicate efficiently
- Useful for scientific and high-performance computing
- Can run on multiple cores or multiple machines

## Overall Disadvantages

- More difficult than normal Python programs
- Requires MPI setup and installation
- Must be executed with `mpiexec` or `mpirun`
- Communication mistakes can cause deadlocks
- Debugging is harder because many processes run together

## Final Summary

Chapter 4 explains how Python can use MPI through the `mpi4py` library for parallel and distributed computing. MPI is powerful because it allows processes to communicate using send/receive and collective operations like broadcast, scatter, gather, reduce, and all-to-all. However, MPI programs require careful process coordination to avoid problems like deadlocks.
