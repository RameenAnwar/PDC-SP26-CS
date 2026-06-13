from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2

data = comm.gather(data, root=0)
if rank == 0:
   print ("rank = %s " %rank +\
          "...receiving data to other process")
   for i in range(1,size):

      value = data[i]
      print(" process %s receiving %s from process %s"\
            %(rank , value , i))

# Output

# rank = 0 ...receiving data to other process
#  process 0 receiving 4 from process 1
#  process 0 receiving 9 from process 2
#  process 0 receiving 16 from process 3
