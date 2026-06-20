# Thread_definition.py
# The simplest way to define and run a thread: pass a target function to Thread().

import threading

def my_func(thread_number):
    # Each thread runs this function with its own number.
    return print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []
    for i in range(10):
        # target = function to run, args = tuple of arguments for it
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()      # begin execution of the thread
        t.join()       # wait for it to finish (here threads run one-by-one)

if __name__ == "__main__":
    main()
