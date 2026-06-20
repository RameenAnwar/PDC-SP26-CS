# spawning_processes.py
# The most basic example: spawn (create and start) a process that runs myFunc().

import multiprocessing

def myFunc(i):
    print('calling myFunc from process n°: %s' % i)
    for j in range(0, i):
        print('output from myFunc is :%s' % j)
    return

if __name__ == '__main__':
    for i in range(6):
        # Create a process targeting myFunc with argument i.
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()    # start the process
        process.join()     # wait for it to finish before spawning the next
