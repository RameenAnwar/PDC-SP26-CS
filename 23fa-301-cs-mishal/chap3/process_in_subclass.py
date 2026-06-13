# IMPORT STATEMENT COMMENT
# Import multiprocessing module to create and manage processes
# Provides the Process class which we will inherit from
import multiprocessing

# CLASS: MyProcess
# Purpose: Custom process class that inherits from multiprocessing.Process
# Demonstrates how to create process by subclassing instead of using target function
class MyProcess(multiprocessing.Process):
    
    # METHOD: run
    # Purpose: Contains the code that executes when the process starts
    # This OVERRIDES the parent Process class's run method
    # Called automatically when .start() is invoked on the process object
    def run(self):
        # Print a message showing which process is executing
        # self.name is inherited from parent Process class
        # Contains either custom name (if set) or auto-generated name (Process-1, Process-2, etc.)
        print('called run method in %s' % self.name)
        
        # Return from the method (explicit return, though optional)
        # Process ends after this line executes
        return

# MAIN EXECUTION BLOCK
# Runs only when script is executed directly (not imported as module)
if __name__ == '__main__':
    
    # Loop 10 times to create and run 10 separate processes
    # i ranges from 0 to 9 (total of 10 iterations)
    for i in range(10):
        
        # Create an instance of our custom MyProcess class
        # At this point, no system process has been created yet
        # Just a Python object in memory
        process = MyProcess()
        
        # Start the process
        # This does TWO things:
        #   1. Creates a new system process (fork on Unix, spawn on Windows)
        #   2. Calls the .run() method in the NEW process
        # The .start() method returns immediately (non-blocking)
        process.start()
        
        # Wait for THIS process to complete before continuing
        # .join() BLOCKS the main program until this specific process finishes
        # This makes execution SEQUENTIAL despite using multiple processes
        # Each process must finish before the next one starts
        process.join()
        
        # After join() completes, the loop continues to next iteration
        # Next process is created, started, and we wait again




#         SUMMARY OF THE CODE
# What This Code Does:
# This program demonstrates creating custom process classes by subclassing multiprocessing.
# Process and overriding the run() method. It creates 10 processes sequentially (one after another), not in parallel.

# Key Difference from Previous Examples:
# Previous Approach	                   This Approach
# Used Process(target=function)	       Used class MyProcess(Process)
# Function passed as target	           run() method overridden
# Functional programming style	        Object-oriented programming style
# Process logic in separate function	Process logic encapsulated in class
# Process Flow Diagram:
# text
# Main Process
#     │
#     ├─ Iteration 1 (i=0):
#     │   ├─ Create MyProcess object #1
#     │   ├─ process.start() → New Process #1 runs run() method
#     │   │                    └─ Prints: "called run method in Process-1"
#     │   └─ process.join() → Wait for Process #1 to finish
#     │
#     ├─ Iteration 2 (i=1):
#     │   ├─ Create MyProcess object #2
#     │   ├─ process.start() → New Process #2 runs run() method
#     │   │                    └─ Prints: "called run method in Process-2"
#     │   └─ process.join() → Wait for Process #2 to finish
#     │
#     ├─ Iteration 3 (i=2):
#     │   ├─ Create MyProcess object #3
#     │   ├─ process.start() → New Process #3 runs run() method
#     │   │                    └─ Prints: "called run method in Process-3"
#     │   └─ process.join() → Wait for Process #3 to finish
#     │
#     └─ ... continues for iterations 4 through 9 (total 10 processes)

# output

# called run method in MyProcess-1
# called run method in MyProcess-2
# called run method in MyProcess-3
# called run method in MyProcess-4
# called run method in MyProcess-5
# called run method in MyProcess-6
# called run method in MyProcess-7
# called run method in MyProcess-8
# called run method in MyProcess-9
# called run method in MyProcess-10