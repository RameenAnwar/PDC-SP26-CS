# 🚀 Python MPI Programming – Complete README

> A comprehensive guide covering Message Passing Interface (MPI) concepts using Python and mpi4py including process communication, collective operations, reduction methods, topology creation, and deadlock handling.

---

## 📑 Table of Contents

1. [Introduction](#1-introduction)
2. [Hello World MPI](#2-hello-world-mpi)
3. [Point-to-Point Communication](#3-point-to-point-communication)
4. [Broadcast Communication](#4-broadcast-communication)
5. [Scatter Communication](#5-scatter-communication)
6. [Gather Communication](#6-gather-communication)
7. [Reduction Operations](#7-reduction-operations)
8. [All-to-All Communication](#8-all-to-all-communication)
9. [Virtual Topology](#9-virtual-topology)
10. [Deadlock Problems](#10-deadlock-problems)
11. [Quick Reference](#11-quick-reference)
12. [Conclusion](#12-conclusion)

---

# 1. Introduction

Normally, a Python program executes tasks one after another:

Step 1 → Step 2 → Step 3

But large problems sometimes need multiple tasks to run at the same time.

That is where **MPI (Message Passing Interface)** comes in.

MPI allows multiple processes to run simultaneously and communicate with each other.

Python supports MPI through:

```python
from mpi4py import MPI
```

---

### Why use MPI?

- Faster execution
- Better CPU utilization
- Solve large computations
- Parallel processing
- Reduced execution time

---

### Important MPI Terms

| Term | Meaning |
|--------|----------|
| Process | Independent running program |
| Rank | Unique process ID |
| Size | Total processes |
| Communicator | Group of communicating processes |
| Root Process | Main controlling process |

---

### How MPI works

            MPI COMMUNICATOR
    ---------------------------------

       Process0
       Process1
       Process2
       Process3
```

Each process has:

- Its own memory
- Its own execution
- Its own rank

---

## Installation

Install mpi4py:

```bash
pip install mpi4py
```

Verify installation:

```bash
python -c "from mpi4py import MPI"
```

---

## Running Programs

General syntax:

```bash
mpiexec -n 4 python filename.py
```

Example:

```bash
mpiexec -n 4 python helloworld_MPI.py
```

---

# 2. Hello World MPI

**File:** `helloworld_MPI.py`

### What is Hello World MPI?

This is the first MPI program used to verify MPI installation and understand process creation.

---

### Functions Used

```python
MPI.COMM_WORLD

comm.Get_rank()

comm.Get_size()
```

---

### Concepts Covered

| Concept | Description |
|-----------|-------------|
| Rank | Process ID |
| Size | Total processes |
| Communicator | Process group |

---

### Example Output

```text
Hello from process 0
Hello from process 1
Hello from process 2
Hello from process 3
```

---

### Explanation

Each process receives its own rank and executes separately.

---

# 3. Point-to-Point Communication

**File:** `pointToPointCommunication.py`

### What is Point-to-Point Communication?

Communication between one sender and one receiver.

---

### Functions Used

comm.send()

comm.recv()

### Communication Flow

Process0 ---------> Process1

### How does it work?

| Step | Action |
|--------|---------|
| Step 1 | Sender creates message |
| Step 2 | Message is sent |
| Step 3 | Receiver waits |
| Step 4 | Receiver gets message |

---
---

### Example Output

Message Sent: Hello
Message Received: Hello
```

---

# 4. Broadcast Communication

**File:** `broadcast.py`

### What is Broadcast?

Broadcast sends identical information from one process to all processes.

---

### Function Used

```python
comm.bcast()
```

---

### Communication Flow

             Process0
            /   |   \
           /    |    \
          /     |     \
        P1      P2     P3
```

---

### Example Output

Process0 receives 100
Process1 receives 100
Process2 receives 100
Process3 receives 100
```

---



# 5. Scatter Communication

**File:** `scatter.py`

### What is Scatter?

Scatter divides information into smaller pieces and distributes them.

---

### Function Used

comm.scatter()
```

---

### Communication Flow

```text
        [10,20,30,40]

              |
      -----------------
      |   |   |   |
     P0  P1 P2 P3
```

---

### Example Output

```text
Process0 gets 10
Process1 gets 20
Process2 gets 30
Process3 gets 40
```

---

---

# 6. Gather Communication

**File:** `gather.py`

### What is Gather?

Gather collects information from all processes and sends it to one process.

---

### Function Used

comm.gather()


### Communication Flow

P0
 \
P1 -----> Root Process
 /
P2
 \
P3
```

---

### Example Output

Collected Data:

[10,20,30,40]
```

---


# 7. Reduction Operations

**File:** `reduction.py`

### What is Reduction?

Reduction combines values from multiple processes into one result.

---

### Function Used

```python
comm.reduce()
```

---

### Operations

| Operation | Purpose |
|------------|----------|
| MPI.SUM | Addition |
| MPI.MAX | Maximum |
| MPI.MIN | Minimum |
| MPI.PROD | Multiplication |

---

### Example

Input:
1 2 3 4

Output:
Total Sum=10


# 8. All-to-All Communication

**File:** `alltoall.py`

### What is All-to-All?

Each process exchanges information with every other process.


### Function Used

comm.alltoall()


### Communication Flow
P0 ↔ P1
↕    ↕
P2 ↔ P3

### Example
Each process sends and receives information

# 9. Virtual Topology

**File:** `virtualTopology.py`

### What is Virtual Topology?

Virtual topology creates logical arrangements among processes.

### Functions Used
Create_cart()

Get_coords()

Shift()


### Concepts Covered

| Concept | Description |
|-----------|-------------|
| Cartesian topology | Grid arrangement |
| Coordinates | Position of process |
| Neighbor communication | Communication with nearby process |

### Example
P0 P1
P2 P3

# 10. Deadlock Problems

**File:** `deadLockProblems.py`

### What is Deadlock?

Deadlock occurs when two or more processes wait forever for each other.


### Example
Process A waiting for Process B

Process B waiting for Process A


### Result
Program execution stops


### Causes of Deadlock

| Cause | Explanation |
|---------|-------------|
| Blocking send | Process waits |
| Blocking receive | Process waits |
| Circular waiting | Processes depend on each other |


### How to avoid deadlocks?

✔ Use proper send/receive order

✔ Use non-blocking communication

✔ Design communication carefully

---

# 11. Quick Reference

| File | Main Concept | Purpose |
|------|--------------|----------|
| helloworld_MPI.py | MPI basics | Basic process execution |
| pointToPointCommunication.py | Send/Receive | Process communication |
| broadcast.py | Broadcast | One-to-all communication |
| scatter.py | Scatter | Divide data |
| gather.py | Gather | Collect data |
| reduction.py | Reduce | Combine values |
| alltoall.py | All-to-All | Exchange data |
| virtualTopology.py | Topology | Organize processes |
| deadLockProblems.py | Deadlock | Avoid waiting |

### What you learned

| Topic | Understanding |
|---------|---------------|
| Hello World | Basic MPI execution |
| Point-to-Point | One-to-one communication |
| Broadcast | One-to-all communication |
| Scatter | Data distribution |
| Gather | Data collection |
| Reduction | Combine values |
| All-to-All | Exchange information |
| Topology | Process arrangement |
| Deadlock | Waiting problems |

> One-line summary: MPI allows multiple processes to communicate and work together efficiently in parallel computing applications.
