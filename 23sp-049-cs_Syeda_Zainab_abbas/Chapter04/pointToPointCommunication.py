# pointToPointCommunication.py  --  Chapter 4: Point-to-Point Communication
# send()/recv() let TWO specific processes exchange a message directly.
# Here rank 0 -> rank 4, and rank 1 -> rank 8.
# RUN COMMAND:  mpiexec -n 9 python pointToPointCommunication.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# comm = MPI.COMM_WORLD
# rank = comm.rank
# print("my rank is : ", rank)
# if rank == 0:
#     data = 10000000
#     destination_process = 4
#     comm.send(data, dest=destination_process)        # blocking send
#     print("sending data %s " % data + "to process %d" % destination_process)
# if rank == 1:
#     destination_process = 8
#     data = "hello"
#     comm.send(data, dest=destination_process)
#     print("sending data %s :" % data + "to process %d" % destination_process)
# if rank == 4:
#     data = comm.recv(source=0)                        # blocking receive from rank 0
#     print("data received is = %s" % data)
# if rank == 8:
#     data1 = comm.recv(source=1)                       # receive from rank 1
#     print("data1 received is = %s" % data1)
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# my rank is :  0
# sending data 10000000 to process 4
# my rank is :  1
# sending data hello :to process 8
# my rank is :  2
# my rank is :  3
# my rank is :  4
# data received is = 10000000
# my rank is :  5
# my rank is :  6
# my rank is :  7
# my rank is :  8
# data1 received is = hello
# --------------------------------------------------------------------
