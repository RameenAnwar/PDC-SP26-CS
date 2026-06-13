from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Message from 0", dest=1)
    msg = comm.recv(source=1)
    print(msg)

elif rank == 1:
    msg = comm.recv(source=0)
    print(msg)

    comm.send("Reply from 1", dest=0)