import multiprocessing
import time

def worker():
    while True:
        print("Background process running")
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)

    p.daemon = True

    p.start()

    time.sleep(5)

    print("Main process finished")