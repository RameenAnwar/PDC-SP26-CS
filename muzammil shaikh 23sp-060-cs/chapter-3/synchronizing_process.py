from multiprocessing import Process, Lock

def display(lock, name):
    lock.acquire()

    try:
        for i in range(5):
            print(name)
    finally:
        lock.release()

if __name__ == "__main__":
    lock = Lock()

    p1 = Process(target=display, args=(lock, "Process 1"))
    p2 = Process(target=display, args=(lock, "Process 2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()