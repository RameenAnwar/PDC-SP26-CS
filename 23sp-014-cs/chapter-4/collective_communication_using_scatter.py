from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None

if rank == 0:
    data = [10, 20, 30, 40]

received = comm.scatter(data, root=0)

print("Process", rank, "received:", received)