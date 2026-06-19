# Import threading module for working with threads
import threading

# Import time module to add delay and measure execution time
import time

# Import os module to get process ID
import os

# Import Thread class from threading module
from threading import Thread

# Import randint to assign random sleep time to each thread
from random import randint

# Lock Definition
# Lock is used so only one thread can enter the critical section at a time
threadLock = threading.Lock()

# Create a thread class by inheriting from Thread
class MyThreadClass (Thread):
    
   # Constructor to initialize thread name and duration
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration

   # This function runs when the thread starts
   def run(self):
      # Acquire the Lock before entering critical section
      threadLock.acquire()      
      
      # Print thread name and process ID
      print ("---> " + self.name + \
             " running, belonging to process ID "\
             + str(os.getpid()) + "\n")
      
      # Pause thread for random duration while lock is still held
      time.sleep(self.duration)
      
      # Print that the thread has finished
      print ("---> " + self.name + " over\n")
      
      # Release the Lock so another thread can run
      threadLock.release()


# Main function
def main():
    # Record start time to measure total execution time
    start_time = time.time()
    
    # Thread Creation
    # Create 9 threads with random duration between 1 and 10 seconds
    thread1 = MyThreadClass("Thread#1 ", randint(1,10))
    thread2 = MyThreadClass("Thread#2 ", randint(1,10))
    thread3 = MyThreadClass("Thread#3 ", randint(1,10))
    thread4 = MyThreadClass("Thread#4 ", randint(1,10))
    thread5 = MyThreadClass("Thread#5 ", randint(1,10))
    thread6 = MyThreadClass("Thread#6 ", randint(1,10))
    thread7 = MyThreadClass("Thread#7 ", randint(1,10))
    thread8 = MyThreadClass("Thread#8 ", randint(1,10))
    thread9 = MyThreadClass("Thread#9 ", randint(1,10))

    # Thread Running
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

    # Thread joining
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

    # End 
    # Print end message after all threads complete
    print("End")

    # Execution Time
    # Print total time taken by the program
    print("--- %s seconds ---" % (time.time() - start_time))


# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    main()


    #This code demonstrates multithreading with a lock in Python. It creates nine threads,
    #  each assigned a random duration between 1 and 10 seconds. When a thread starts, it acquires a lock,
    #  prints its name and process ID, sleeps for its assigned time, and then prints that it is over before releasing the lock. 
    # Since the lock is held during the entire execution inside run(), only one thread can execute this section at a time,
    #  making the threads behave almost like serial execution. 
    # The program waits for all threads to finish using join() and then prints the total execution time.

# Only one thread could run critical section at a time
# Output was more controlled
# Threads behaved more like one by one

#     output
#     ---> Thread#1  running, belonging to process ID 28640

# ---> Thread#1  over

# ---> Thread#2  running, belonging to process ID 28640

# ---> Thread#2  over

# ---> Thread#3  running, belonging to process ID 28640

# ---> Thread#3  over

# ---> Thread#4  running, belonging to process ID 28640

# ---> Thread#4  over

# ---> Thread#5  running, belonging to process ID 28640

# ---> Thread#5  over

# ---> Thread#6  running, belonging to process ID 28640

# ---> Thread#6  over

# ---> Thread#7  running, belonging to process ID 28640

# ---> Thread#7  over

# ---> Thread#8  running, belonging to process ID 28640

# ---> Thread#8  over

# ---> Thread#9  running, belonging to process ID 28640

# ---> Thread#9  over

# End
# --- 41.017375469207764 seconds ---