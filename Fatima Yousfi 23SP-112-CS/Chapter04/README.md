# Chapter 04

This chapter contains MPI examples implemented with `mpi4py`. These scripts require both the `mpi4py` package and an MPI runtime such as MS-MPI or OpenMPI.

## `helloworld_MPI.py`

- Prints a hello message together with the process rank.
- Useful as a first MPI smoke test.

## `pointToPointCommunication.py`

- Demonstrates direct `send()` and `recv()` calls between selected ranks.
- The current script assumes enough ranks exist for process `4` and process `8`.

## `deadLockProblems.py`

- Illustrates a deadlock scenario using blocking MPI communication.
- Rank `1` waits to receive before it sends, while rank `5` also participates in the same communication pattern.

## `broadcast.py`

- Uses `comm.bcast()` to share a value from rank `0` with every other rank.

## `scatter.py`

- Uses `comm.scatter()` to distribute elements from a root-side list.
- The root process provides the shared list and every rank receives one piece.

## `gather.py`

- Uses `comm.gather()` to collect one computed value from each process at rank `0`.
- In this script each rank contributes `(rank + 1) ** 2`.

## `alltoall.py`

- Uses NumPy arrays with `comm.Alltoall()`.
- Every rank sends data to every other rank and receives a full result array back.

## `reduction.py`

- Uses `comm.Reduce(..., op=MPI.SUM)` to sum arrays across all ranks into the root process.

## `virtualTopology.py`

- Builds a Cartesian communicator with `Create_cart()`.
- Each rank prints its grid coordinates and its logical neighbors.

## How to run

Examples:

```bash
mpiexec -n 4 python helloworld_MPI.py
mpiexec -n 4 python broadcast.py
```

Some files require more than four ranks. For example, `pointToPointCommunication.py` references rank `8`, so it should be run with at least nine processes.
