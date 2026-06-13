# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the rank (ID) of the current process (alternative way to comm.Get_rank())
rank = comm.rank
# Print the rank of each process as it starts execution
print("my rank is %i" % (rank))

# Code for process with rank 1
if rank == 1:
    # Data to send to process 5
    data_send = "a"
    # Target process to send data to
    destination_process = 5
    # Source process to receive data from (process 5)
    source_process = 5

    # IMPORTANT: This recv() is called BEFORE send()
    # But process 5 will send first, so this will block until process 5 sends
    data_received = comm.recv(source=source_process)
    # Then send data to process 5
    comm.send(data_send, dest=destination_process)
    
    # Print confirmation of sent data
    print("sending data %s " % data_send + \
          "to process %d" % destination_process)
    # Print received data
    print("data received is = %s" % data_received)

# Code for process with rank 5
if rank == 5:
    # Data to send to process 1
    data_send = "b"
    # Target process to send data to (process 1)
    destination_process = 1
    # Source process to receive data from (process 1)
    source_process = 1

    # Send data to process 1 FIRST
    comm.send(data_send, dest=destination_process)
    # Then receive data from process 1
    data_received = comm.recv(source=source_process)
    
    # Print confirmation of sent data
    print("sending data %s :" % data_send + \
          "to process %d" % destination_process)
    # Print received data
    print("data received is = %s" % data_received)



    #output
# my rank is 1
# my rank is 0
# my rank is 2
# my rank is 4
# my rank is 3