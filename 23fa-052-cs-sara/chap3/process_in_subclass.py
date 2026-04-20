import multiprocessing  # For creating processes

# CUSTOM PROCESS CLASS - Inherits from multiprocessing.Process
class MyProcess(multiprocessing.Process):
    
    # run() method executes when process starts
    def run(self):
        # Print the name of the current process
        print ('called run method in %s' %self.name)
        return  # Function ends

# MAIN PROGRAM
if __name__ == '__main__':
    # Create and run 10 processes one by one
    for i in range(10):  # Loop 10 times (0 to 9)
        process = MyProcess()  # Create a new process object
        process.start()        # Start the process (calls run())
        process.join()         # Wait for this process to finish before next one