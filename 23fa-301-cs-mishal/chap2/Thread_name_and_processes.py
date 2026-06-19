# Import Thread class from threading module to create threads
from threading import Thread
# Import time module (not used here but can be used for delays)
import time
# Import os module to access operating system functionalities (like process ID)
import os

# Define a custom thread class that inherits from Thread
class MyThreadClass (Thread):
   # Constructor to initialize the thread with a name
   def __init__(self, name):
      Thread.__init__(self)  # Initialize the parent Thread class
      self.name = name       # Store the name of the thread
 
   # The run() method defines the code executed by the thread
   def run(self):
       # Print the name of the thread currently running
       print("ID of process running {}".format(self.name)) 
       # You can also print the process ID using os.getpid() if uncommented

# Main function to create and run threads
def main():
    from random import randint  # Import randint for random numbers (not used here)
    
    # Thread Creation: create two threads with names
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Thread Running: start the threads
    thread1.start()
    thread2.start()

    # Thread joining: wait for both threads to finish
    thread1.join()
    thread2.join()

    # End of program
    print("End")

# Ensure this code runs only when executed directly
if __name__ == "__main__":
    main()

   # This code defines a custom thread class MyThreadClass and creates two threads with different names. 
   # Each thread simply prints its name when running. 
   # The start() method begins thread execution, and join() ensures the main program waits until both threads finish. 
   # The program finally prints "End". This demonstrates basic thread creation and execution in Python.