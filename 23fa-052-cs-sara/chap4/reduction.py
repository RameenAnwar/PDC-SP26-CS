# Import numpy for arrays and MPI for parallel processing
import numpy
from mpi4py import MPI

# Get the communicator
comm = MPI.COMM_WORLD

# Get total number of processes and this process's rank
size = comm.size
rank = comm.rank

# Size of the array (10 elements)
array_size = 10

# Create empty array to store received data (all zeros)
recvdata = numpy.zeros(array_size, dtype=numpy.int)

# Create data to send:
# (rank+1) multiplied by [0,1,2,3,4,5,6,7,8,9]
# Example: rank0 → [0,1,2,3,4,5,6,7,8,9]
# Example: rank1 → [0,2,4,6,8,10,12,14,16,18]
# Example: rank2 → [0,3,6,9,12,15,18,21,24,27]
senddata = (rank+1) * numpy.arange(array_size, dtype=numpy.int)

# Print what each process is sending
print(" process %s sending %s " % (rank, senddata))

# REDUCE: Combine all processes' data using SUM operation
# All processes send their senddata to process 0 (root)
# Process 0 adds them all together element-wise
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

# Print result after reduction
print('on task', rank, 'after Reduce:    data = ', recvdata)

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