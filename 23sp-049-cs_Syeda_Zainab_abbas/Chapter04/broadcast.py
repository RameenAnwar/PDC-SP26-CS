# broadcast.py  --  Chapter 4: Collective Communication (broadcast)
# comm.bcast() sends a value from the root process (rank 0) to ALL processes.
# RUN COMMAND:  mpiexec -n 10 python broadcast.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# if rank == 0:
#    variable_to_share = 100            # only rank 0 sets the real value
# else:
#    variable_to_share = None           # others start with nothing
# variable_to_share = comm.bcast(variable_to_share, root=0)   # rank 0 broadcasts to all
# print("process = %d" % rank + " variable shared  = %d " % variable_to_share)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# process = 0 variable shared  = 100
# process = 1 variable shared  = 100
# process = 2 variable shared  = 100
# process = 3 variable shared  = 100
# process = 4 variable shared  = 100
# process = 5 variable shared  = 100
# process = 6 variable shared  = 100
# process = 7 variable shared  = 100
# process = 8 variable shared  = 100
# process = 9 variable shared  = 100
# --------------------------------------------------------------------
