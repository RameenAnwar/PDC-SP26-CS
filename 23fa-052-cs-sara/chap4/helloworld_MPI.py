# Simple hello world program using MPI
from mpi4py import MPI

# Get the communicator (lets processes talk to each other)
comm = MPI.COMM_WORLD

# Get this process's ID number (0, 1, 2, ...)
rank = comm.Get_rank()

# Each process prints its own "hello world" message
print("hello world from process ", rank)
#output
# hello world from process  1
# hello world from process  0
# hello world from process  4
# hello world from process  2
# hello world from process  3
