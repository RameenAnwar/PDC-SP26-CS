# Rlock.py
# Demonstrates a RE-ENTRANT lock (RLock). An RLock can be acquired multiple times
# by the SAME thread without blocking itself - useful when a locked method calls
# another locked method (here add()/remove() both call execute(), all under the lock).

import threading
import time
import random

class Box:
    def __init__(self):
        self.lock = threading.RLock()   # re-entrant lock
        self.total_items = 0

    def execute(self, value):
        with self.lock:                 # `with` automatically acquires & releases
            self.total_items += value

    def add(self):
        with self.lock:                 # acquires the lock...
            self.execute(1)             # ...then execute() acquires it AGAIN (allowed for RLock)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(box, items):
    print("N° {} items to ADD \n".format(items))
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print("ADDED one item -->{} item to ADD \n".format(items))

def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print("REMOVED one item -->{} item to REMOVE \n".format(items))

def main():
    items = 10
    box = Box()
    # Two threads add and remove a random number of items concurrently.
    t1 = threading.Thread(target=adder,   args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    t1.start(); t2.start()
    t1.join();  t2.join()

if __name__ == "__main__":
    main()
