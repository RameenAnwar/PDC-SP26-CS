import threading
import time
import os
from threading import Thread
from random import randint

# Global Lock object
# Used to ensure that only one thread executes a critical section at a time
threadLock = threading.Lock()

class MyThreadClass(Thread):
   def __init__(self, name, duration):
      # Initialize the parent Thread class
      Thread.__init__(self)
      
      # Store thread name and sleep duration
      self.name = name
      self.duration = duration

   def run(self):
      # This method is automatically called when thread.start() is executed
      
      # Acquire the lock before entering critical section (printing)
      threadLock.acquire()
      
      # Critical section: only one thread can print this at a time
      print("---> " + self.name +
            " running, belonging to process ID "
            + str(os.getpid()) + "\n")
      
      # Release the lock so other threads can access this section
      threadLock.release()
      
      # Simulate some work by sleeping for a random duration
      time.sleep(self.duration)
      
      # This part is NOT protected by lock, so output order may vary
      print("---> " + self.name + " over\n")
      # (No lock used here intentionally)


def main():
    # Record start time to measure execution duration
    start_time = time.time()
    
    # -------- Thread Creation --------
    # Create 9 threads with random sleep durations (1–10 seconds)
    thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1,10))
    thread3 = MyThreadClass("Thread#3 ", randint(1,10))
    thread4 = MyThreadClass("Thread#4 ", randint(1,10))
    thread5 = MyThreadClass("Thread#5 ", randint(1,10))
    thread6 = MyThreadClass("Thread#6 ", randint(1,10))
    thread7 = MyThreadClass("Thread#7 ", randint(1,10))
    thread8 = MyThreadClass("Thread#8 ", randint(1,10))
    thread9 = MyThreadClass("Thread#9 ", randint(1,10))

    # -------- Start Threads --------
    # All threads begin execution concurrently
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # -------- Join Threads --------
    # Wait for all threads to finish before continuing
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # Program end indicator
    print("End")

    # Print total execution time
    print("--- %s seconds ---" % (time.time() - start_time))


# Entry point of the program
if __name__ == "__main__":
    main()