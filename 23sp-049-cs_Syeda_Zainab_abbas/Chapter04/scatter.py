# scatter.py  --  Chapter 4: Collective Communication (scatter)
# comm.scatter() SPLITS a list on the root and gives ONE element to each process.
# RUN COMMAND:  mpiexec -n 10 python scatter.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# if rank == 0:
#    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # 10 items, one per process
# else:
#    array_to_share = None
# recvbuf = comm.scatter(array_to_share, root=0)   # each process gets array[rank]
# print("process = %d" % rank + " variable shared  = %d " % recvbuf)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# process = 0 variable shared  = 1
# process = 1 variable shared  = 2
# process = 2 variable shared  = 3
# process = 3 variable shared  = 4
# process = 4 variable shared  = 5
# process = 5 variable shared  = 6
# process = 6 variable shared  = 7
# process = 7 variable shared  = 8
# process = 8 variable shared  = 9
# process = 9 variable shared  = 10
# --------------------------------------------------------------------
