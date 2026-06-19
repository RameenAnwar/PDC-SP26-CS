from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


senddata = (rank+1)*numpy.arange(size,dtype=int)
recvdata = numpy.empty(size,dtype=int)
comm.Alltoall(senddata,recvdata)


print(" process %s sending %s receiving %s"\
      %(rank , senddata , recvdata))

#output
#process 0 sending [0 1 2 3] receiving [0 0 0 0]
#process 1 sending [0 2 4 6] receiving [1 2 3 4]
#process 2 sending [0 3 6 9] receiving [2 4 6 8]
#process 3 sending [ 0  4  8 12] receiving [ 3  6  9 12]