import threading  # To use threads and locks
import time  # For delays
import random  # To generate random numbers

class Box:
    def __init__(self):
        self.lock = threading.RLock()  # Reentrant lock to protect shared data
        self.total_items = 0  # Count of total items in the box

    def execute(self, value):
        with self.lock:  # Acquire lock to safely update total_items
            self.total_items += value

    def add(self):
        with self.lock:  # Lock while adding one item
            self.execute(1)

    def remove(self):
        with self.lock:  # Lock while removing one item
            self.execute(-1)

def adder(box, items):
    print("N° {} items to ADD \n".format(items))  # Show how many items to add
    while items:
        box.add()  # Add one item
        time.sleep(1)  # Wait 1 second
        items -= 1  # Decrease remaining items
        print("ADDED one item -->{} item to ADD \n".format(items))  # Show remaining

def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))  # Show how many items to remove
    while items:
        box.remove()  # Remove one item
        time.sleep(1)  # Wait 1 second
        items -= 1  # Decrease remaining items
        print("REMOVED one item -->{} item to REMOVE \n".format(items))  # Show remaining

def main():
    items = 10  # Initial number of items (not used directly here)
    box = Box()  # Create a Box instance

    # Create threads with random number of items to add/remove
    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10)))
    
    t1.start()  # Start adder thread
    t2.start()  # Start remover thread

    t1.join()  # Wait until adder finishes
    t2.join()  # Wait until remover finishes

if __name__ == "__main__":
    main()  # Run the main function