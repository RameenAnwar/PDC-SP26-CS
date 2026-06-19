from mpi4py import MPI  # Imports the MPI library to allow multiple processes to communicate
import numpy  # Imports NumPy to handle mathematical arrays efficiently

comm = MPI.COMM_WORLD  # Defines the group containing all the processes running in this program
size = comm.Get_size()  # Gets the total number of processes participating in the communication
rank = comm.Get_rank()  # Assigns a unique ID number to each individual process (starting from 0)

# Generates a unique array of numbers for this process to send out
senddata = (rank+1)*numpy.arange(size,dtype=int) 

# Creates an empty "buffer" array to store the data that will be received
recvdata = numpy.empty(size,dtype=int) 



# Performs a many-to-many data swap where every process exchanges data with everyone else
comm.Alltoall(senddata,recvdata) 

# Prints the rank, what was sent, and what was received to show the final result
print(" process %s sending %s receiving %s"\
      %(rank , senddata , recvdata))