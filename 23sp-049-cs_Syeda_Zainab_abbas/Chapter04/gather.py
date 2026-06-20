# gather.py  --  Chapter 4: Collective Communication (gather)
# comm.gather() is the OPPOSITE of scatter: every process sends a value to the
# root (rank 0), which collects them all into a list.
# RUN COMMAND:  mpiexec -n 5 python gather.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# size = comm.Get_size()
# rank = comm.Get_rank()
# data = (rank + 1) ** 2                 # each process computes (rank+1) squared
# data = comm.gather(data, root=0)       # send to rank 0; rank 0 gets the full list
# if rank == 0:
#    print("rank = %s " % rank + "...receiving data to other process")
#    for i in range(1, size):
#       value = data[i]
#       print(" process %s receiving %s from process %s" % (rank, value, i))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# rank = 0 ...receiving data to other process
#  process 0 receiving 4 from process 1
#  process 0 receiving 9 from process 2
#  process 0 receiving 16 from process 3
#  process 0 receiving 25 from process 4
# --------------------------------------------------------------------
