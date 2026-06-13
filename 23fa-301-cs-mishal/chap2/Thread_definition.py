# Import threading module for creating threads
import threading


# Function that will be executed by each thread
def my_func(thread_number):
    # Print which thread called this function
    return print('my_func called by thread N°{}'.format(thread_number))


# Main function
def main():
    # List to store thread objects
    threads = []
    
    # Loop to create 10 threads
    for i in range(10):
        # Create a thread and pass current value of i as argument
        t = threading.Thread(target=my_func, args=(i,))
        
        # Add thread object to the list
        threads.append(t)
        
        # Start the thread
        t.start()
        
        # Wait for the current thread to finish before starting next one
        t.join()


# Ensure this code runs only when file is executed directly
if __name__ == "__main__":
    main()

    #This code demonstrates basic thread creation in Python. A function my_func() is defined, which prints the thread number passed to it. 
    # Inside the main() function, a loop creates 10 threads, each assigned a unique number from 0 to 9. Each thread starts and executes the function, 
    # but since join() is called immediately after start() inside the loop, the program waits for each thread to finish before creating the next one. 
    # As a result, the threads execute sequentially instead of concurrently, making this a simple example of thread creation and execution control.


#     output
#     my_func called by thread N°0
# my_func called by thread N°1
# my_func called by thread N°2
# my_func called by thread N°3
# my_func called by thread N°4
# my_func called by thread N°5
# my_func called by thread N°6
# my_func called by thread N°7
# my_func called by thread N°8
# my_func called by thread N°9