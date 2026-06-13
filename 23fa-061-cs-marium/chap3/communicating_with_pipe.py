## Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing 
 
 
def create_items(pipe):
    # Get the sending end of the pipe, ignore the receiving end
    output_pipe, _ = pipe
    
    # Loop through numbers 0 to 9 and send each one through the pipe
    for item in range(10):
        output_pipe.send(item)
    
    # Close the pipe when done so receiver knows no more data is coming
    output_pipe.close()
 
def multiply_items(pipe_1, pipe_2):
    # From first pipe, we only need the receiving end to get numbers
    close, input_pipe = pipe_1
    close.close()  # Don't need this end, so close it immediately
    
    # From second pipe, we only need the sending end to output results
    output_pipe, _ = pipe_2
    
    try:
        # Keep receiving numbers until pipe is closed (EOFError occurs)
        while True:
            item = input_pipe.recv()      # Get a number from first pipe
            output_pipe.send(item * item) # Send its square through second pipe
    except EOFError:
        # When input pipe closes, just close the output pipe and exit
        output_pipe.close()
 
 
if __name__== '__main__':

# First process pipe will send numbers from 0 to 9
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = \
                   multiprocessing.Process\
                   (target=create_items, args=(pipe_1,))
    process_pipe_1.start()

# Second pipe will receive squares and send them to main process
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
                   multiprocessing.Process\
                   (target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()
 
    # Close the sending ends in main process because we won't use them
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        # Keep receiving and printing squared numbers from pipe_2
        while True:
            print (pipe_2[1].recv())
    except EOFError:
        # Print "End" when all numbers have been received
        print ("End")