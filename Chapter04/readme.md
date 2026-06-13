# Chapter 04 — MPI / Message Passing Examples

This chapter contains small examples using `mpi4py` to demonstrate basic MPI communication patterns.

- `helloworld_MPI.py`:
  - Minimal MPI example printing the process rank; run with `mpiexec -n <N> python helloworld_MPI.py`.

- `pointToPointCommunication.py`:
  - Demonstrates `comm.send` and `comm.recv` for direct point-to-point messages between ranks.
  - Selected ranks send data to specific destination ranks and others perform corresponding receives.

- `deadLockProblems.py`:
  - Shows a simple deadlock scenario when two ranks perform blocking `send`/`recv` in the wrong order.
  - Useful to study why ordering and nonblocking operations or proper matching of sends/receives matters.

- `broadcast.py`:
  - Demonstrates `comm.bcast` to broadcast a variable from root (rank 0) to all processes.

- `scatter.py`:
  - Demonstrates `comm.scatter` where rank 0 distributes distinct list elements to each process (one item per rank).

- `gather.py`:
  - Demonstrates `comm.gather` where each rank computes a value and the root collects the list of values.

- `alltoall.py`:
  - Demonstrates `comm.Alltoall`, where each process sends a block of data to every other process and receives blocks in return.

- `reduction.py`:
  - Shows `comm.Reduce` with `MPI.SUM` to aggregate arrays across ranks into the root process.

- `virtualTopology.py`:
  - Uses `Create_cart` to build a 2D Cartesian communicator, computes neighbor ranks with `Shift`, and prints neighbor mapping.

How to run

- MPI examples require `mpi4py` and an MPI runtime. Example invocation:

```
mpiexec -n 4 python helloworld_MPI.py
```

Notes

- Replace `-n 4` with the desired number of processes; some examples reference specific ranks and need enough processes to avoid errors.
- Use nonblocking (`Isend`/`Irecv`) or proper ordering to avoid deadlocks in real applications.
