# Chapter 04 : MPI Programming in Python

---

## 1. alltoall.py

### What I learned

This program demonstrates All-to-All communication using MPI. Each process sends data to every other process and receives data from them.

### How to execute

```bash
mpiexec -n 4 python alltoall.py
```

### End use

Used in distributed systems where every process exchanges data with all other processes.

### When and how to use

Used when all processes need simultaneous communication using comm.Alltoall().

### Summary

Demonstrates all-to-all communication in MPI.

### Advantages

* Efficient parallel communication
* Fast distributed data exchange

### Disadvantages

* High communication overhead

---

## 2. broadcast.py

### What I learned

This program demonstrates broadcasting data from one process to all other processes.

### How to execute

```bash
mpiexec -n 4 python broadcast.py
```

### End use

Used to share the same data with all processes.

### When and how to use

Used when one process needs to distribute information to every other process.

### Summary

Shows MPI broadcast communication.

### Advantages

* Fast data sharing
* Easy implementation

### Disadvantages

* Only one source process allowed

---

## 3. deadLockProblems.py

### What I learned

This program demonstrates communication between processes and explains deadlock situations caused by improper send and receive operations.

### How to execute

```bash
mpiexec -n 6 python deadLockProblems.py
```

### End use

Used for understanding synchronization and deadlock issues in MPI.

### When and how to use

Used when learning safe process communication.

### Summary

Demonstrates deadlock concepts in MPI.

### Advantages

* Helps understand process synchronization

### Disadvantages

* Incorrect communication order can freeze processes

---

## 4. gather.py

### What I learned

This program demonstrates gathering data from all processes into a single root process.

### How to execute

```bash
mpiexec -n 4 python gather.py
```

### End use

Used to collect results from multiple processes.

### When and how to use

Used when distributed tasks generate outputs that must be combined.

### Summary

Shows gather operation in MPI.

### Advantages

* Efficient result collection

### Disadvantages

* Root process may become overloaded

---

## 5. helloWorld_MPI.py

### What I learned

This is a basic MPI program where each process prints its process rank.

### How to execute

```bash
mpiexec -n 4 python helloWorld_MPI.py
```

### End use

Used as an introduction to MPI programming.

### When and how to use

Used for understanding MPI initialization and process identification.

### Summary

Basic Hello World MPI example.

### Advantages

* Easy for beginners

### Disadvantages

* No process communication

---

## 6. pointToPointCommunication.py

### What I learned

This program demonstrates point-to-point communication using send() and recv() between specific processes.

### How to execute

```bash
mpiexec -n 9 python pointToPointCommunication.py
```

### End use

Used for direct communication between processes.

### When and how to use

Used when one process sends data directly to another process.

### Summary

Demonstrates point-to-point communication in MPI.

### Advantages

* Simple communication model

### Disadvantages

* Hard to manage in large-scale systems

---

## 7. reduction.py

### What I learned

This program demonstrates reduction operations where data from all processes is combined using MPI operations such as SUM.

### How to execute

```bash
mpiexec -n 4 python reduction.py
```

### End use

Used in scientific and parallel computations.

### When and how to use

Used when processes need to combine their results into one final output.

### Summary

Shows reduction operations in MPI.

### Advantages

* Efficient result aggregation

### Disadvantages

* Dependent on root process

---

## 8. scatter.py

### What I learned

This program demonstrates scattering data from one process to multiple processes.

### How to execute

```bash
mpiexec -n 4 python scatter.py
```

### End use

Used to distribute workloads among multiple processes.

### When and how to use

Used when large datasets need to be divided for parallel processing.

### Summary

Demonstrates scatter communication in MPI.

### Advantages

* Efficient workload distribution

### Disadvantages

* Requires proper data division

---

## 9. virtualTopology.py

### What I learned

This program demonstrates virtual Cartesian topology in MPI where processes are arranged in a grid structure and neighbor processes are identified.

### How to execute

```bash
mpiexec -n 4 python virtualTopology.py
```

### End use

Used in parallel algorithms and simulations requiring structured communication.

### When and how to use

Used in grid-based systems and scientific simulations.

