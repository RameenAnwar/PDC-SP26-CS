from random import randrange  # To generate random numbers for sleep time
from threading import Barrier, Thread  # To use threads and a barrier for synchronization
from time import ctime, sleep  # To get current time and pause execution

num_runners = 3  # Number of runners in the race
finish_line = Barrier(num_runners)  # Barrier to synchronize threads at the finish line
runners = ['Huey', 'Dewey', 'Louie']  # Names of the runners

def runner():
    name = runners.pop()  # Get a runner name from the list
    sleep(randrange(2, 5))  # Simulate running by sleeping random seconds
    print('%s reached the barrier at: %s \n' % (name, ctime()))  # Print when runner reaches barrier
    finish_line.wait()  # Wait for all runners to reach the barrier

def main():
    threads = []  # List to store thread objects
    print('START RACE!!!!')  # Start message
    for i in range(num_runners):
        threads.append(Thread(target=runner))  # Create a new thread for each runner
        threads[-1].start()  # Start the thread
    for thread in threads:
        thread.join()  # Wait for all threads to finish
    print('Race over!')  # Print when race is finished

if __name__ == "__main__":
    main()  # Run the main function