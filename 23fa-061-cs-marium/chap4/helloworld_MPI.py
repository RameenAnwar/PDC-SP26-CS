#hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print ("hello world from process ", rank)

# Output

# hello world from process  0
# hello world from process  1
# hello world from process  2
# hello world from process  3