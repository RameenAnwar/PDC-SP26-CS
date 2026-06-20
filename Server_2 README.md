Python Socket File Transfer (Server)
A Python script demonstrating how to create a TCP server that listens for incoming client connections, receives an initial greeting, and transmits a file (`mytext.txt`) over the network in chunks.

Prerequisites:
Python version: 3.x
No external libraries are required as `socket` is part of the Python Standard Library.
Important: You must create a file named `mytext.txt` in the same directory as this script before running it, or the server will crash with a `FileNotFoundError`.

How to Run:
Because this is a server script, it needs to be running in the background before any clients attempt to connect to it.

Step 1: Start the server
Open your terminal and run the script:
bash
python server_sender.py

The server will print "Server listening...." and wait for connections.

Step 2: Connect a client
Use a companion Python client script to connect to port `60000`.

Step 3: Stopping the server
Because the server runs in an infinite `while True:` loop, it will not stop on its own. To shut it down, click into your server terminal and press Ctrl + C.

What it Does:
This script acts as the file host in a client-server architecture:
1. Setup: `socket.socket()` creates a default TCP socket. It binds to the local machine's hostname on port `60000`.
2. Listening: `s.listen(15)` tells the OS to start listening, allowing a queue of up to 15 pending client requests.
3. Accepting & Receiving: It accepts an incoming connection and waits to receive up to 1024 bytes (`conn.recv(1024)`), which it prints to the console.
4. Sending the File: It opens `mytext.txt` in binary read mode (`'rb'`). It reads the file in 1024-byte chunks and sends them to the client using a `while` loop.
5. Teardown: Once the file is fully read, it sends a final thank-you message and closes the connection to that specific client, looping back to wait for the next person.

Important Code Observations (Bug Alert):
If you are using this code in a real project, you must fix the indentation inside the `while (l):` loop.
Currently, `f.close()`, the final `conn.send()`, and `conn.close()` are indented *inside* the loop. If your `mytext.txt` file is larger than 1024 bytes, the script will close the file and the network connection during the very first cycle, causing a fatal error on the second cycle!

How to fix it:
Un-indent those final four lines so they only execute *after* the `while` loop finishes:
python
    while (l):
        conn.send(l)
        print ('Sent',repr(l.decode()))
        l =f.read(1024)
        
    # Un-indent these so they run AFTER the file is fully sent!
    f.close()
    print ('Donesending')
    conn.send('->Thank you for connecting'.encode())
    conn.close()

Note on Binary Files: Inside the loop, it prints `repr(l.decode())`. If you change `mytext.txt` to an image or a zip file, `.decode()` will throw a `UnicodeDecodeError`. If you plan to send non-text files, safely remove the `.decode()` print statements!

Expected Output:
When the server is running and a client successfully connects, your server terminal will log the transfer process:
Server listening....
Got connection from ('192.168.1.10', 54321)
Server received 'HelloServer!'
Sent 'First chunk of the text file...'
Donesending
