import numpy  # Imports NumPy to handle data arrays efficiently
from mpi4py import MPI  # Imports the MPI library for parallel processing

comm = MPI.COMM_WORLD  # Sets up the group for all running processes to communicate
size = comm.size  # Stores the total number of processes in the group
rank = comm.rank  # Stores the unique ID number of the current process


array_size = 10  # Defines the length of the data arrays to be used
recvdata = numpy.zeros(array_size,dtype=numpy.int)  # Creates an array of zeros to hold the final result (on the root)
senddata = (rank+1)*numpy.arange(array_size,dtype=numpy.int)  # Each process creates its own unique array based on its rank

print(" process %s sending %s " %(rank , senddata))  # Displays what each process is contributing before the reduction



# The 'Reduce' command collects arrays from all processes and combines them into one
# 'root=0' means process 0 will store the final result
# 'op=MPI.SUM' means the values at each position in the arrays will be added together
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)

# Each process prints its 'recvdata' array to show the result (only root 0 will have the sum)
print ('on task',rank,'after Reduce:    data = ',recvdata)