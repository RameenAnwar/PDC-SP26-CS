Python TCP Socket Client:
A minimal Python script demonstrating how to create a basic TCP client using the built-in `socket` library. This specific client connects to a local server, receives a timestamp, and prints it to the console.

Prerequisites:
Python version: 3.x
No external libraries are required as `socket` is part of the Python Standard Library.

How to Run:
Because this is a client-side script, it requires an active server listening on port 9999 to successfully connect.

Step 1: Start your server
Make sure your companion server script is running in its own terminal window.

Step 2: Run the client
Open a new terminal window and execute the client script:
bash
python client.py

What it Does:
This script acts as the receiver in a standard client-server network architecture:
1. Socket Creation: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` initializes a new socket object using IPv4 (`AF_INET`) and TCP (`SOCK_STREAM`).
2. Targeting the Server: It sets the target host to the local machine (`socket.gethostname()`) and designates port `9999`.
3. Connecting: `s.connect((host, port))` attempts to establish a TCP connection with the server.
4. Receiving Data: Once connected, `s.recv(1024)` waits to receive a payload from the server (up to a maximum of 1024 bytes).
5. Teardown & Output: It immediately closes the connection (`s.close()`), decodes the raw bytes received from the server into an ASCII string, and prints the result to your terminal.

Important Code Observations:
If you run this script without a server actively listening on port 9999, the script will crash and throw a `ConnectionRefusedError`. The client can only connect if the server is already up and waiting for connections!

Expected Output:
When successfully connected to a time-broadcasting server, your terminal output will look something like this:
Time connection server: Mon Jun  8 03:33:51 2026
