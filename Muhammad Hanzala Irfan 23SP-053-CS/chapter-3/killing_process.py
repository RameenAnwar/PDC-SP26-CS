import multiprocessing
import time

def worker():
    while True:
        print("Working...")
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)

    p.start()

    time.sleep(3)

    p.terminate()

    print("Process terminated")