# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI
# Import numpy for array operations
import numpy

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the total number of processes in the communicator
size = comm.Get_size()
# Get the rank (ID) of the current process (0 to size-1)
rank = comm.Get_rank()

# Create data to send: each process sends an array where each element is 
# (rank+1) multiplied by 0, 1, 2, ..., size-1
# Example: rank 0 sends [0,0,0,...], rank 1 sends [0,1,2,...], etc.
senddata = (rank+1) * numpy.arange(size, dtype=int)
# Create an empty array to receive data from all processes
recvdata = numpy.empty(size, dtype=int)

# Perform an all-to-all collective communication:
# Each process sends its senddata to all processes, and receives data 
# from all processes. Process j receives the j-th element from every process.
comm.Alltoall(senddata, recvdata)

# Print the rank, what each process sent, and what it received
print(" process %s sending %s receiving %s" \
      % (rank, senddata, recvdata))

#What this code does:
# All-to-all communication: Each process sends a different piece of its data to every other process
# Data pattern: Process i sends value (i+1) * j to process j
# Result: After execution, process j receives an array where the i-th element is (i+1) * j



#output
#  process 2 sending [0 3 6] receiving [2 4 6]
#  process 0 sending [0 1 2] receiving [0 0 0]
#  process 1 sending [0 2 4] receiving [1 2 3]