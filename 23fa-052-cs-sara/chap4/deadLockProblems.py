# Import MPI for parallel processing
from mpi4py import MPI

# Get the communicator
comm = MPI.COMM_WORLD

# Get this process's ID
rank = comm.rank

# Print each process's rank (ID number)
print("my rank is %i" % (rank))

# PROCESS WITH RANK 1
if rank == 1:
    # Data to send to process 5
    data_send = "a"
    
    # Destination (where to send) = process 5
    destination_process = 5
    
    # Source (where to receive from) = process 5
    source_process = 5

    # FIRST: Try to receive data from process 5 (THIS WILL CAUSE DEADLOCK!)
    data_received = comm.recv(source=source_process)
    
    # SECOND: Send data to process 5
    comm.send(data_send, dest=destination_process)
    
    # Print what was sent and received
    print("sending data %s " % data_send + \
          "to process %d" % destination_process)
    print("data received is = %s" % data_received)

# PROCESS WITH RANK 5
if rank == 5:
    # Data to send to process 1
    data_send = "b"
    
    # Destination = process 1
    destination_process = 1
    
    # Source (where to receive from) = process 1
    source_process = 1

    # FIRST: Send data to process 1
    comm.send(data_send, dest=destination_process)
    
    # SECOND: Receive data from process 1
    data_received = comm.recv(source=source_process)
    
    # Print what was sent and received
    print("sending data %s :" % data_send + \
          "to process %d" % destination_process)
    print("data received is = %s" % data_received)
#output
# my rank is 1
# my rank is 0
# my rank is 2
# my rank is 4
# my rank is 3