# MyThreadClass.py
# Subclassing Thread. Nine threads each sleep for a RANDOM duration. Because there
# is NO lock, their start/finish messages interleave freely (concurrent output).

import time
import os
from random import randint
from threading import Thread

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration      # how long this thread will sleep
    def run(self):
        print("---> " + self.name + " running, belonging to process ID " + str(os.getpid()) + "\n")
        time.sleep(self.duration)     # simulate work of variable length
        print("---> " + self.name + " over\n")

def main():
    start_time = time.time()

    # Create 9 threads, each with a random sleep duration (1-10 sec).
    thread1 = MyThreadClass("Thread#1 ", randint(1, 10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))

    # Start them all (they run concurrently).
    thread1.start(); thread2.start(); thread3.start()
    thread4.start(); thread5.start(); thread6.start()
    thread7.start(); thread8.start(); thread9.start()

    # Join them all (wait until every thread has finished).
    thread1.join(); thread2.join(); thread3.join()
    thread4.join(); thread5.join(); thread6.join()
    thread7.join(); thread8.join(); thread9.join()

    print("End")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
