# Bring in the tools we need
from random import randrange          # For random numbers
from threading import Barrier, Thread # For waiting together and running at same time
from time import ctime, sleep         # For time and delays

# How many runners are racing
num_runners = 3

# Create a finish line that needs ALL 3 runners to arrive before anyone can finish
finish_line = Barrier(num_runners)

# Names of our runners
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    """What each runner does"""
    
    # Take one name from the list
    name = runners.pop()
    
    # Each runner takes random time (2 to 4 seconds) to reach the finish line
    sleep(randrange(2, 5))
    
    # Runner announces they reached the finish line
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    
    # Runner waits here until ALL 3 runners arrive
    finish_line.wait()

def main():
    """Start the race"""
    
    threads = []  # List to store all runners
    print('START RACE!!!!')
    
    # Create and start 3 runner threads (they all run together)
    for i in range(num_runners):
        threads.append(Thread(target=runner))  # Make a runner
        threads[-1].start()                    # Start the runner
    
    # Wait for all runners to finish
    for thread in threads:
        thread.join()
    
    # This prints only after ALL runners have crossed the finish line together
    print('Race over!')

# Run the race
if __name__ == "__main__":
    main()