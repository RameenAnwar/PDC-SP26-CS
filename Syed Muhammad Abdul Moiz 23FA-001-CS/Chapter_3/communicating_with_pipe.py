import multiprocessing 

def create_items(pipe):
    # Unpack the pipe. We only need the output side here.
    output_pipe, _ = pipe
    # Loop to generate numbers from 0 to 9
    for item in range(10):
        # Send the generated number into the pipe
        output_pipe.send(item)
    # Close the pipe when done sending
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    # Unpack the first pipe (getting the input side)
    close, input_pipe = pipe_1
    # We don't need the close side here, so we close it
    close.close()
    # Unpack the second pipe (getting the output side)
    output_pipe, _ = pipe_2
    try:
        # Keep reading data until there is nothing left
        while True:
            # Receive the item from the first process
            item = input_pipe.recv()
            # Square the item and send it to the second pipe
            output_pipe.send(item * item)
    except EOFError:
        # If no more data is coming, close the output pipe
        output_pipe.close()

if __name__== '__main__':
    # First process pipe with numbers from 0 to 9
    # Create a two-way (duplex) pipe
    pipe_1 = multiprocessing.Pipe(True)
    # Create the first process and give it pipe_1
    process_pipe_1 = \
        multiprocessing.Process\
        (target=create_items, args=(pipe_1,))
    # Start the first process
    process_pipe_1.start()

    # second pipe
    # Create another two-way pipe
    pipe_2 = multiprocessing.Pipe(True)
    # Create the second process and give it both pipes
    process_pipe_2 = \
        multiprocessing.Process\
        (target=multiply_items, args=(pipe_1, pipe_2,))
    # Start the second process
    process_pipe_2.start()

    # Close the ends of the pipes that the main process won't use
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        # Main process reads the final results from pipe_2
        while True:
            # Print the received squared numbers
            print(pipe_2[1].recv())
    except EOFError:
        # Print "End" when all data is read
        print("End")