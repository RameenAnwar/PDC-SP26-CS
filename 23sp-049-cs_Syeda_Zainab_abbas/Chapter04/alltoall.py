# alltoall.py  --  Chapter 4: Collective Communication (all-to-all)
# Alltoall: every process sends a distinct piece of data to every other process,
# and receives a piece from every process (a full matrix "transpose" of data).
# RUN COMMAND:  mpiexec -n 4 python alltoall.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# import numpy
# comm = MPI.COMM_WORLD
# size = comm.Get_size()
# rank = comm.Get_rank()
# senddata = (rank + 1) * numpy.arange(size, dtype=int)   # data this process sends
# recvdata = numpy.empty(size, dtype=int)                 # buffer for what it receives
# comm.Alltoall(senddata, recvdata)
# print(" process %s sending %s receiving %s" % (rank, senddata, recvdata))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (run with 4 processes)
#  process 0 sending [0 0 0 0] receiving [0 0 0 0]
#  process 1 sending [0 2 4 6] receiving [0 2 4 6]
#  process 2 sending [0 3 6 9] receiving [0 4 8 12]
#  process 3 sending [0 4 8 12] receiving [0 6 12 18]
# --------------------------------------------------------------------
