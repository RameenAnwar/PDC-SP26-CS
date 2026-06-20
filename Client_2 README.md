Python Socket File Transfer (Client):
A Python script demonstrating how to create a TCP client that connects to a server, sends an initial greeting, and downloads a file over the network by receiving data in continuous chunks.

Prerequisites:
Python version: 3.x
No external libraries are required as `socket` is part of the Python Standard Library.

How to Run:
Because this is a client script, it requires an active server listening on port `60000` to successfully connect and receive the file.

Step 1: Start your server
Ensure your companion server script is running in a separate terminal and ready to send a file.

Step 2: Run the client
Open a new terminal window and execute the script:
bash
python client2.py

What it Does:
This script acts as the file receiver in a client-server architecture:

1. Connection setup: `socket.socket()` creates a default TCP/IPv4 socket. It resolves the local machine's hostname and connects to port `60000`.
2. Initial Handshake: `s.send('HelloServer!'.encode())` sends a quick greeting to the server. The `.encode()` method converts the Python string into raw bytes so it can be transmitted over the network.
3. File Reception Loop: It creates a local file named `received.txt` in binary write mode (`'wb'`).
It enters an infinite `while True` loop, waiting to receive data chunks up to 1024 bytes at a time (`s.recv(1024)`).
It writes each incoming raw byte chunk directly to `received.txt`.
4. Termination: The loop breaks automatically when `s.recv()` returns an empty byte string (`if not data:`), which happens when the server finishes sending the file and closes its end of the connection. Finally, it safely closes the local file and socket.

Important Code Observations:
Decoding Binary Data: Inside the `while` loop, the script prints `data.decode()`. This works perfectly if the server is sending plain text. However, if the server sends a non-text binary file (like a `.jpg` or `.pdf` image), `.decode()` will throw a `UnicodeDecodeError` because the raw bytes cannot be converted into readable text. If you plan to transfer images or zips, remove the `print ('Data=>', data.decode())` line!
Redundant File Close: The script uses `with open(...) as f:`. This acts as a context manager, meaning the file is automatically closed as soon as the `with` block ends. The explicit `f.close()` right after the block is redundant and can safely be removed.

Expected Output:
If connected to a server sending a text file containing "File transfer complete", the terminal output will look like this:
file opened
receiving data...
Data=> File transfer complete
receiving data...
Successfully get the file
connection closed
Successfully get the file
connection closed

```
