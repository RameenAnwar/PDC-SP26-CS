# naming_processes.py
# Shows how to give processes NAMES. One process gets a custom name, the other
# uses the default auto-generated name (Process-1, etc.).

import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name   # read this process's name
    print("Starting process name = %s \n" % name)
    time.sleep(3)
    print("Exiting process name = %s \n" % name)

if __name__ == '__main__':
    # Process with an explicit, custom name.
    process_with_name = multiprocessing.Process(name='myFunc process', target=myFunc)
    # Process that will get a default name automatically.
    process_with_default_name = multiprocessing.Process(target=myFunc)

    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
