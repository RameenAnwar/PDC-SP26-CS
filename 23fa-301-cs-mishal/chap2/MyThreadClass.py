# Import time module to add delay and measure execution time
import time

# Import os module to get process ID
import os

# Import randint to assign random sleep time to each thread
from random import randint

# Import Thread class for creating custom threads
from threading import Thread

# Create a custom thread class by inheriting from Thread
class MyThreadClass (Thread):
    
   # Constructor to initialize thread name and duration
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration

   # This function runs when the thread starts
   def run(self):
      # Print thread name and process ID
      print ("---> " + self.name + \
             " running, belonging to process ID "\
             + str(os.getpid()) + "\n")
      
      # Pause the thread for its random duration
      time.sleep(self.duration)
      
      # Print when the thread finishes
      print ("---> " + self.name + " over\n")


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


    #This code demonstrates basic multithreading in Python without using any synchronization mechanism like a lock.
    #  It creates nine threads, each assigned a random duration between 1 and 10 seconds. 
    # When a thread starts, it prints its name and process ID, sleeps for its assigned duration, and then prints that it has completed. 
    # Since there is no lock, multiple threads can run and print at the same time, so the output order may vary each time the program is executed.
    #  The join() method ensures the main program waits for all threads to finish before printing "End" and the total execution time.


#     This code (without lock):
# Threads run freely at the same time
# Output may come in mixed order
# Faster parallel behavior

#     output
#     ---> Thread#4  running, belonging to process ID 14096
# ---> Thread#3  running, belonging to process ID 14096


# ---> Thread#5  running, belonging to process ID 14096

# ---> Thread#6  running, belonging to process ID 14096

# ---> Thread#7  running, belonging to process ID 14096

# ---> Thread#8  running, belonging to process ID 14096
# ---> Thread#9  running, belonging to process ID 14096


# ---> Thread#1  over

# ---> Thread#9  over

# ---> Thread#6  over

# ---> Thread#3  over

# ---> Thread#8  over

# ---> Thread#4  over

# ---> Thread#7  over

# ---> Thread#5  over
# ---> Thread#2  over


# End
# --- 10.003739833831787 seconds ---