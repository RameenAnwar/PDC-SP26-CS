# Chapter 4: Parallel Programming with MPI (Message Passing Interface)

This chapter contains Python examples demonstrating various communication patterns and concepts in parallel programming using the **mpi4py** library. These programs show how multiple processes can communicate and coordinate with each other.

## Prerequisites

- **mpi4py**: Python bindings for MPI
- **NumPy**: For numerical operations
- **MPI Installation**: An MPI implementation (OpenMPI or MPICH)

Install required packages:
```bash
pip install mpi4py numpy
```

## File Overview

### 1. **helloworld_MPI.py**
**Purpose:** Basic introduction to MPI programming

**What it does:**
- Initializes an MPI communicator to get access to all processes
- Retrieves the rank (unique ID) of each process
- Each process prints a "hello world" message with its rank

**Code Flow:**
```
Process 0: hello world from process 0
Process 1: hello world from process 1
Process 2: hello world from process 2
... (continues for all processes)
```

**Expected Output:**
```
hello world from process 0
hello world from process 1
hello world from process 2
...
```

**Key Concepts:**
- `MPI.COMM_WORLD`: Global communicator containing all processes
- `Get_rank()`: Returns unique identifier for the current process

---

### 2. **pointToPointCommunication.py**
**Purpose:** Demonstrates direct process-to-process communication (send/receive)

**What it does:**
- Process 0 sends an integer (10000000) to process 4
- Process 1 sends a string ("hello") to process 8
- Process 4 receives data from process 0
- Process 8 receives data from process 1
- All processes display their rank

**Code Flow:**
```
Process 0: Sends 10000000 to process 4
Process 1: Sends "hello" to process 8
Process 4: Receives data from process 0
Process 8: Receives data from process 1
```

**Expected Output (with 9+ processes):**
```
my rank is: 0
sending data 10000000 to process 4
my rank is: 1
sending data hello: to process 8
my rank is: 4
data received is = 10000000
my rank is: 8
data1 received is = hello
... (other processes print their rank)
```

**Key Concepts:**
- `send(data, dest=process_rank)`: Sends data to a specific process
- `recv(source=process_rank)`: Receives data from a specific process
- Point-to-point communication is the foundation of MPI

---

### 3. **broadcast.py**
**Purpose:** Broadcasts data from one process to all other processes

**What it does:**
- Process 0 initializes a variable with value 100
- All other processes initialize it as None
- Process 0 broadcasts the variable to all processes
- All processes receive and print the broadcasted value

**Code Flow:**
```
Process 0: Broadcasts variable_to_share = 100
All Processes: Receive variable_to_share = 100
```

**Expected Output:**
```
process = 0 variable shared = 100
process = 1 variable shared = 100
process = 2 variable shared = 100
...
```

**Key Concepts:**
- `bcast(data, root=0)`: One-to-all communication
- All processes receive the same data from the root process
- Efficient collective communication pattern

---

### 4. **scatter.py**
**Purpose:** Distributes different parts of an array to different processes

**What it does:**
- Process 0 creates an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Process 0 scatters the array elements one-to-one with each process
- Each process receives a single element
- Each process prints the element it received

**Code Flow:**
```
Process 0: Scatters [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Process 0: Receives element 1
Process 1: Receives element 2
Process 2: Receives element 3
... (continues for all processes)
```

**Expected Output:**
```
process = 0 variable shared = 1
process = 1 variable shared = 2
process = 2 variable shared = 3
...
process = 9 variable shared = 10
```

**Key Concepts:**
- `scatter(data, root=0)`: One-to-all communication (each process gets different data)
- Useful for distributing workload across processes
- Data must be divided into chunks equal to number of processes

---

### 5. **gather.py**
**Purpose:** Collects data from all processes to a single process (root)

**What it does:**
- Each process calculates (rank+1)² 
- All processes send their calculated value to process 0
- Process 0 gathers all results and prints them with their source process

**Code Flow:**
```
Process 0: Computes (0+1)² = 1, sends to process 0
Process 1: Computes (1+1)² = 4, sends to process 0
Process 2: Computes (2+1)² = 9, sends to process 0
...
Process 0: Receives and displays all results
```

**Expected Output (with 5 processes):**
```
rank = 0 ...receiving data to other process
process 0 receiving 4 from process 1
process 0 receiving 9 from process 2
process 0 receiving 16 from process 3
process 0 receiving 25 from process 4
```

**Key Concepts:**
- `gather(data, root=0)`: All-to-one communication
- Process 0 is the root that collects all data
- Inverse of scatter operation

---

### 6. **alltoall.py**
**Purpose:** Demonstrates all-to-all communication (each process sends to all others)

**What it does:**
- Each process creates send data as: (rank+1) × [0, 1, 2, ..., size-1]
- Each process performs an Alltoall operation
- Every process sends different data to every other process
- Each process receives data from all other processes

**Code Flow:**
```
Process 0: Sends [0, 0, 0, ...] to all, Receives contributions from all
Process 1: Sends [1, 2, 3, ...] to all, Receives contributions from all
Process 2: Sends [2, 4, 6, ...] to all, Receives contributions from all
...
```

**Expected Output (with 3 processes):**
```
process 0 sending [0 0 0] receiving [0 1 2]
process 1 sending [1 2 3] receiving [0 2 4]
process 2 sending [2 4 6] receiving [0 2 6]
```

**Key Concepts:**
- `Alltoall(senddata, recvdata)`: All processes exchange data with each other
- Complex communication pattern
- Useful for matrix transposition and similar operations

---

### 7. **reduction.py**
**Purpose:** Combines data from all processes using a reduction operation (sum)

**What it does:**
- Each process creates an array: (rank+1) × [0, 1, 2, ..., 9]
- All processes perform a Reduce operation with SUM
- Process 0 accumulates the sum of all arrays
- Each process displays its send data and the accumulated result

**Code Flow:**
```
Process 0: Sends [0, 0, 0, ...] to process 0
Process 1: Sends [1, 2, 3, ...] to process 0
Process 2: Sends [2, 4, 6, ...] to process 0
...
Process 0: Calculates sum = [0+1+2+..., 0+2+4+..., ...]
```

**Expected Output (with 3 processes):**
```
process 0 sending [0 0 0 0 0 0 0 0 0 0]
on task 0 after Reduce: data = [3 6 9 12 15 18 21 24 27 30]
process 1 sending [1 2 3 4 5 6 7 8 9 10]
on task 1 after Reduce: data = [0 0 0 0 0 0 0 0 0 0]
process 2 sending [2 4 6 8 10 12 14 16 18 20]
on task 2 after Reduce: data = [0 0 0 0 0 0 0 0 0 0]
```

**Key Concepts:**
- `Reduce(senddata, recvdata, root=0, op=MPI.SUM)`: Reduces data with an operation
- Root process receives the combined result
- Other reduce operations: MAX, MIN, PROD, etc.

---

### 8. **deadLockProblems.py**
**Purpose:** Demonstrates a potential deadlock scenario in MPI communication

**What it does:**
- Only processes 1 and 5 participate in this example
- Process 1: Attempts to receive from process 5, then send to process 5
- Process 5: Attempts to send to process 1, then receive from process 1
- Shows how improper ordering of send/recv can cause deadlock

**Code Flow (Problematic):**
```
Process 1: Waits to receive from 5 (blocked)
Process 5: Tries to send to 1 (may fail to complete)
→ DEADLOCK: Both processes waiting
```

**Expected Output:**
```
my rank is 1
my rank is 5
my rank is 0
... (other processes print rank)
[Program may hang or timeout due to deadlock]
```

**Key Concepts:**
- **Deadlock**: Two or more processes are stuck waiting for each other
- Incorrect ordering of send/recv operations can cause deadlock
- Solution: Use non-blocking communication or reorder operations
- Example of synchronization issues in parallel programming

---

### 9. **virtualTopology.py**
**Purpose:** Creates a 2D Cartesian grid topology for organized process communication

**What it does:**
- Creates a 2D Cartesian (grid) topology from all available processes
- Calculates grid dimensions based on the number of processes
- Retrieves each process's coordinates in the grid
- Identifies neighbor processes (UP, DOWN, LEFT, RIGHT)
- Handles periodic boundaries (wrap-around)

**Code Flow:**
```
4 processes → 2×2 grid
Process 0: (0,0) → Neighbors: UP=2, DOWN=2, LEFT=2, RIGHT=1
Process 1: (0,1) → Neighbors: UP=3, DOWN=3, LEFT=0, RIGHT=0
Process 2: (1,0) → Neighbors: UP=0, DOWN=0, LEFT=3, RIGHT=3
Process 3: (1,1) → Neighbors: UP=1, DOWN=1, LEFT=2, RIGHT=2
```

**Expected Output (with 4 processes):**
```
Building a 2 x 2 grid topology:
Process = 0 row = 0 column = 0 --->
neighbour_processes[UP] = 2
neighbour_processes[DOWN] = 2
neighbour_processes[LEFT] = 2
neighbour_processes[RIGHT] = 1

Process = 1 row = 0 column = 1 --->
neighbour_processes[UP] = 3
neighbour_processes[DOWN] = 3
neighbour_processes[LEFT] = 0
neighbour_processes[RIGHT] = 0
... (continues for all processes)
```

**Key Concepts:**
- `Create_cart()`: Creates Cartesian (grid) topology
- `Get_coords()`: Returns grid coordinates for a process
- `Shift()`: Finds neighbor processes in a given direction
- `periods=(True, True)`: Enables periodic boundaries (wrapping)
- Useful for stencil-based computations and spatial domains

---

## How to Run

### Run with 4 processes:
```bash
mpirun -np 4 python helloworld_MPI.py
mpirun -np 4 python broadcast.py
mpirun -np 4 python scatter.py
mpirun -np 4 python gather.py
mpirun -np 4 python alltoall.py
mpirun -np 4 python reduction.py
mpirun -np 4 python virtualTopology.py
```

### Run with specific process count (for point-to-point and deadlock):
```bash
mpirun -np 9 python pointToPointCommunication.py
mpirun -np 6 python deadLockProblems.py
```

## Learning Outcomes

After studying these programs, you will understand:

1. **Basic MPI Operations**: Initialization and rank identification
2. **Point-to-Point Communication**: Direct process-to-process messaging
3. **Collective Communication**: Broadcast, scatter, gather operations
4. **All-to-All Communication**: Complex multi-process data exchange
5. **Reduction Operations**: Aggregating data across processes
6. **Deadlock Issues**: Synchronization problems and their causes
7. **Virtual Topologies**: Organizing processes in structured patterns
8. **Practical Applications**: When and how to use each communication pattern

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| "Rank mismatch" errors | Process trying to communicate with non-existent rank | Ensure process count matches expectations |
| Program hangs | Deadlock in communication | Check send/recv ordering; use non-blocking calls |
| "Import mpi4py failed" | mpi4py not installed | `pip install mpi4py` |
| Unexpected output order | Process scheduling variance | Expected behavior; output order may vary |

---

**Note:** These programs are educational examples from the Python Parallel Programming Cookbook. They demonstrate fundamental MPI concepts suitable for learning parallel programming patterns.
