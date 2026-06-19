import threading  # To use threads

def my_func(thread_number):
    # Function executed by each thread
    print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []  # List to store thread objects
    for i in range(10):  # Create 10 threads
        t = threading.Thread(target=my_func, args=(i,))  # Create a thread with argument
        threads.append(t)  # Add thread to the list
        t.start()  # Start the thread
        t.join()  # Wait for the thread to finish before starting next

if __name__ == "__main__":
    main()  # Run the main function