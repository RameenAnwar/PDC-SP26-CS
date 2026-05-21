# Import MPI for parallel processing
from mpi4py import MPI
import numpy

# Create a communicator (allows processes to talk to each other)
comm = MPI.COMM_WORLD

# Get total number of processes running
size = comm.Get_size()

# Get this process's ID (0, 1, 2, ...)
rank = comm.Get_rank()

# Create data to send:
# (rank+1) multiplied by array [0,1,2,...,size-1]
# Example: if rank=0 and size=4 → [0,1,2,3]
# Example: if rank=1 and size=4 → [0,2,4,6]
senddata = (rank+1) * numpy.arange(size, dtype=int)

# Create empty array to store received data
recvdata = numpy.empty(size, dtype=int)

# All-to-all communication:
# Process 0 sends its 1st element to P0, 2nd to P1, 3rd to P2...
# Process 1 sends its 1st element to P0, 2nd to P1, 3rd to P2...
# Each process also receives data from all other processes
comm.Alltoall(senddata, recvdata)

# Print what this process sent and what it received
print(" process %s sending %s receiving %s" \
      %(rank, senddata, recvdata))
#output
#  process 2 sending [0 3 6] receiving [2 4 6]
#  process 0 sending [0 1 2] receiving [0 0 0]
#  process 1 sending [0 2 4] receiving [1 2 3]
