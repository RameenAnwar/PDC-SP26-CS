from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = np.array(rank, dtype='i')

total = np.array(0, dtype='i')

comm.Reduce(data, total, op=MPI.SUM, root=0)

if rank == 0:
    print("Optimized Sum =", total)