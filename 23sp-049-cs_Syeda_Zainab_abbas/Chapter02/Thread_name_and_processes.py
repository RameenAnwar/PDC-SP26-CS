# Thread_name_and_processes.py
# Defining a thread by SUBCLASSING threading.Thread and overriding run().

from threading import Thread
import time
import os

class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)     # always call the parent constructor first
        self.name = name
    def run(self):                # run() holds the code that executes in the thread
        print("ID of process running {}".format(self.name))

def main():
    from random import randint
    # Create two threads.
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")

    thread1.start(); thread2.start()   # start both
    thread1.join();  thread2.join()    # wait for both

    print("End")

if __name__ == "__main__":
    main()
