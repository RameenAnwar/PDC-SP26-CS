# Import threading module for working with threads
import threading

# Import time module to add delay and measure execution time
import time

# Import os module to get process ID
import os

# Import Thread class from threading module
from threading import Thread

# Import randint to generate random duration for each thread
from random import randint

# Create a lock object
# Lock is used to allow only one thread at a time to access a critical section
threadLock = threading.Lock()


# Create a thread class by inheriting from Thread
class MyThreadClass(Thread):
    
   # Constructor to initialize thread name and duration
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration

   # This function runs when the thread starts
   def run(self):
      # Acquire the lock before entering critical section
      threadLock.acquire()      

      # Print thread name and process ID
      print ("---> " + self.name + \
             " running, belonging to process ID "\
             + str(os.getpid()) + "\n")

      # Release the lock so another thread can print
      threadLock.release()

      # Pause the thread for its random duration
      time.sleep(self.duration)

      # Print when thread finishes
      print ("---> " + self.name + " over\n")


# Main function
def main():
    # Record start time to measure total execution time
    start_time = time.time()
    
    # -------------------------
    # Thread Creation
    # -------------------------
    # Create 9 thread objects with random durations between 1 and 10 seconds
    thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1,10))
    thread3 = MyThreadClass("Thread#3 ", randint(1,10))
    thread4 = MyThreadClass("Thread#4 ", randint(1,10))
    thread5 = MyThreadClass("Thread#5 ", randint(1,10))
    thread6 = MyThreadClass("Thread#6 ", randint(1,10))
    thread7 = MyThreadClass("Thread#7 ", randint(1,10))
    thread8 = MyThreadClass("Thread#8 ", randint(1,10))
    thread9 = MyThreadClass("Thread#9 ", randint(1,10))

    # -------------------------
    # Thread Running
    # -------------------------
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

    # -------------------------
    # Thread Joining
    # -------------------------
    # Wait for all threads to finish before moving ahead
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # Print end message after all threads are done
    print("End")

    # Print total execution time
    print("--- %s seconds ---" % (time.time() - start_time))


# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    main()


#     This code creates 9 threads, and each thread runs for a random amount of time between 1 and 10 seconds.

# What each thread does:
# First it acquires a lock
# Then it prints:
# thread name
# process ID
# Then it releases the lock
# Then it sleeps for some random seconds
# Then it prints that it is over

# output

# ---> Thread#1  running, belonging to process ID 23824

# ---> Thread#2  running, belonging to process ID 23824

# ---> Thread#3  running, belonging to process ID 23824

# ---> Thread#4  running, belonging to process ID 23824

# ---> Thread#5  running, belonging to process ID 23824

# ---> Thread#6  running, belonging to process ID 23824

# ---> Thread#7  running, belonging to process ID 23824

# ---> Thread#8  running, belonging to process ID 23824

# ---> Thread#9  running, belonging to process ID 23824

# ---> Thread#2  over

# ---> Thread#3  over

# ---> Thread#5  over

# ---> Thread#7  over

# ---> Thread#8  over

# ---> Thread#1  over

# ---> Thread#6  over

# ---> Thread#4  over

# ---> Thread#9  over

# End
# --- 9.003803491592407 seconds ---