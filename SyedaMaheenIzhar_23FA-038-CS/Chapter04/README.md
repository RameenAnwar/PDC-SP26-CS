# Chapter 04: MPI Programming in Python

## 1. All-to-All Communication (alltoall.py)
### What I learned

This program demonstrates all-to-all communication, where every process exchanges data with all other processes.

### How to run
mpiexec -n 4 python alltoall.py
### Purpose

Used in distributed systems where complete inter-process data exchange is required.

### Overview

Implements full communication between all processes using MPI.

### Benefits
Efficient parallel data exchange
Useful for distributed algorithms
### Limitations
High communication overhead

## 2. Broadcasting Data (broadcast.py)
### What I learned

This program shows how one process sends the same data to all other processes using broadcast.

### How to run
mpiexec -n 4 python broadcast.py
### Purpose

Used when a single process needs to share data with all processes.

### Overview

Demonstrates MPI broadcast operation.

### Benefits
Fast data distribution
Simple communication model
### Limitations
Only one root process controls data

## 3. Deadlock Problems (deadLockProblems.py)
### What I learned

This program demonstrates how improper send/receive order can lead to deadlocks in MPI.

### How to run
mpiexec -n 6 python deadLockProblems.py
### Purpose

Used to understand synchronization issues in parallel communication.

### Overview

Shows how incorrect communication design can freeze processes.

### Benefits
Helps understand safe communication design
### Limitations
Wrong ordering can block execution

## 4. Gathering Data (gather.py)
### What I learned

This program demonstrates collecting data from all processes into a single root process.

### How to run
mpiexec -n 4 python gather.py
### Purpose

Used to combine distributed results into one process.

### Overview

Implements MPI gather operation.

### Benefits
Centralized result collection
Useful in parallel computations
### Limitations
Root process may become overloaded

## 5. Hello World MPI (helloWorld_MPI.py)
### What I learned

Each process prints its unique rank using MPI initialization.

### How to run
mpiexec -n 4 python helloWorld_MPI.py
### Purpose

Introductory MPI program for beginners.

### Overview

Shows process rank and initialization.

### Benefits
Simple and beginner-friendly
### Limitations
No communication between processes

## 6. Point-to-Point Communication (pointToPointCommunication.py)
### What I learned

This program demonstrates direct communication between processes using send() and recv().

### How to run
mpiexec -n 9 python pointToPointCommunication.py
### Purpose

Used for direct message passing between specific processes.

### Overview

Implements MPI point-to-point communication.

### Benefits
Simple and precise communication
### Limitations
Difficult to scale in large systems

## 7. Reduction Operation (reduction.py)
### What I learned

This program demonstrates combining values from all processes into a single result using reduction operations like SUM.

### How to run
mpiexec -n 4 python reduction.py
### Purpose

Used for aggregating distributed computation results.

### Overview

Shows MPI reduce operation.

### Benefits
Efficient data aggregation
Useful in scientific computing
### Limitations
Depends on root process

## 8. Scatter Operation (scatter.py)
### What I learned

This program demonstrates distributing data from one process to multiple processes.

### How to run
mpiexec -n 4 python scatter.py
### Purpose

Used to divide workloads across processes.

### Overview

Implements MPI scatter operation.

### Benefits
Efficient parallel workload distribution
### Limitations
Requires properly structured input data

## 9. Virtual Topology (virtualTopology.py)
### What I learned

This program demonstrates arranging processes in a grid (Cartesian topology) for structured communication.

### How to run
mpiexec -n 4 python virtualTopology.py
### Purpose

Used in simulations and grid-based parallel systems.

### Overview

Defines virtual process layout and neighbor relationships.

### Benefits
Structured communication model
Useful for scientific simulations
### Limitations
Complex for beginners