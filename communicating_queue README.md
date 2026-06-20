Producer–Consumer with Multiprocessing 

Overview:
This program uses Python `multiprocessing` with a Queue:

How It Works:

1. Producer Process
Generates 10 random numbers (0–256)
Adds them to the queue
Prints:
The produced item
Current queue size
Waits 1 second between each item
2. Consumer Process
Continuously checks the queue
If not empty:
Removes (consumes) an item
Prints the consumed item
If empty:
Stops execution
Producer adds random numbers to the queue
Consumer removes and prints them

Important Notes:

multiprocessing.Queue() is used for safe data sharing between processes
Producer and Consumer run independently
time.sleep() is used to simulate processing delay
queue.empty() may not always be reliable in real-world applications
