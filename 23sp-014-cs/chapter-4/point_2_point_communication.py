from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = "Hello Process 1"
    comm.send(data, dest=1)

elif rank == 1:
    data = comm.recv(source=0)
    print("Received:", data)