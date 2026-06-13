"""
Chapter 2 – Topic 3: How to Determine the Current Thread
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  Each Thread instance carries a name (default: "Thread-N").
  Naming threads makes logging and debugging far easier, especially
  in server applications with many concurrent service threads.

KEY API:
  threading.current_thread()          – returns the Thread object running now
  threading.current_thread().name     – its human-readable name
  threading.current_thread().getName() – older alias (still works)
  threading.enumerate()              – list of all live Thread objects
"""

import threading
import time


def function_A():
    print(threading.current_thread().name + " --> starting")
    time.sleep(2)
    print(threading.current_thread().name + " --> exiting")


def function_B():
    print(threading.current_thread().name + " --> starting")
    time.sleep(2)
    print(threading.current_thread().name + " --> exiting")


def function_C():
    print(threading.current_thread().name + " --> starting")
    time.sleep(2)
    print(threading.current_thread().name + " --> exiting")


def main():
    # Assign meaningful names so we can identify threads in logs
    t1 = threading.Thread(name="function_A", target=function_A)
    t2 = threading.Thread(name="function_B", target=function_B)
    t3 = threading.Thread(name="function_C", target=function_C)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 3: How to Determine the Current Thread")
    print("=" * 55)
    main()
