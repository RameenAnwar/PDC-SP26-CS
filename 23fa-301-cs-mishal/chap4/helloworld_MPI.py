#hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print ("hello world from process ", rank)

# What this code does:
# Parallel execution: When run with multiple processes (e.g., mpirun -np 4 python hello.py), each process runs the code independently

# Process identification: Each process gets a unique rank (0, 1, 2, 3, ...)

# Output: Each process prints a message identifying itself

#output
# hello world from process  1
# hello world from process  0
# hello world from process  4
# hello world from process  2
# hello world from process  3