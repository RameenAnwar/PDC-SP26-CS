# serialtest.py

import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

start = time.time()

task("Task 1")
task("Task 2")

end = time.time()

print("Total Time:", end - start)