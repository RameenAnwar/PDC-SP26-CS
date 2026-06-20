# killing_processes.py
# Demonstrates the life cycle of a process and how to forcibly terminate() it.
# is_alive() reports whether the process is currently running.

import multiprocessing
import time

def foo():
    print('Starting function')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())   # not started yet -> False
    p.start()
    print('Process running:', p, p.is_alive())            # now alive -> True
    p.terminate()                                          # kill the process immediately
    print('Process terminated:', p, p.is_alive())
    p.join()                                               # clean up the finished process
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)                # negative code = killed by signal
