# Chapter 4 – MPI Concepts with GCD & LCM

## Overview

This project demonstrates various Message Passing Interface (MPI) concepts using Python and the **mpi4py** library. The implementation uses **Greatest Common Divisor (GCD)** and **Least Common Multiple (LCM)** computations as practical examples to explore parallel and distributed computing techniques.

Each MPI concept is applied to the same GCD/LCM problem to understand communication, synchronization, reduction operations, and process topologies in a distributed environment.

---

## Concepts Implemented

### 1. Hello World MPI

* Basic MPI program execution.
* Demonstrates MPI initialization and rank identification.
* Each process prints its rank information.

### 2. Point-to-Point Communication

* Uses `comm.send()` and `comm.recv()`.
* One process computes an LCM value and sends it directly to another process.
* Demonstrates direct communication between ranks.

### 3. Broadcast

* Uses `comm.bcast()`.
* Root process broadcasts an LCM value to all participating ranks.
* Ensures all processes receive identical data.

### 4. Scatter

* Uses `comm.scatter()`.
* Root process distributes different pairs of numbers among ranks.
* Each process computes the LCM for its assigned data.

### 5. Gather

* Uses `comm.gather()`.
* Each rank computes an LCM and sends the result to the root process.
* Root collects and displays all computed values.

### 6. All-to-All Communication

* Uses `comm.alltoall()`.
* Every process exchanges data with every other process.
* Demonstrates many-to-many communication patterns.

### 7. Reduction

* Uses `comm.reduce()`.
* Aggregates LCM results from all processes.
* Example operations include sum, maximum, and minimum.

### 8. Deadlock Example

* Demonstrates improper communication ordering.
* Shows how deadlocks occur in distributed systems.
* Highlights safe communication practices.

### 9. Virtual Topology (Cartesian)

* Uses `comm.Create_cart()`.
* Creates a virtual Cartesian process grid.
* Processes communicate based on coordinates within the topology.

---

## Project Structure

| File Name               | Description                  |
| ----------------------- | ---------------------------- |
| helloworld_mpi.py       | Hello World MPI              |
| pointtopoint_mpi.py     | Point-to-Point Communication |
| broadcast_mpi.py        | Broadcast Communication      |
| scatter_mpi.py          | Scatter Operation            |
| gather_mpi.py           | Gather Operation             |
| alltoall_mpi.py         | All-to-All Communication     |
| reduction_mpi.py        | Reduction Operation          |
| deadlock_mpi.py         | Deadlock Demonstration       |
| virtual_topology_mpi.py | Cartesian Virtual Topology   |

---

## Requirements

### Software

* Python 3.8+
* MPI Implementation (OpenMPI or MPICH)
* mpi4py

### Installation

```bash
pip install mpi4py
```

Verify MPI installation:

```bash
mpiexec --version
```

---

## Running the Programs

Run any MPI program using:

```bash
mpiexec -n 4 python filename.py
```

Example:

```bash
mpiexec -n 4 python scatter_mpi.py
```

or

```bash
mpiexec -n 4 python reduction_mpi.py
```

---

## Execution Time Measurement

Each MPI program records execution time using Python's `time` module.

```python
start = time.time()

# GCD / LCM computation

end = time.time()

print("Execution Time:", end - start)
```

This allows performance comparison across different MPI communication techniques.

---

## Example Output

```text
Rank 0 computed LCM 36, Time 0.0000012 sec
Rank 1 computed LCM 36, Time 0.0000011 sec
Rank 2 computed LCM 36, Time 0.0000013 sec
Rank 3 computed LCM 36, Time 0.0000012 sec
```

---

## Learning Objectives

After completing this chapter, you will be able to:

* Understand MPI initialization and execution.
* Work with ranks, communicators, and process groups.
* Implement point-to-point communication using send/receive.
* Use collective communication operations such as Broadcast, Scatter, Gather, and All-to-All.
* Perform reduction operations for distributed aggregation.
* Identify and avoid communication deadlocks.
* Create virtual Cartesian topologies.
* Measure and analyze execution time in distributed systems.

---

## Performance Analysis

This project enables comparison between:

* Point-to-Point vs Collective Communication
* Scatter/Gather vs Broadcast
* Reduction vs Manual Aggregation
* Structured Topology vs Standard Communication

These comparisons help understand the efficiency of distributed computing models.

---

## Future Enhancements

* Distributed GCD/LCM computation across multiple machines.
* Hybrid MPI + Multithreading implementation.
* Performance benchmarking on clusters.
* Dynamic load balancing among MPI ranks.
* Fault-tolerant distributed computing models.
* Large-scale numerical processing using MPI.

---

## Author

Huzaifa Alim

Computer Science Student
Usman Institute of Technology (UIT)

