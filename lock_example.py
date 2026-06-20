import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    
    lock.acquire()
    for i in range(100000):
        counter += 1
    lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter:", counter)
