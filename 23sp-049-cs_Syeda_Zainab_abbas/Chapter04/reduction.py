# reduction.py  --  Chapter 4: Collective Communication (reduce)
# comm.Reduce() combines values from all processes using an operation (here MPI.SUM)
# and stores the single combined result on the root process (rank 0).
# RUN COMMAND:  mpiexec -n 3 python reduction.py
# NOTE: numpy.int is deprecated in new NumPy - replace with `int` if you get an error.
#
# ----------------------- CODE (commented out) -----------------------
# import numpy
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# size = comm.size
# rank = comm.rank
# array_size = 10
# recvdata = numpy.zeros(array_size, dtype=numpy.int)
# senddata = (rank + 1) * numpy.arange(array_size, dtype=numpy.int)
# print(" process %s sending %s " % (rank, senddata))
# comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)   # element-wise SUM across processes
# print('on task', rank, 'after Reduce:    data = ', recvdata)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (run with 3 processes; rank 0 holds the summed array)
#  process 0 sending [0 1 2 3 4 5 6 7 8 9]
#  process 1 sending [ 0  2  4  6  8 10 12 14 16 18]
#  process 2 sending [ 0  3  6  9 12 15 18 21 24 27]
# on task 1 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
# on task 2 after Reduce:    data =  [0 0 0 0 0 0 0 0 0 0]
# on task 0 after Reduce:    data =  [ 0  6 12 18 24 30 36 42 48 54]
# --------------------------------------------------------------------
