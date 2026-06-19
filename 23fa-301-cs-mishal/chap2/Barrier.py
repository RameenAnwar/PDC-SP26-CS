# Import randrange to generate random numbers
from random import randrange
# Import Barrier and Thread from threading module
from threading import Barrier, Thread
# Import ctime to show current time and sleep to pause threads
from time import ctime, sleep


# Total number of runners/threads
num_runners = 3

# Create a barrier that waits for all 3 runners to arrive
finish_line = Barrier(num_runners)
# List of runner names
runners = ['Huey', 'Dewey', 'Louie']
# Function that each thread will run
def runner():
     # Take one runner name from the list
    name = runners.pop()
      # Sleep for random time between 2 and 4 seconds
    sleep(randrange(2, 5))
     # Print when this runner reaches the barrier
    print('%s reached the barrier at: %s \n' % (name, ctime()))
     # Wait here until all runners reach the barrier
    finish_line.wait()
#main func
def main():
      # List to store thread objects
    threads = []
     # Print race start message
    print('START RACE!!!!')
        # Create and start threads for all runners
    for i in range(num_runners):

        threads.append(Thread(target=runner))
        threads[-1].start()
      # Wait for all threads to finish    
    for thread in threads:
        thread.join()
         # Print race end message
    print('Race over!')
# Ensure program runs only when file is executed directly
if __name__ == "__main__":
    main()


    #This code demonstrates the use of a Barrier in multithreading in Python. 
    # It creates three runner threads, each representing a runner with a random delay before reaching a common point called the barrier.
    #  When a runner reaches the barrier, it prints its name and arrival time, then waits there.
    #  The Barrier ensures that all threads must arrive before any of them can continue,
    #  simulating a race where all runners must reach the finish line before the race is considered over.
    #  Finally, the program waits for all threads to complete and prints "Race over!".


#     output
#     START RACE!!!!
# Louie reached the barrier at: Sat Apr  4 18:14:55 2026 

# Huey reached the barrier at: Sat Apr  4 18:14:56 2026 

# Dewey reached the barrier at: Sat Apr  4 18:14:57 2026 

# Race over!
