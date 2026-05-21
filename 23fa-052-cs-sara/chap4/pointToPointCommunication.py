# Import MPI for parallel processing
from mpi4py import MPI

# Get the communicator
comm = MPI.COMM_WORLD

# Get this process's ID (0, 1, 2, ...)
rank = comm.rank

# Print my rank number
print("my rank is : ", rank)

# PROCESS WITH RANK 0
if rank == 0:
    # Data to send (a large number)
    data = 10000000
    
    # Send to process 4
    destination_process = 4
    
    # Send the data to process 4
    comm.send(data, dest=destination_process)
    
    # Print confirmation message
    print("sending data %s " % data + \
          "to process %d" % destination_process)

# PROCESS WITH RANK 1
if rank == 1:
    # Send to process 8
    destination_process = 8
    
    # Data to send (a string "hello")
    data = "hello"
    
    # Send the data to process 8
    comm.send(data, dest=destination_process)
    
    # Print confirmation message
    print("sending data %s :" % data + \
          "to process %d" % destination_process)

# PROCESS WITH RANK 4
if rank == 4:
    # Receive data from process 0
    data = comm.recv(source=0)
    
    # Print the received data
    print("data received is = %s" % data)

# PROCESS WITH RANK 8
if rank == 8:
    # Receive data from process 1
    data1 = comm.recv(source=1)
    
    # Print the received data
    print("data1 received is = %s" % data1)
#ouptut
# my rank is :  3
# my rank is :  0
# sending data 10000000 to process 4
# my rank is :  4
# data received is = 10000000
# my rank is :  1
# my rank is :  2