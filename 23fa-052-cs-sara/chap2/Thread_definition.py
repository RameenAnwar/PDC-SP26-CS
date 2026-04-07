import threading  # Import threading module to create and manage threads

def my_func(thread_number):
    """Simple function that prints which thread called it"""
    return print('my_func called by thread N°{}'.format(thread_number))
    # Print a message showing the thread number (0 to 9)


def main():
    """Main function that creates and runs threads"""
    threads = []  # Empty list to store thread objects
    
    # Create 10 threads (i goes from 0 to 9)
    for i in range(10):
        # Create a thread that will run my_func and pass i as argument
        t = threading.Thread(target=my_func, args=(i,))
        # target = function to run
        # args = arguments to pass to that function (must be a tuple)
        
        threads.append(t)  # Add thread to list (for reference)
        t.start()          # Start the thread (run my_func)
        t.join()           # Wait for this thread to finish before continuing
        #  This means threads run ONE AT A TIME, not simultaneously!


if __name__ == "__main__":
    main()  # Run the main function