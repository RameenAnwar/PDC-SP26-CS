"""
Chapter 2 – Topic 10: Thread Synchronization with a Barrier
Python Parallel Programming Cookbook (2nd Edition) – Giancarlo Zaccone

CONCEPT:
  A Barrier divides a program's execution into PHASES.
  All threads in a group must reach the barrier before any of them
  are allowed to proceed to the next phase.

HOW IT WORKS:
  barrier = threading.Barrier(n)   – create barrier for n threads
  barrier.wait()                   – each thread calls this when it reaches
                                     the synchronisation point; blocks until
                                     all n threads have called wait().
                                     The last thread to call wait() releases
                                     all of them simultaneously.

ADDITIONAL API:
  barrier.broken   – True if the barrier is in a broken state
  barrier.parties  – number of threads the barrier waits for
  barrier.n_waiting – threads currently waiting at the barrier
  barrier.reset()  – reset to default empty state (may cause BrokenBarrierError)
  barrier.abort()  – put barrier in broken state (wake all with BrokenBarrierError)

USE CASES:
  - Parallel simulations where all workers must finish phase N before phase N+1.
  - Parallel tests that must all complete setup before any starts execution.
  - Race / game simulations (all runners must finish before results announced).

RISK:
  If one thread never calls wait() (crash, bug), the others block forever.
  Use barrier.abort() or timeouts (barrier.wait(timeout)) to guard against this.

EXAMPLE:
  Simulate a race: Huey, Dewey, and Louie run at random speeds.
  Results are only announced once ALL runners cross the finish line.
"""

import threading
import time
from random import randrange
from threading import Barrier, Thread
from time import ctime


num_runners = 3
finish_line = Barrier(num_runners)          # all 3 must arrive before any proceeds
runners     = ["Huey", "Dewey", "Louie"]


def runner():
    """Each runner sleeps for a random time, then waits at the barrier."""
    name       = runners.pop()
    sleep_time = randrange(1, 5)
    time.sleep(sleep_time)
    print(f"{name} reached the barrier at: {ctime()}")
    finish_line.wait()                      # block until all 3 have arrived


def demo_race():
    print("\n--- Race simulation ---")
    print("START RACE!!!!")

    threads = [Thread(target=runner) for _ in range(num_runners)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Race over!")


def demo_phased_computation():
    """
    Two-phase parallel computation:
      Phase 1 – each worker squares its number.
      Phase 2 – each worker prints double of its result.
    No worker starts phase 2 until all have finished phase 1.
    """
    print("\n--- Two-phase phased computation ---")
    barrier = Barrier(4)
    results = [0] * 4

    def worker(idx, value):
        # Phase 1
        results[idx] = value ** 2
        print(f"Worker-{idx} finished phase 1: {results[idx]}")
        barrier.wait()          # wait for all workers to finish phase 1

        # Phase 2 (all workers now have access to the complete results list)
        doubled = results[idx] * 2
        print(f"Worker-{idx} finished phase 2: {doubled}")

    threads = [Thread(target=worker, args=(i, i + 1)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main():
    demo_race()
    demo_phased_computation()


if __name__ == "__main__":
    print("=" * 55)
    print("Topic 10: Thread Synchronization with a Barrier")
    print("=" * 55)
    main()
