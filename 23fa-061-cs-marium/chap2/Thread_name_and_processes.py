from threading import Thread  # To use threads
import time  # For delays (not used here, but imported)
import os  # To get process ID (not used in print here)

class MyThreadClass(Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name  # Name of the thread

   def run(self):
       # Print thread name (optional: could include process ID)
       print("ID of process running {}".format(self.name))  

def main():
    from random import randint  # Imported for possible random use

    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

    # End message
    print("End")

if __name__ == "__main__":
    main()  # Run the main function