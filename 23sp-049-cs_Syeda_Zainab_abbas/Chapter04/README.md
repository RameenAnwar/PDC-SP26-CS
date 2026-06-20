# 🌐 Chapter 04 — Message Passing (MPI with `mpi4py`)

> **Topic:** Distributed-memory parallelism using the Message Passing Interface

---

## 🎯 Overview
**MPI** is the standard for parallel programs that run across **many processes — even many machines**. Every process runs the *same* program but is given a unique **rank** (ID). Processes don't share memory at all; they cooperate purely by **passing messages**. `mpi4py` is the Python binding for MPI.

> 📝 **Why is the code here `#` commented with the output written in?**
> These programs are launched with **`mpiexec`**, not plain `python`, and need an MPI runtime installed. So in each file the code is preserved as comments and the **expected output is documented at the bottom** of the file.

---

## 🧠 Key Concepts

| Term | Meaning |
|------|---------|
| **Communicator** (`COMM_WORLD`) | The group of all participating processes. |
| **Rank** | A process's unique ID: `comm.Get_rank()`. |
| **Size** | Total number of processes: `comm.Get_size()`. |
| **Point-to-point** | One process `send`s, another `recv`s. |
| **Collective** | All processes participate together (broadcast, scatter, gather, reduce…). |
| **Deadlock** | Two processes wait on each other forever — avoided by careful send/recv ordering. |

### Collective operations at a glance
| Operation | Direction | Picture |
|-----------|-----------|---------|
| **Broadcast** | one → all | root copies one value to everyone |
| **Scatter** | one → all (split) | root hands each process **one slice** of a list |
| **Gather** | all → one | root **collects** a value from everyone |
| **Reduce** | all → one (combine) | combine values with an op (e.g. SUM) |
| **Alltoall** | all ↔ all | every process exchanges with every other |

---

## 📂 Files in this folder
| File | Concept | Run command |
|------|---------|-------------|
| `helloworld_MPI.py` | Ranks | `mpiexec -n 5 python helloworld_MPI.py` |
| `pointToPointCommunication.py` | `send` / `recv` | `mpiexec -n 9 python pointToPointCommunication.py` |
| `deadLockProblems.py` | Avoiding deadlock | `mpiexec -n 6 python deadLockProblems.py` |
| `broadcast.py` | `bcast` | `mpiexec -n 10 python broadcast.py` |
| `scatter.py` | `scatter` | `mpiexec -n 10 python scatter.py` |
| `gather.py` | `gather` | `mpiexec -n 5 python gather.py` |
| `reduction.py` | `Reduce` (SUM) | `mpiexec -n 3 python reduction.py` |
| `alltoall.py` | `Alltoall` | `mpiexec -n 4 python alltoall.py` |
| `virtualTopology.py` | Cartesian grid | `mpiexec -n 4 python virtualTopology.py` |

---

## 🛠️ Setup
```bash
pip install mpi4py numpy
```
Plus an MPI runtime:
- **Windows:** install **MS-MPI** (`msmpisetup.exe` + SDK), then use `mpiexec`.
- **Linux:** `sudo apt install openmpi-bin libopenmpi-dev`
- **macOS:** `brew install open-mpi`

> ⚠️ **Common fixes**
> - `reduction.py`: newer NumPy removed `numpy.int` → replace with plain `int`.
> - `-n` must be **≥** the highest rank a file uses (e.g. `pointToPointCommunication.py` needs rank 8 → `-n 9`).

---

## ✅ Summary
MPI scales beyond one machine. Same program, many ranks, **no shared memory** — only messages. Master the collective ops (broadcast / scatter / gather / reduce) and the deadlock trap, and you understand distributed-memory computing.
