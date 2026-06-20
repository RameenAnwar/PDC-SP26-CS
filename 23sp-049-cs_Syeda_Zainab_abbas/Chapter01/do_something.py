# do_something.py
# Helper module used by the serial / threading / multiprocessing tests.
# It does a CPU-bound job: fill a list with `count` random floating-point numbers.

import random  # standard library module for generating random numbers


def do_something(count, out_list):
    # Loop `count` times and append a random float (0.0 - 1.0) each time.
    # This deliberately keeps the CPU busy so we can compare execution times
    # between serial, multithreaded and multiprocess versions.
    for i in range(count):
        out_list.append(random.random())
