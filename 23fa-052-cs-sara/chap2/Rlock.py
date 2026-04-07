import threading  # For locks and threads
import time       # For delays
import random     # For random numbers


class Box:
    """A box that keeps track of total items (can go up or down)"""
    
    def __init__(self):
        # RLock = Reentrant Lock - same thread can lock multiple times
        self.lock = threading.RLock()
        self.total_items = 0  # Counter for items in box

    def execute(self, value):
        """Add or remove items (value can be +1 or -1)"""
        with self.lock:  # Only one thread can change total_items at a time
            self.total_items += value

    def add(self):
        """Add 1 item to box"""
        with self.lock:  # Lock to prevent conflicts
            self.execute(1)  # Add +1

    def remove(self):
        """Remove 1 item from box"""
        with self.lock:  # Lock to prevent conflicts
            self.execute(-1)  # Add -1 (subtract)


def adder(box, items):
    """Thread function - keeps ADDING items to box"""
    print("N° {} items to ADD \n".format(items))
    
    while items:  # Keep adding until items reaches 0
        box.add()           # Add 1 item
        time.sleep(1)       # Wait 1 second
        items -= 1          # Decrease remaining count
        print("ADDED one item -->{} item to ADD \n".format(items))


def remover(box, items):
    """Thread function - keeps REMOVING items from box"""
    print("N° {} items to REMOVE \n".format(items))
    
    while items:  # Keep removing until items reaches 0
        box.remove()        # Remove 1 item
        time.sleep(1)       # Wait 1 second
        items -= 1          # Decrease remaining count
        print("REMOVED one item -->{} item to REMOVE \n".format(items))


def main():
    items = 10  # Not actually used? (Each thread gets random numbers)
    box = Box()  # Create the shared box

    # Thread 1: Adds random items (between 10 to 20 items)
    t1 = threading.Thread(target=adder, \
                          args=(box, random.randint(10,20)))
    
    # Thread 2: Removes random items (between 1 to 10 items)
    t2 = threading.Thread(target=remover, \
                          args=(box, random.randint(1,10)))
    
    # Start both threads
    t1.start()
    t2.start()

    # Wait for both to finish
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()