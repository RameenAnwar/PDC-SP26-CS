# Chapter 04 – Message Passing (MPI)

---

# 1. Message Passing Interface (MPI)

## Definition

- MPI (Message Passing Interface) is a standardized and portable communication system used in parallel programming.
- It allows multiple processes to communicate by sending and receiving messages in distributed memory systems.

---

## Key Idea

- Each process has its own private memory
- No shared memory exists between processes
- Communication happens only through messages

---

## Example

- Process A sends data → Process B receives data
- Process B processes data → sends result to Process C

---

## Goals of MPI

- Efficiency → reduces communication overhead
- Flexibility → works on different architectures
- Portability → same program runs on different systems

---

# 2. MPI Programming Model

## Distributed Memory Model

- Each process has separate memory
- Data sharing only through message passing
- Used in clusters and supercomputers

---

## Hybrid Memory Model

- Combination of shared memory + distributed memory
- Used in modern HPC systems

---

## SPMD Model

- Single Program Multiple Data
- Same program runs on all processes
- Different behavior based on rank

### Example

- Rank 0 → Input handling
- Rank 1 → Computation
- Rank 2 → Output handling

---

# 3. Core MPI Concepts

## Process

- Independent execution unit in MPI

## Rank

- Unique ID of each process
- Starts from 0 to n-1

## Communicator

- Group of processes that can communicate
- Default communicator: MPI_COMM_WORLD

---

# 4. Types of Communication in MPI

---

# 4.1 Point-to-Point Communication

## Definition

- Communication between exactly two processes (sender and receiver)

## Functions

- Send → sends data to another process
- Receive → receives data from another process

## Example

- P0 sends data to P1
- P1 receives and processes it

---

## Advantages

- Simple communication
- Full control over sender and receiver

---

## Disadvantages

- Not scalable for large systems
- Manual management required

---

# 4.2 Collective Communication

## Definition

- Communication involving multiple processes in a group

---

## Advantages

- Faster than multiple point-to-point calls
- Easy synchronization
- Optimized by MPI library

---

## Disadvantages

- Less control over individual communication
- Can cause synchronization delays

---

# 5. Collective Operations

---

## 5.1 Broadcast (Bcast)

### Definition

- One process sends the same data to all processes

### Example

- Root sends value 10 → all processes receive 10

### Key Point

- One-to-all communication

---

## 5.2 Scatter

### Definition

- Root divides data into parts and sends different parts to processes

### Example

- [10,20,30,40]
  - P0 → 10
  - P1 → 20
  - P2 → 30
  - P3 → 40

---

## 5.3 Gather

### Definition

- All processes send data to root process

### Example

- P0=10, P1=20, P2=30 → Root collects [10,20,30]

---

## 5.4 Reduce

### Definition

- Combines data from all processes using an operation

### Example (SUM)

- P0=1, P1=2, P2=3 → Result = 6

### Operations

- SUM
- MAX
- MIN
- PRODUCT

---

## 5.5 Alltoall

### Definition

- Every process sends data to all other processes

### Example

- P0 sends to P1,P2
- P1 sends to P0,P2
- P2 sends to P0,P1

---

## 5.6 Barrier

### Definition

- Synchronization point where all processes wait

### Example

- No process moves forward until all reach barrier

---

# 6. Comparison Table

| Communication Type | Processes Involved | Data Type       | Example          |
| ------------------ | ------------------ | --------------- | ---------------- |
| Point-to-Point     | 2 processes        | Single message  | Send/Recv        |
| Broadcast          | 1 → All            | Same data       | Root → All       |
| Scatter            | 1 → Many           | Different parts | Array split      |
| Gather             | Many → 1           | Collected data  | Merge results    |
| Reduce             | Many → 1           | Computed result | Sum/Max          |
| Alltoall           | All → All          | Full exchange   | Matrix transpose |

---

# 7. Execution Flow of MPI

- Program starts on all processes
- Each process gets a rank
- Data is distributed
- Computation is performed
- Results are collected

---

# 8. Topologies in MPI

## Cartesian Topology

- Grid structure
- Used in simulations (physics, weather)

## Graph Topology

- Custom structure
- Defined using adjacency matrix

---

## Common Structures

- Ring → circular connection
- Mesh → grid structure
- Torus → wrap-around mesh

---

# 9. Strengths of MPI

## Advantages

- Standardized across HPC systems
- Highly portable
- High performance
- Scalable for large systems
- Supports many communication models

---

# 10. Limitations of MPI

## Disadvantages

- Complex programming model
- Debugging is difficult
- Requires manual communication handling
- Not suitable for small applications
- High learning curve

---

# 11. Important MPI Functions

## Initialization

- MPI_Init → start MPI
- MPI_Finalize → end MPI

---

## Point-to-Point

- MPI_Send → send data
- MPI_Recv → receive data

---

## Collective

- MPI_Bcast → broadcast
- MPI_Scatter → distribute data
- MPI_Gather → collect data
- MPI_Reduce → combine data

---

## Process Info

- MPI_Comm_size → number of processes
- MPI_Comm_rank → process ID

---

## Synchronization

- MPI_Barrier → synchronization point

---

# 12. Key Exam Comparisons

## Point-to-Point vs Collective

- Point-to-Point → 2 processes, manual control
- Collective → multiple processes, optimized communication

---

## Scatter vs Gather

- Scatter → one-to-many (split data)
- Gather → many-to-one (collect data)

---

## Broadcast vs Reduce

- Broadcast → send same data to all
- Reduce → combine data into one result

---

# 13. Summary

- MPI is used in distributed memory systems
- Communication happens via messages only
- Two main types: Point-to-Point and Collective
- Rank identifies each process
- SPMD is the most common model
- Collective operations simplify parallel processing
