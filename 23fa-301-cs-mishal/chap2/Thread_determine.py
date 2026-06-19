# Import threading module to work with threads
import threading
# Import time module to introduce delays (simulate work)
import time

# Function A that will be run in a thread
def function_A():
    # Print the name of the current thread and indicate it is starting
    print (threading.currentThread().getName()+str('--> starting \n'))
    # Pause for 2 seconds to simulate work
    time.sleep(2)
    # Print the name of the current thread and indicate it is exiting
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return

# Function B that will be run in a thread
def function_B():
    # Print the name of the current thread and indicate it is starting
    print (threading.currentThread().getName()+str('--> starting \n'))
    # Pause for 2 seconds to simulate work
    time.sleep(2)
    # Print the name of the current thread and indicate it is exiting
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return

# Function C that will be run in a thread
def function_C():
    # Print the name of the current thread and indicate it is starting
    print (threading.currentThread().getName()+str('--> starting \n'))
    # Pause for 2 seconds to simulate work
    time.sleep(2)
    # Print the name of the current thread and indicate it is exiting
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return


# Main block ensures code runs only when executed directly
if __name__ == "__main__":
    # Create a thread t1 with name 'function_A' to run function_A
    t1 = threading.Thread(name='function_A', target=function_A)
    # Create a thread t2 with name 'function_B' to run function_B
    t2 = threading.Thread(name='function_B', target=function_B)
    # Create a thread t3 with name 'function_C' to run function_C
    t3 = threading.Thread(name='function_C', target=function_C) 

    # Start all three threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to complete before exiting main program
    t1.join()
    t2.join()
    t3.join()

    #This code creates three threads, each running a separate function (function_A, function_B, function_C). 
# Each function prints a start message, sleeps for 2 seconds to simulate work, and then prints an exit message. 
# Threads are started almost simultaneously using start(), and the program waits for all threads to finish using join().
#  Because threads run concurrently, their start and exit messages may interleave, depending on thread scheduling.#