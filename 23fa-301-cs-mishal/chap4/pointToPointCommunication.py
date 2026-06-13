# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the rank (ID) of the current process
rank = comm.rank
# Print the rank of each process as it starts execution
print("my rank is : ", rank)

# Process with rank 0 sends integer data to process 4
if rank == 0:
    data = 10000000  # Integer data to send
    destination_process = 4  # Target process to receive the data
    # Send the data to process 4 (non-blocking send)
    comm.send(data, dest=destination_process)
    # Print confirmation of sent data
    print("sending data %s " % data + \
          "to process %d" % destination_process)

# Process with rank 1 sends string data to process 8
if rank == 1:
    destination_process = 8  # Target process to receive the data
    data = "hello"  # String data to send
    # Send the string to process 8
    comm.send(data, dest=destination_process)
    # Print confirmation of sent data
    print("sending data %s :" % data + \
          "to process %d" % destination_process)

# Process with rank 4 receives data from process 0
if rank == 4:
    # Receive data specifically from process 0 (source=0)
    # This will block until process 0 sends the data
    data = comm.recv(source=0)
    # Print the received data (should be 10000000)
    print("data received is = %s" % data)

# Process with rank 8 receives data from process 1
if rank == 8:
    # Receive data specifically from process 1 (source=1)
    # This will block until process 1 sends the data
    data1 = comm.recv(source=1)
    # Print the received data (should be "hello")
    print("data1 received is = %s" % data1)

#     What this code does:
# This code demonstrates point-to-point communication between specific process pairs:

#ouptut
# my rank is :  3
# my rank is :  0
# sending data 10000000 to process 4
# my rank is :  4
# data received is = 10000000
# my rank is :  1
# my rank is :  2