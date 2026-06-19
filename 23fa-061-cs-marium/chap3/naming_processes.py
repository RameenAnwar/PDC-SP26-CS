
import multiprocessing
import time

# Function that prints process name, sleeps 3 seconds, then prints exit message
def myFunc():
    name = multiprocessing.current_process().name
    print ("Starting process name = %s \n" %name)
    time.sleep(3)
    print ("Exiting process name = %s \n" %name)

if __name__ == '__main__':
    # Create a process with custom name 'myFunc process'
    process_with_name = multiprocessing.Process\
                        (name='myFunc process',\
                         target=myFunc)

    #process_with_name.daemon = True  # Uncomment to make this process a daemon

    # Create another process that will get default name (Process-1, Process-2, etc.)
    process_with_default_name = multiprocessing.Process\
                                (target=myFunc)

    process_with_name.start()  # Start the named process
    process_with_default_name.start()  # Start the default-named process

    process_with_name.join()  # Wait for named process to finish
    process_with_default_name.join()  # Wait for default process to finish