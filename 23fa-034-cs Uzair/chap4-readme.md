# Chapter 4 – MPI Programming in Python

## Student Information

**Name:** Uzair
**Roll Number:** 23FA-034-CS

---

## Overview

This chapter introduces MPI (Message Passing Interface) and demonstrates communication among distributed processes running in parallel.

---

## Hello World MPI (helloworld_MPI.py)

### Learning Outcome

Learned the basic structure of MPI programs.

### Execution

```bash
mpiexec -n 4 python helloworld_MPI.py
```

### Summary

Basic MPI example.

---

## Point-to-Point Communication (pointToPointCommunication.py)

### Learning Outcome

Learned direct communication between processes.

### Execution

```bash
mpiexec -n 4 python pointToPointCommunication.py
```

### Summary

Implements send and receive operations.

---

## Broadcast Communication (broadcast.py)

### Learning Outcome

Learned how one process sends data to all processes.

### Execution

```bash
mpiexec -n 4 python broadcast.py
```

### Summary

Demonstrates MPI broadcast operation.

---

## Scatter Communication (scatter.py)

### Learning Outcome

Learned data distribution among processes.

### Execution

```bash
mpiexec -n 4 python scatter.py
```

### Summary

Demonstrates workload distribution.

---

## Gather Communication (gather.py)

### Learning Outcome

Learned collection of distributed results.

### Execution

```bash
mpiexec -n 4 python gather.py
```

### Summary

Combines results from multiple processes.

---

## Reduction Operation (reduction.py)

### Learning Outcome

Learned aggregation operations in MPI.

### Execution

```bash
mpiexec -n 4 python reduction.py
```

### Summary

Demonstrates reduction functions.

---

## All-to-All Communication (alltoall.py)

### Learning Outcome

Learned data exchange among all processes.

### Execution

```bash
mpiexec -n 4 python alltoall.py
```

### Summary

Implements all-to-all communication.

---

## Virtual Topology (virtualTopology.py)

### Learning Outcome

Learned logical organization of MPI processes.

### Execution

```bash
mpiexec -n 4 python virtualTopology.py
```

### Summary

Demonstrates MPI topologies.

---

## Deadlock Problems (deadLockProblems.py)

### Learning Outcome

Learned causes and prevention of communication deadlocks.

### Execution

```bash
mpiexec -n 4 python deadLockProblems.py
```

### Summary

Illustrates deadlock situations.

---

## Final Summary

This chapter introduced distributed communication and coordination using MPI.

---

## Conclusion

Through this chapter, I learned how distributed systems exchange information efficiently using MPI communication primitives.
