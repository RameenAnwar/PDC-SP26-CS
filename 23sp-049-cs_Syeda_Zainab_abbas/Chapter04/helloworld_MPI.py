# helloworld_MPI.py  --  Chapter 4: Message Passing (MPI with mpi4py)
# The classic MPI "hello world". Every process prints its own rank (ID).
# RUN COMMAND:  mpiexec -n 5 python helloworld_MPI.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD          # the default communicator = all processes
# rank = comm.Get_rank()         # this process's unique ID (0,1,2,...)
# print("hello world from process ", rank)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (Order varies every run because the processes run in parallel)
# hello world from process  1
# hello world from process  0
# hello world from process  3
# hello world from process  2
# hello world from process  4
# --------------------------------------------------------------------
