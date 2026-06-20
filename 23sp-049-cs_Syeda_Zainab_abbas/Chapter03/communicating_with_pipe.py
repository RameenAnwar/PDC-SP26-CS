# communicating_with_pipe.py
# IPC using a PIPE. A pipe has two ends. Process 1 sends numbers 0..9 into pipe_1.
# Process 2 reads them from pipe_1, squares them, and sends results into pipe_2.
# The main process then reads the squared results from pipe_2.

import multiprocessing

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)        # send 0..9 into the pipe
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()  # receive a number from pipe_1
            output_pipe.send(item * item)   # send its square into pipe_2
    except EOFError:                  # raised when the other end is closed
        output_pipe.close()

if __name__ == '__main__':
    # First pipe carries numbers 0..9
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    # Second pipe carries the squared results
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())   # print each squared result: 0,1,4,9,...,81
    except EOFError:
        print("End")
