import threading  # For creating and managing threads
import time       # For adding delays (sleep)

def function_A():
    """Function that runs in Thread A"""
    # Get the name of current thread and print with "starting" message
    print(threading.currentThread().getName() + str('--> starting \n'))
    
    time.sleep(2)  # Pause for 2 seconds (simulate work)
    
    # Print exit message with thread name
    print(threading.currentThread().getName() + str('--> exiting \n'))
    return

def function_B():
    """Function that runs in Thread B"""
    print(threading.currentThread().getName() + str('--> starting \n'))
    time.sleep(2)  # Pause for 2 seconds
    print(threading.currentThread().getName() + str('--> exiting \n'))
    return

def function_C():
    """Function that runs in Thread C"""
    print(threading.currentThread().getName() + str('--> starting \n'))
    time.sleep(2)  # Pause for 2 seconds
    print(threading.currentThread().getName() + str('--> exiting \n'))
    return


if __name__ == "__main__":
    # Create 3 threads with custom names
    t1 = threading.Thread(name='function_A', target=function_A)  # Thread A
    t2 = threading.Thread(name='function_B', target=function_B)  # Thread B
    t3 = threading.Thread(name='function_C', target=function_C)  # Thread C

    # Start all 3 threads (they run at the SAME time!)
    t1.start()  # Start thread A
    t2.start()  # Start thread B (doesn't wait for A)
    t3.start()  # Start thread C (doesn't wait for A or B)

    # Wait for ALL threads to finish before continuing
    t1.join()   # Wait for thread A to finish
    t2.join()   # Wait for thread B to finish
    t3.join()   # Wait for thread C to finish

    # Program ends here after all threads are done