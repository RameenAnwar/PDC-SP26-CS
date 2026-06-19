##Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism
# We import multiprocessing to create separate processes that can run concurrently
# This allows us to:
# 1. Run functions in parallel (create_items and multiply_items run simultaneously)
# 2. Use Pipe() for communication between processes (like a two-way communication channel)
# 3. Create Process objects to spawn new processes
# Without this, Python would run everything in a single process/thread
import multiprocessing 
 
 #purpose: Producer function that generates numbers and sends them through a pipe
def create_items(pipe):
     # pipe is a tuple containing two connection objects: (sending_end, receiving_end)
    # We unpack the tuple - output_pipe gets the sending end, _ ignores the receiving end
    # The underscore (_) is a convention meaning "we don't need this value"
    output_pipe, _ = pipe
     # Loop to generate numbers 0 through 9 
    for item in range(10):
         # .send() serializes the object (using pickle) and writes it to the pipe
        # The receiving process will get this exact object in the same order
        output_pipe.send(item)
     # .close() is CRITICAL - it sends an EOF (End of File) signal
    # Without this, the receiving process would wait forever for more data
    # This triggers EOF Error on the receiving end when all data is consumed    
    output_pipe.close()


 #Purpose: Worker function that reads numbers from first pipe, squares them, sends to second pipe
def multiply_items(pipe_1, pipe_2):
     # pipe_1: from producer process (contains numbers 0-9)
    # Unpack: 'close' gets sending end (which we don't need), input_pipe gets receiving end
    close, input_pipe = pipe_1
    # Close the unused sending end immediately to prevent resource leaks
    # Every process should close pipe ends they don't use to avoid deadlocks
    close.close()
     # pipe_2: to main process (will receive squared numbers)
    # Unpack: output_pipe gets sending end (to send results), _ ignores receiving end
    output_pipe, _ = pipe_2

      # Try-except block to handle when input pipe is closed
    try:
        # Infinite loop - keeps receiving until pipe is closed
        while True:
              # .recv() blocks (waits) until data arrives from pipe_1
            # When pipe_1 is closed and all data is read, raises EOFError
            item = input_pipe.recv()
             # Send the square (item * item) through output_pipe to main process
            output_pipe.send(item * item)
    # Catch the EOFError when create_items closes its pipe
        # This is the signal to stop processing and clean up
        # Close our output pipe to signal main process we're done        
    except EOFError:
        output_pipe.close()
 
 # Main execution block - ONLY runs when script is executed directly
# This prevents code from running if this file is imported as a module
if __name__== '__main__':
# Create first pipe for communication between producer and worker
    # Pipe(True) creates a duplex (two-way) pipe
    # Returns tuple: (connection1, connection2) - both can send AND receive
    # We'll use it one-way though: create_items -> multiply_items
    #First process pipe with numbers from 0 to 9
    pipe_1 = multiprocessing.Pipe(True)

    # Create first process that will run create_items function
    # Process(target=function_name, args=tuple_of_arguments)
    # This doesn't start the process yet, just creates the object
    
    process_pipe_1 = \
                   multiprocessing.Process\
                   (target=create_items, args=(pipe_1,))
    # .start() actually creates a new system process and begins executing create_items
    # The new process gets a copy of pipe_1 (both ends)
    process_pipe_1.start()

#second pipe,
 # Create second pipe for communication between worker and main process
    # This will carry the squared results back to main
    pipe_2 = multiprocessing.Pipe(True)
    # Create second process that will run multiply_items function
    # Pass both pipes: pipe_1 (to read from producer) and pipe_2 (to write results to main)
    process_pipe_2 = \
                   multiprocessing.Process\
                   (target=multiply_items, args=(pipe_1, pipe_2,))
     # Start the worker process - it begins waiting for data from pipe_1
    process_pipe_2.start()
  # In MAIN process, close the sending end of pipe_1 (index 0)
    # Main process doesn't need to send anything through pipe_1
    # Closing unused ends prevents accidental interference and resource waste
    pipe_1[0].close()
    # In MAIN process, close the sending end of pipe_2 (index 0)
    # Main process will only READ from pipe_2, not send anything
    # So close the sending end to prevent accidental writes
    pipe_2[0].close()
 # Try-except to handle when pipe_2 is closed by multiply_items
    try:
          # Infinite loop to keep receiving squared numbers
        while True:
             # .recv() on pipe_2[1] (the receiving end of pipe_2)
            # This blocks until multiply_items sends data or closes the pipe
            # Each call receives one squared number
            print (pipe_2[1].recv())
    except EOFError:
        # When multiply_items closes its sending end of pipe_2
        # After sending all 10 squares, it closes the pipe
        # This causes EOFError on our receiving end
        # Print "End" to indicate completion
        print ("End")


        #Summary of the Code
        # This code demonstrates interprocess communication using pipes in Python's multiprocessing module. It creates a pipeline of three processes:
        # Producer Process (create_items): Generates numbers 0 through 9 and sends them through pipe_1
        # Worker Process (multiply_items): Receives numbers from pipe_1, squares each number, and sends the result through pipe_2
        # Main Process: Receives squared numbers from pipe_2 and prints them


    #     Main Process (PID: 1000)
    # │
    # ├─ creates pipe_1 ────────┐
    # ├─ starts Process 1 (PID: 1001) ──┐
    # │                          │       │
    # │                     runs create_items()
    # │                          │       │
    # │                          └───────┘ sends 0,1,2...9 through pipe_1
    # │                                      │
    # ├─ creates pipe_2 ────────────┐       │
    # ├─ starts Process 2 (PID: 1002) ──────┘
    # │                          │
    # │                     runs multiply_items()
    # │                          │
    # │                          ├─ receives from pipe_1
    # │                          ├─ calculates square
    # │                          └─ sends to pipe_2
    # │                                      │
    # └─ Main reads from pipe_2 ────────────┘
    #        prints: 0, 1, 4, 9...81
    #        prints: "End"



#output
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# End

