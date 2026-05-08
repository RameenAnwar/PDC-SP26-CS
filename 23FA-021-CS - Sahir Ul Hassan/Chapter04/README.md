# Chapter 04 - MPI Basics, Collective Communication, and Virtual Topologies

## What I learned overall

- MPI introduces a different parallel model from threads and processes because every process has its own rank and communicates explicitly.
- `COMM_WORLD`, `rank`, and `size` are the first ideas I need to understand before any MPI program makes sense.
- Point-to-point communication and collective communication solve different problems, and choosing the right one matters for correctness and simplicity.
- Communication order is very important in MPI; a small mismatch in send/receive behavior can cause a deadlock.

## Concepts from each file

### `helloworld_MPI.py`
This is the simplest MPI program in the chapter:

- Imports `MPI` from `mpi4py`.
- Uses `MPI.COMM_WORLD` to access all running processes.
- Gets the current process rank with `Get_rank()`.
- Prints a hello message from each process.

My takeaway: this file helped me understand that every MPI process runs the same script, but each one behaves differently because of its rank.

### `pointToPointCommunication.py`
This file shows direct communication between specific processes:

- Process `0` sends an integer to process `4`.
- Process `1` sends a string to process `8`.
- Process `4` receives from process `0`.
- Process `8` receives from process `1`.

My conclusion: point-to-point communication is very explicit, so it is useful when I know exactly which process should send and which process should receive.

### `broadcast.py`
This demonstrates broadcast communication:

- Rank `0` creates the shared value.
- Other ranks start with `None`.
- `comm.bcast(..., root=0)` sends the same value to every process.

My understanding: broadcast is a clean way to distribute one piece of information from a root process to all workers.

### `scatter.py`
This file demonstrates splitting data across processes:

- Rank `0` creates a list of values.
- `comm.scatter(..., root=0)` divides that list across the ranks.
- Each process receives one part of the original data.

Takeaway: scatter is useful when I want one process to prepare work and then hand out pieces of it to the rest of the group.

### `gather.py`
This shows the reverse of scatter:

- Each rank computes a value based on its rank.
- `comm.gather(..., root=0)` collects all values at the root.
- Rank `0` prints the values it received from the other processes.

My conclusion: gather is a natural fit when every process produces a partial result and the root process needs the full collection.

### `reduction.py`
This introduces reduction operations on arrays:

- Creates a NumPy array for sending data.
- Prepares a zero-filled receive buffer on the root.
- Uses `comm.Reduce(..., op=MPI.SUM)` to combine all process contributions.

My takeaway: reduction is powerful because it combines communication and computation, especially when I only need a final aggregated result.

### `alltoall.py`
This file demonstrates full exchange between all processes:

- Each rank creates a send array.
- `comm.Alltoall(senddata, recvdata)` exchanges data with every other rank.
- Each process receives a value from every other process.

My understanding: all-to-all communication is more general than broadcast or gather, but it is also heavier because everyone talks to everyone.

### `virtualTopology.py`
This is the most structural example in the chapter:

- Builds a 2D Cartesian grid using `Create_cart()`.
- Uses `Get_coords()` to find each process position.
- Uses `Shift()` to identify neighboring processes in the up, down, left, and right directions.
- Sets periodic boundaries so the grid wraps around.

My conclusion: virtual topologies are useful when processes should behave like they are arranged in a mesh or grid, such as in scientific simulations.

### `deadLockProblems.py`
This file shows a communication pattern that can deadlock:

- Rank `1` tries to receive before sending.
- Rank `5` also sends before receiving.
- Because both ranks depend on each other in the wrong order, the program can block.

My takeaway: MPI communication order matters a lot. Blocking `send` and `recv` calls must be planned carefully, otherwise the program can freeze waiting for a message that never arrives.

## Personal chapter conclusions

- I now understand MPI as a message-passing model where ranks cooperate without shared memory.
- Collectives like broadcast, scatter, gather, reduce, and all-to-all make communication patterns much easier to express.
- Topology-aware communication adds another layer of structure for grid-based problems.
- The deadlock example was especially useful because it showed that correctness in MPI depends on message order just as much as it depends on logic.

