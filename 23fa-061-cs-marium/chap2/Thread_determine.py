import threading  # To use threads
import time  # To add delays

def function_A():
    print(threading.currentThread().getName() + '--> starting \n')  # Show thread starting
    time.sleep(2)  # Simulate work by sleeping for 2 seconds
    print(threading.currentThread().getName() + '--> exiting \n')  # Show thread exiting
    return

def function_B():
    print(threading.currentThread().getName() + '--> starting \n')  # Show thread starting
    time.sleep(2)  # Simulate work
    print(threading.currentThread().getName() + '--> exiting \n')  # Show thread exiting
    return

def function_C():
    print(threading.currentThread().getName() + '--> starting \n')  # Show thread starting
    time.sleep(2)  # Simulate work
    print(threading.currentThread().getName() + '--> exiting \n')  # Show thread exiting
    return

if __name__ == "__main__":
    # Create threads with names
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C) 

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    t3.join()