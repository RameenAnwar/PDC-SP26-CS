# 📂 Chapter 4: MPI & Distributed Parallelism in Python

This chapter covers **Message Passing Interface (MPI)** using `mpi4py` for distributed computing, including communication patterns such as broadcast, scatter, gather, reduce, and process topology.

---

## 🔹 1. All-to-All Communication
📄 File: `Chapter-4/all_to_all.py`

**Concepts Covered:**
- MPI.Alltoall
- Data exchange between all processes
- Parallel communication

---

## 🔹 2. Broadcast Communication
📄 File: `Chapter-4/broadcast.py`

**Concepts Covered:**
- MPI.bcast
- One-to-all communication
- Shared variable distribution

---

## 🔹 3. Point-to-Point Communication
📄 File: `Chapter-4/send_receive.py`

**Concepts Covered:**
- MPI.send / MPI.recv
- Process-to-process communication
- Data exchange between specific ranks

---

## 🔹 4. Gather Operation
📄 File: `Chapter-4/gather.py`

**Concepts Covered:**
- MPI.gather
- Collecting data to root process
- Aggregation of results

---

## 🔹 5. Hello World with MPI
📄 File: `Chapter-4/hello_mpi.py`

**Concepts Covered:**
- MPI basics
- Process rank identification
- Distributed execution

---

## 🔹 6. Multiple Send/Receive Example
📄 File: `Chapter-4/multi_send_receive.py`

**Concepts Covered:**
- Multiple process communication
- Sending different data types
- Controlled message passing

---

## 🔹 7. Reduce Operation
📄 File: `Chapter-4/reduce.py`

**Concepts Covered:**
- MPI.Reduce
- Aggregation operations (SUM)
- Parallel data reduction

---

## 🔹 8. Scatter Operation
📄 File: `Chapter-4/scatter.py`

**Concepts Covered:**
- MPI.scatter
- Data distribution among processes
- Parallel workload division

---

## 🔹 9. Cartesian Topology
📄 File: `Chapter-4/cartesian_topology.py`

**Concepts Covered:**
- MPI Cartesian communicator
- Grid-based process layout
- Neighbor communication
