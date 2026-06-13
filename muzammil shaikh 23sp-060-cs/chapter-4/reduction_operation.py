from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank + 1

result = comm.reduce(data, op=MPI.SUM, root=0)

if rank == 0:
    print("Sum =", result)