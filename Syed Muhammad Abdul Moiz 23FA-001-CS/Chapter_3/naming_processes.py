import multiprocessing
import time

def myFunc():
    # Get the name of the process that is running this function right now
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" %name)
    # Sleep for 3 seconds to simulate doing some work
    time.sleep(3)
    print("Exiting process name = %s \n" %name)

if __name__ == '__main__':
    # Create a process and give it a custom specific name
    process_with_name = multiprocessing.Process\
        (name='myFunc process',\
         target=myFunc)

    #process_with_name.daemon = True

    # Create a process but let Python give it a default name (like Process-2)
    process_with_default_name = multiprocessing.Process\
        (target=myFunc)

    # Start both processes
    process_with_name.start()
    process_with_default_name.start()

    # Wait for both processes to finish
    process_with_name.join()
    process_with_default_name.join()