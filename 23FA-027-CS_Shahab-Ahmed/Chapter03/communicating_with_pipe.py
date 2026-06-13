# Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing 

# Function to create items and send them through pipe
def create_items(pipe):
    output_pipe, _ = pipe  # Take the sending end of pipe
    for item in range(10):
        output_pipe.send(item)  # Send numbers 0–9
    output_pipe.close()  # Close pipe after sending


# Function to receive items, process them, and send results
def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1  # Receiving end of first pipe
    close.close()  # Close unused end

    output_pipe, _ = pipe_2  # Sending end of second pipe

    try:
        while True:
            item = input_pipe.recv()  # Receive data
            output_pipe.send(item * item)  # Send squared value
    except EOFError:
        output_pipe.close()  # Close when no more data


if __name__ == '__main__':

    # First pipe: sends numbers 0–9
    pipe_1 = multiprocessing.Pipe(True)

    # First process: generates numbers
    process_pipe_1 = multiprocessing.Process(
        target=create_items, args=(pipe_1,)
    )
    process_pipe_1.start()

    # Second pipe: sends processed data
    pipe_2 = multiprocessing.Pipe(True)

    # Second process: squares numbers
    process_pipe_2 = multiprocessing.Process(
        target=multiply_items, args=(pipe_1, pipe_2,)
    )
    process_pipe_2.start()

    # Close unused pipe ends in main process
    pipe_1[0].close()
    pipe_2[0].close()

    # Receive and print results
    try:
        while True:
            print(pipe_2[1].recv())  # Print squared values
    except EOFError:
        print("End")