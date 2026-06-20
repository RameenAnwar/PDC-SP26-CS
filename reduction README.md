MPI Reduce Example:
A minimal Python script demonstrating the `Reduce` collective communication operation using the `mpi4py` and `numpy` libraries.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python packages:

```bash
pip install numpy mpi4py

```

How to Run:
Launch the script using an MPI executor. To run with 3 processes, use the following command in your terminal:

```bash
mpiexec -n 3 python script_name.py
```

What it Does:
This script demonstrates an element-wise array reduction, where data from all processes is combined into a single result on the root process:

1. Initialization: Every process creates an empty receiving array (`recvdata`) of size 10, filled with zeros.
2. Local Computation: Each process creates a sending array (`senddata`) of size 10. The values are a sequence from 0 to 9, multiplied by `(rank + 1)`.
3. The Reduce Operation: `comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)` performs an element-wise addition (`MPI.SUM`) of the `senddata` arrays across all processes.
4. The Result: The final summed array is saved into `recvdata` only on the root process (Process 0). For all other processes, `recvdata` remains unchanged (all zeros).

Example Output:
Running with 2 processes (`mpiexec -n 2 python script_name.py`) yields output similar to this:

```
 process 0 sending [0 1 2 3 4 5 6 7 8 9] 
 process 1 sending [ 0  2  4  6  8 10 12 14 16 18] 
on task 0 after Reduce:    data =  [ 0  3  6  9 12 15 18 21 24 27]
on task 1 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]

```
(Notice how the arrays from Process 0 and 1 are added together and stored in Process 0's `recvdata`, while Process 1's `recvdata` remains untouched).
