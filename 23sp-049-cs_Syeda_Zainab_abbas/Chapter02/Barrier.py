# Barrier.py
# A BARRIER makes a set of threads WAIT for each other at a common point.
# Here 3 "runners" each sleep a random time, then wait at the finish line.
# The race is only "over" once ALL runners have reached the barrier.

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)    # barrier releases only when 3 threads wait on it
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))            # each runner takes a different amount of time
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()               # wait here until all runners arrive

def main():
    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()
