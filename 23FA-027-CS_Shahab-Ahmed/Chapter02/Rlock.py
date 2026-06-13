import threading
import time
import random


class Box:
    def __init__(self):
        # Reentrant Lock (RLock) allows the same thread to acquire the lock multiple times
        # This is important here because add() and remove() both call execute(),
        # and all of them use the same lock
        self.lock = threading.RLock()
        
        # Shared resource that will be modified by multiple threads
        self.total_items = 0

    def execute(self, value):
        # Critical section: only one thread can modify total_items at a time
        with self.lock:
            self.total_items += value

    def add(self):
        # Acquire lock before adding an item
        # Calls execute() which also uses the same lock (safe because of RLock)
        with self.lock:
            self.execute(1)

    def remove(self):
        # Acquire lock before removing an item
        # Calls execute() which also uses the same lock
        with self.lock:
            self.execute(-1)


def adder(box, items):
    # Function executed by thread t1 to add items
    print("N° {} items to ADD \n".format(items))
    
    while items:
        box.add()              # Add one item to the box
        time.sleep(1)          # Simulate delay (like real-world processing)
        items -= 1             # Decrease remaining items count
        
        print("ADDED one item -->{} item to ADD \n".format(items))


def remover(box, items):
    # Function executed by thread t2 to remove items
    print("N° {} items to REMOVE \n".format(items))
    
    while items:
        box.remove()           # Remove one item from the box
        time.sleep(1)          # Simulate delay
        items -= 1             # Decrease remaining items count
        
        print("REMOVED one item -->{} item to REMOVE \n".format(items))


def main():
    items = 10  # (Not used directly, just a placeholder value)
    
    # Create a shared Box object that both threads will modify
    box = Box()

    # Create thread t1 to ADD a random number of items (10–20)
    t1 = threading.Thread(
        target=adder,
        args=(box, random.randint(10, 20))
    )

    # Create thread t2 to REMOVE a random number of items (1–10)
    t2 = threading.Thread(
        target=remover,
        args=(box, random.randint(1, 10))
    )
    
    # Start both threads (they will run concurrently)
    t1.start()
    t2.start()

    # Wait for both threads to finish execution before moving on
    t1.join()
    t2.join()
    

# Entry point of the program
if __name__ == "__main__":
    main()