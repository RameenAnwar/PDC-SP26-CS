# deadLockProblems.py  --  Chapter 4: Avoiding Deadlock
# A deadlock happens when two processes wait on each other forever. Here the
# ORDER of send/recv is arranged so it does NOT deadlock: rank 5 sends first while
# rank 1 receives first, so neither blocks permanently. (If both called recv()
# before send(), with no matching send, they would hang = deadlock.)
# RUN COMMAND:  mpiexec -n 6 python deadLockProblems.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# rank = comm.rank
# print("my rank is %i" % (rank))
# if rank == 1:
#     data_send = "a"
#     destination_process = 5
#     source_process = 5
#     data_received = comm.recv(source=source_process)   # receive first
#     comm.send(data_send, dest=destination_process)     # then send
#     print("sending data %s " % data_send + "to process %d" % destination_process)
#     print("data received is = %s" % data_received)
# if rank == 5:
#     data_send = "b"
#     destination_process = 1
#     source_process = 1
#     comm.send(data_send, dest=destination_process)     # send first
#     data_received = comm.recv(source=source_process)   # then receive
#     print("sending data %s :" % data_send + "to process %d" % destination_process)
#     print("data received is = %s" % data_received)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# my rank is 0
# my rank is 2
# my rank is 3
# my rank is 4
# my rank is 1
# my rank is 5
# sending data b :to process 1
# data received is = a
# sending data a to process 5
# data received is = b
# --------------------------------------------------------------------
