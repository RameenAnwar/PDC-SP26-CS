import threading
import time

def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

if __name__ == "__main__":
    t1 = threading.Thread(target=task, args=("One",))
    t2 = threading.Thread(target=task, args=("Two",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All threads completed")
