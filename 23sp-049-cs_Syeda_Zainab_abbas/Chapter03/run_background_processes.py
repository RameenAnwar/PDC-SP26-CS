# run_background_processes.py
# DAEMON vs non-daemon processes. A daemon process runs in the background and is
# killed automatically when the main program exits. Here background_process is a
# daemon, so it may not finish/print fully before the program ends.

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
    background_process.daemon = True          # DAEMON = background, dies with main program

    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
    NO_background_process.daemon = False       # normal foreground process

    background_process.start()
    NO_background_process.start()
