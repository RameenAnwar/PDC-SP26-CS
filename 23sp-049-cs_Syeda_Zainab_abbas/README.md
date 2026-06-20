# PDC-SP26 — Parallel & Distributed Computing 

Commented and documented code for the PDC course, based on the *Python Parallel Programming Cookbook* examples. Source code pulled from the class repository and worked on chapter-wise.

## Structure
| Chapter | Topic | Work done |
|---------|-------|-----------|
| **Chapter01** | Parallel computing intro + Python basics | Code **commented**, runnable |
| **Chapter02** | Thread-based parallelism & synchronization | Code **commented**, runnable |
| **Chapter03** | Process-based parallelism | Code **commented**, runnable |
| **Chapter04** | Message passing (MPI / mpi4py) | Code **commented-out** + **expected output** |
| **Chapter05** | Asynchronous programming (asyncio) | Code **commented-out** + **expected output** |
| **Chapter06** | Distributed Python (Celery, Pyro4, sockets) | Code **commented-out** + **expected output** |

Each chapter folder has its own `README.md` with file-by-file notes and run commands.

## How to run
- **Chapters 1–3:** plain Python, e.g. `python serial_test.py`
- **Chapter 4:** needs MPI, e.g. `mpiexec -n 4 python broadcast.py`
- **Chapter 5:** `python asyncio_and_futures.py 5 6`
- **Chapter 6:** needs a broker / Pyro name server / two terminals (see chapter README)
