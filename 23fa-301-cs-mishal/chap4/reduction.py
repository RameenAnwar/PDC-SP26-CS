# Import numpy for array operations
import numpy
# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI 

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD 
# Get the total number of processes in the communicator
size = comm.size 
# Get the rank (ID) of the current process (0 to size-1)
rank = comm.rank

# Define the size of the array each process will work with
array_size = 10
# Create an array to receive the reduced data (will be filled at root process)
recvdata = numpy.zeros(array_size, dtype=numpy.int16)
# Create data to send: each element is (rank+1) multiplied by 0, 1, 2, ..., 9
# Example: rank 0: [0,1,2,3,4,5,6,7,8,9]
#          rank 1: [0,2,4,6,8,10,12,14,16,18]
#          rank 2: [0,3,6,9,12,15,18,21,24,27]
senddata = (rank + 1) * numpy.arange(array_size, dtype=numpy.int16)

# Each process prints what it is sending
print(" process %s sending %s " % (rank, senddata))

# Perform a Reduce operation:
# All processes send their 'senddata' arrays to the root process (rank 0)
# The root process combines all arrays element-wise using the SUM operation
# After reduction, root gets [sum of element 0, sum of element 1, ...] from all processes
# Non-root processes receive nothing (recvdata remains zeros)
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

# Each process prints its rank and recvdata after reduction
# For rank 0: recvdata contains the summed result
# For other ranks: recvdata is still all zeros
print('on task', rank, 'after Reduce:    data = ', recvdata)


# What this code does:
# Reduce Operation: All processes send their data to the root process, which combines them using a specified operation (MPI.SUM).

# Data pattern (with 3 processes, array_size=5):

# Process 0: [0, 1, 2, 3, 4]

# Process 1: [0, 2, 4, 6, 8]

# Process 2: [0, 3, 6, 9, 12]

# Sum reduction at root (rank 0):

#OUTPUT
#  process 4 sending [ 0  5 10 15 20 25 30 35 40 45] 
# on task 4 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
#  process 1 sending [ 0  2  4  6  8 10 12 14 16 18] 
# on task 1 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
#  process 3 sending [ 0  4  8 12 16 20 24 28 32 36] 
# on task 3 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
#  process 2 sending [ 0  3  6  9 12 15 18 21 24 27] 
# on task 2 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
#  process 0 sending [0 1 2 3 4 5 6 7 8 9] 
# on task 0 after Reduce:    data =  [  0  15  30  45  60  75  90 105 120 135]