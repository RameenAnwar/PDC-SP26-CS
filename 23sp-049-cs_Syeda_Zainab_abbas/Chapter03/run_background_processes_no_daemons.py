# run_background_processes_no_daemons.py
# Same as the previous file but BOTH processes are non-daemon (daemon = False).
# Now both run to completion and print all their output, because the main program
# waits for non-daemon children to finish.

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    if name == 'background_process':
        for i in range(0, 5):
            print('---> %d \n' % i)
        time.sleep(1)
    else:
        for i in range(5, 10):
            print('---> %d \n' % i)
        time.sleep(1)
    print("Exiting %s \n" % name)

if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = False          # NOT a daemon now

    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
