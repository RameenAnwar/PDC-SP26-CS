import multiprocessing

# Create a custom Process class by inheriting from multiprocessing.Process
class MyProcess(multiprocessing.Process):

    # Overwrite the run() method to define what this process will do
    def run(self):
        # Print a message using the auto-generated name of the process
        print('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    # Create and run 10 separate processes one by one
    for i in range(10):
        # Create an object of our custom process class
        process = MyProcess()
        # Start the process (this calls the run() method)
        process.start()
        # Wait for this process to finish before going to the next loop iteration
        process.join()