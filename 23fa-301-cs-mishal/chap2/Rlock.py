# Import threading module for threads and locks
import threading

# Import time module to add delay
import time

# Import random module to generate random number of items
import random


# Create a Box class
class Box:
    
    # Constructor of Box class
    def __init__(self):
        # Create an RLock (Reentrant Lock)
        # It allows the same thread to acquire the lock multiple times
        self.lock = threading.RLock()
        
        # Variable to keep track of total items in the box
        self.total_items = 0

    # Function to update total_items by adding or subtracting value
    def execute(self, value):
        # Acquire lock before modifying shared data
        with self.lock:
            self.total_items += value

    # Function to add 1 item to the box
    def add(self):
        # Acquire lock before calling execute
        with self.lock:
            self.execute(1)

    # Function to remove 1 item from the box
    def remove(self):
        # Acquire lock before calling execute
        with self.lock:
            self.execute(-1)


# Function for adding items
def adder(box, items):
    # Print how many items will be added
    print("N° {} items to ADD \n".format(items))
    
    # Keep adding until items become 0
    while items:
        # Add 1 item to the box
        box.add()
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease remaining items count
        items -= 1
        
        # Print remaining items to add
        print("ADDED one item -->{} item to ADD \n".format(items))


# Function for removing items
def remover(box, items):
    # Print how many items will be removed
    print("N° {} items to REMOVE \n".format(items))
    
    # Keep removing until items become 0
    while items:
        # Remove 1 item from the box
        box.remove()
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease remaining items count
        items -= 1
        
        # Print remaining items to remove
        print("REMOVED one item -->{} item to REMOVE \n".format(items))


# Main function
def main():
    # Local variable (not actually used later)
    items = 10
    
    # Create Box object
    box = Box()

    # Create first thread for adding random number of items (10 to 20)
    t1 = threading.Thread(target=adder, \
                          args=(box, random.randint(10,20)))
    
    # Create second thread for removing random number of items (1 to 10)
    t2 = threading.Thread(target=remover, \
                          args=(box, random.randint(1,10)))
    
    # Start adder thread
    t1.start()
    
    # Start remover thread
    t2.start()

    # Wait for adder thread to finish
    t1.join()
    
    # Wait for remover thread to finish
    t2.join()
    

# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    main()


   # This code demonstrates the use of multithreading with RLock (Reentrant Lock) in Python to safely manage access to shared data. 
   # A Box object contains a shared variable total_items, which is updated by two threads: one thread adds items while the other removes items.
   #  The RLock ensures that the same thread can safely acquire the lock multiple times when methods like add() and remove() internally call execute(), which also uses the same lock. 
   # This prevents race conditions and allows both threads to work safely on the shared resource while printing progress after each operation.

#    Thread 1 → adder
# gets a random number from 10 to 20
# adds one item every second
# prints remaining items to add
# Thread 2 → remover
# gets a random number from 1 to 10
# removes one item every second
# prints remaining items to remove
# What happens overall
# both threads work on the same box
# both change the same variable total_items
# RLock makes sure this shared data is updated safely
# one thread adds, one removes

#output
# N° 12 items to ADD 

# N° 4 items to REMOVE

# ADDED one item -->11 item to ADD 
# REMOVED one item -->3 item to REMOVE


# REMOVED one item -->2 item to REMOVE 
# ADDED one item -->10 item to ADD


# ADDED one item -->9 item to ADD 
# REMOVED one item -->1 item to REMOVE


# ADDED one item -->8 item to ADD 

# REMOVED one item -->0 item to REMOVE

# ADDED one item -->7 item to ADD 

# ADDED one item -->6 item to ADD 

# ADDED one item -->5 item to ADD 

# ADDED one item -->4 item to ADD 

# ADDED one item -->3 item to ADD 

# ADDED one item -->2 item to ADD 

# ADDED one item -->1 item to ADD 

# ADDED one item -->0 item to ADD