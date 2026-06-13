import threading  # To use threads and locks
import time  # For delays and measuring execution time
import os  # To get process ID
from threading import Thread  # Thread class
from random import randint  # To generate random duration for threads

# Lock Definition
threadLock = threading.Lock()  # Create a lock to control thread access

class MyThreadClass (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name  # Name of the thread
      self.duration = duration  # Duration thread will run

   def run(self):
      # Acquire the Lock before printing and running
      threadLock.acquire()      
      print ("---> " + self.name + \
             " running, belonging to process ID "\
             + str(os.getpid()) + "\n")  # Show thread name and process ID
      time.sleep(self.duration)  # Simulate work by sleeping
      print ("---> " + self.name + " over\n")  # Print when thread finishes
      # Release the Lock after work is done
      threadLock.release()


def main():
    start_time = time.time()  # Record start time

    # Thread Creation with random durations
    thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1,10))
    thread3 = MyThreadClass("Thread#3 ", randint(1,10))
    thread4 = MyThreadClass("Thread#4 ", randint(1,10))
    thread5 = MyThreadClass("Thread#5 ", randint(1,10))
    thread6 = MyThreadClass("Thread#6 ", randint(1,10))
    thread7 = MyThreadClass("Thread#7 ", randint(1,10))
    thread8 = MyThreadClass("Thread#8 ", randint(1,10))
    thread9 = MyThreadClass("Thread#9 ", randint(1,10))

    # Start all threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End message
    print("End")

    # Print total execution time
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()  # Run the main function