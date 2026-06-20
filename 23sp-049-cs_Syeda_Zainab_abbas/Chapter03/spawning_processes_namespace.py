# spawning_processes_namespace.py
# Same as spawning_processes.py, but myFunc is imported from the separate
# myFunc module (a "namespace"). Good practice: keep worker functions in their
# own module so they import cleanly in child processes.

import multiprocessing
from myFunc import myFunc          # import the function from myFunc.py

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
