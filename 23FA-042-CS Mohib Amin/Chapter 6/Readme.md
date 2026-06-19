
CHAPTER 6

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: addTask.py

## Description
This script sets up a basic background worker using the Celery distributed task queue. It links up with a local message broker and registers a straightforward function that adds two numbers together, using a special decorator so the function can be picked up and processed outside of your main application thread.

## When to Execute
Run using "celery -A addTask worker --loglevel=info".
Execute this file when you need to stand up a background worker node that listens to a message broker for incoming, offloaded execution requests.

## What We Learned
- Importing the Celery library and setting it up to talk to a local broker using an AMQP connection string.
- Wrapping standard Python functions with the @app.task decorator to flip them into asynchronous background jobs.
- Building a standalone task module that can be easily pulled into separate client scripts to trigger work remotely.

## Advantages
- Safely moves heavy or time-consuming math away from your main script, keeping your primary user interface snappy and responsive.
- Makes scaling incredibly simple since you can spin up multiple identical workers across different machines to drain the exact same queue.
- Includes built-in stability features to handle task retries and connection drops automatically if a worker goes offline.

## Disadvantages
- Adds a fair amount of structural complexity since you have to run and look after a separate message broker like RabbitMQ.
- Debugging can be a bit of a headache because print statements and errors pop up inside the worker's log rather than your client terminal.
- Forces you to be careful with inputs, as complex or non-serializable objects can't be encoded to travel over the message broker network.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: addTask_main.py

## Description
This is a simple launcher script that acts as the client-side trigger for the Celery task. 
Instead of running the addition math locally on the original machine, it imports the task module and dispatches the numbers out to the background queue to be handled somewhere else.

## When to Execute
Run using "python addTask_main.py".
Execute this script to test the message broker connection and verify that the client can successfully dispatch background jobs to an active worker.

## What We Learned
- Importing a task file and utilizing the .delay() method to ship a function call out to a message broker instead of running it inline.
- Seeing how a client script instantly regains control of its timeline right after throwing a job over the fence.
- Grabbing a task result reference that lets you check back in later on the job's progress or pull down the final answer.

## Advantages
- Completely non-blocking, meaning your client script can fire off tons of requests in a few milliseconds without waiting for any of them to finish.
- The coding changes are minimal and intuitive since triggering a background job looks almost exactly like calling a regular function.
- Keeps your project organization incredibly clean by dividing your work into a lightweight frontend and a hardworking backend worker.

## Disadvantages
- It completely assumes a worker is actually awake and listening; if no workers are online, your script won't error out, but your tasks will sit in the queue forever.
- Local testing requires a bit of screen juggling since you have to keep separate terminal windows open for the broker, the worker, and the client.
- You don't get the return value back instantly, so you have to write extra tracking logic if your next step depends entirely on that data.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: pyro_server.py

## Description
This program uses the Pyro4 library to spin up a Remote Method Invocation (RMI) server. It defines a class with a simple greeting method, marks it for network exposure, registers it with a central name server, and opens up a continuous listener loop so remote clients can call its functions over a network socket.

## When to Execute
Run using "python pyro_server.py". *(Note: A Pyro name server must be running in the background via "pyro4-ns" before starting this script).*
Execute this file to launch a distributed service node that waits for remote clients to connect and call its internal methods over the network.

## What We Learned
- Exposing specific Python classes and their methods to the network using the @Pyro4.expose decorator.
- Setting up a network daemon with Pyro4.Daemon() and finding an active naming directory via Pyro4.locateNS().
- Binding an object to a specific string key in the registry and keeping the server alive using daemon.requestLoop().

## Advantages
- Bridges the gap between machines seamlessly, letting you write normal object-oriented code while the library hides all the messy socket handling under the hood.
- The built-in naming registry allows your server to switch IP addresses or ports without forcing clients to rewrite their connection strings.
- Excellent foundation for building microservices or multi-node tools where distinct scripts need to call each other's logic over a network.

## Disadvantages
- Creates a single point of failure; if the central naming directory crashes or loses connection, your entire network setup loses the ability to talk.
- Highly vulnerable out of the box if thrown onto public networks without configuring custom firewalls, encryption keys, or access controls.
- Requires tight control over your environments, as version mismatches between Python or Pyro libraries on different machines can instantly break connections.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: pyro_client.py

## Description
This script handles the client side of your Pyro4 connection. 
It asks you to type in a name, uses a text identifier to look up the remote server object from the naming directory, creates a proxy handle, and runs the remote welcome message as if it were running right on your own machine.

## When to Execute
Run using "python pyro_client.py".
Execute this program to verify your network routing, check object lookups against your active name server, and confirm you can pull back responses from your running server.

## What We Learned
- Creating a remote connection handle by passing a registered text name straight into the Pyro4.Proxy constructor.
- Triggering functions over a network socket while letting the library automatically handle the data translation behind the scenes.
- Grabbing and displaying string data returned directly by a separate process running somewhere else on the network.

## Advantages
- Saves you from writing hundreds of lines of low-level networking boilerplate like HTTP headers, payload parsers, or custom socket wrappers.
- Makes client setups incredibly flexible since you only need to know the logical name of a service rather than hardcoding strict IP addresses.
- Transparent syntax keeps your client-side scripts looking like clean, standard Python, which makes it very easy to read and maintain.

## Disadvantages
- Adds network latency to your applications because every single method execution has to take a trip over a network cable instead of running in local RAM.
- If the remote server hits a snag or drops its connection mid-call, your client code will freeze or throw a messy traceback exception.
- You can't pass complex or custom object types across the wire without manually configuring serialization rules, or the proxy link will break.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: chainTopology.py

## Description
This module provides the core blueprint for a multi-stage distributed pipeline where tasks get passed down a chain of servers. It defines a processing class that initializes tracking names, builds network proxies on the fly, logs routing paths, and passes messages forward while ensuring a message doesn't get trapped in an infinite loop.

## When to Execute
Do not run this script directly.
Keep this module in the same directory as your server chain scripts so they can import the core message routing class definitions properly.

## What We Learned
- Designing an interconnected workflow where individual objects track both their own identity and their downstream neighbor's name.
- Creating on-demand remote connections dynamically by assembling proxy names inside an active function block.
- Tracking message history in an array to detect when data has made a full circle, letting you close the chain gracefully.

## Advantages
- Perfect for building structured pipelines like token-passing systems, sequential workflow approvals, or circular ring networks.
- Incredibly low memory overhead since individual servers only need to know about their immediate neighbor rather than keeping a map of the entire grid.
- Highly customizable layout allows you to reorganize your entire processing order just by changing the text parameters passed at startup.

## Disadvantages
- The pipeline is highly fragile; if a single middle server goes down or lags out, the entire chain breaks and messages get stuck mid-transit.
- Tracing errors can turn into a massive headache because a single request hops across completely separate processes and multiple terminal windows.
- Risk of causing silent failures or memory spikes if your loop-detection conditions aren't perfect and a message starts bouncing endlessly between servers.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: server_chain_1.py

## Description
This script sets up the first link (Server 1) in your circular distributed network. It pulls in your topology blueprint, builds a chain object configured to target Server 2 as its downstream neighbor, registers itself with the name server, and starts listening for incoming client requests.

## When to Execute
Run using "python server_chain_1.py". *(Note: Ensure your Pyro name server is up and that server_chain_2 and server_chain_3 are launched alongside it).*
Execute this file to establish the first foundational hop of your distributed circular network topology.

## What We Learned
- Instantiating a custom topology object with explicit tracking variables for the current location and the next hop destination.
- Formatting organized object names in the registry using structured string paths like 'example.chainTopology.1'.
- Launching an independent service daemon and putting it into an active request loop to keep it awake and responsive.

## Advantages
- Establishes a rock-solid, predictable entry point for clients looking to drop data into your multi-stage pipeline.
- Leverages a shared topology module, which keeps your individual server scripts incredibly small, readable, and simple.
- Operates independently, allowing you to reboot or adjust this specific hop without needing to change any code on the other servers.

## Disadvantages
- Requires a strict and orderly startup sequence; launching this before your name server is up will cause an immediate crash.
- Hardcoded string values for the current and next server IDs mean you can't dynamically scale or reroute the pipeline at runtime.
- Consumes a full terminal session or process slot just to handle a single step of your overall distributed network logic.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: server_chain_2.py

## Description
This script handles the intermediate bridge (Server 2) of your network pipeline. It mirrors the exact same setup structure as the first link but alters its startup parameters so that it registers under its own name and points its downstream forwarding target toward Server 3.

## When to Execute
Run using "python server_chain_2.py".
Execute this script alongside your other chain files to complete the intermediate transit routing needed for your distributed network.

## What We Learned
- Replicating multi-process network nodes by running identical class logic with shifted arguments across separate script files.
- Registering completely separate service objects under a unified naming directory without causing name collisions.
- Observing how data travels smoothly through a middle transit layer without requiring any extra input or guidance from the original client.

## Advantages
- Acts as a true decoupled relay station, passing messages anonymously down the line without needing any direct link to the original client.
- Provides an excellent point to inject custom mid-stage processing, validation checks, or data formatting without cluttering your other nodes.
- Isolates your endpoints beautifully, ensuring that Server 1 and Server 3 never have to connect to or know about each other directly.

## Disadvantages
- Increases the moving parts of your system infrastructure, leaving you with another active background listener that must be monitored.
- If this specific script drops offline or encounters an error, your pipeline is cleanly cut in half, stranding any data sent from the front.
- Hard to profile accurately because diagnosing a slowdown requires figuring out if the bottleneck is local code or network transit lag.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: server_chain_3.py

## Description
This script rounds out your distributed ring by standing up the final link (Server 3). It configures itself as the third stage and loops the entire pipeline back around by pointing its downstream target right back at Server 1, establishing a closed, circular network.

## When to Execute
Run using "python server_chain_3.py".
Execute this file to close your distributed network loop, enabling full circular message passing across your architecture.

## What We Learned
- Closing a distributed network ring by pointing the final hop's target back to the initial entry point of the pipeline.
- Seeing firsthand how a circular network handles termination once an incoming message realizes it has hit its starting node.
- Managing a multi-node ecosystem on a single name server to verify that circular object proxies link up without hitches.

## Advantages
- Creates a complete, self-contained loop that lets messages cycle continuously through your processing states until explicit exit criteria are triggered.
- Keeps your architectural design flexible, making it easy to add a Server 4 or 5 later by just adjusting the target parameters.
- Guarantees that any node in the circle can confidently forward data along without needing to manage the ultimate endpoint itself.

## Disadvantages
- High risk of creating a runaway message loop that can spam your network and peg your CPU if your exit-check logic ever fails.
- Demands highly meticulous management of your configuration variables; mixing up an ID string will break the link or send data into a dead end.
- Managing and cleaning up your local workspace gets clunky since shutting down the workflow requires tracking down and killing three separate servers.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: client_chain.py

## Description
This script is the spark plug that sets your entire multi-server ring into motion. It hooks into the central naming directory, requests a proxy connection to Server 1, and drops an initial test message into the pipeline, waiting patiently while the data travels through the full circle and prints out the final path.

## When to Execute
Run using "python client_chain.py". *(Note: All three server chain nodes and the central naming service must be completely active before running this).*
Execute this file from your control terminal to send a test message through your distributed circular pipeline and trace its path.

## What We Learned
- Kicking off a multi-hop, distributed pipeline workflow by interacting directly with a single entry-point node.
- Passing data arrays across a network proxy to collect a historical log of every single distributed node that handled the data.
- Understanding blocking client behavior where your main script waits for a message to complete a multi-server journey before continuing.

## Advantages
- Provides a clean and simple user entry point that hides the messy infrastructure of your multi-server backend from the end user.
- Gathers a clean, readable history trace, which makes it incredibly simple to verify that your data actually hit every server in the intended order.
- Complete separation of concerns; the client script only ever needs to know how to connect to Server 1, keeping it completely decoupled from the rest of the ring.

## Disadvantages
- Faces an elevated risk of hanging or freezing up because it has to sit and wait for a multi-hop network trip to resolve before unblocking.
- Error handling is complex; if Server 2 or 3 crashes mid-run, your client gets a generic proxy error that makes it hard to see which specific node failed.
- Highly vulnerable to socket timeouts, as an unexpected delay or heavy processing load on any of the hops can cause the client link to drop prematurely.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: server.py

## Description
This script sets up a basic TCP server using Python's built-in socket library. It binds to port 9999 on the local machine, listens for incoming connections, and handles up to 5 requests in its queue. Whenever a client connects, it fetches the current system time, formats it as a string, sends it over the socket connection, and immediately closes the link.

## When to Execute
Run using "python server.py".
Execute this file when you need to start a persistent backend listener that provides timestamp data to connecting clients.

## What We Learned
- Initializing an AF_INET, SOCK_STREAM socket to configure a standard TCP network connection.
- Binding a script to a specific host and port registry, and utilizing the listen() method to handle an incoming connection queue.
- Employing a continuous while loop paired with accept() to seamlessly accept client requests and dispatch encoded data dynamically.

## Advantages
- Extremely lightweight with zero external dependencies, making it easy to run on any machine with standard Python installed.
- Clear structural simplicity that keeps network connections highly predictable and isolated from complex application layers.
- Uses standard, non-blocking response workflows by closing individual sockets immediately after the necessary data is pushed out.

## Disadvantages
- Runs on a single-threaded blocking model, meaning it can only process one client handshake at a time, which can limit performance under load.
- Lacks built-in encryption or security protocols out of the box, exposing transmitted data to potential network interception.
- Bound directly to local hostname resolutions, requiring manual environment updates if moving across separate network subnets.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: client.py

## Description
This script implements a direct TCP client designed to pair with the time server. It establishes a connection to port 9999 on the local machine, waits to receive an incoming stream up to 1024 bytes, decodes the received ASCII timestamp payload, and prints the result to the console before exiting cleanly.

## When to Execute
Run using "python client.py".
Execute this file to verify that your basic socket server is running properly and that you can parse network text payloads without connection drops.

## What We Learned
- Instantiating a matching TCP socket object to establish outbound handshakes over a targeted network interface.
- Using the connect() method to actively route traffic to a specific port and handle host translations.
- Reading buffered network streams with recv() and safely handling character decoding to convert raw bytes back into readable strings.

## Advantages
- Highly efficient execution path that performs its specific network query and instantly returns system memory to the OS.
- Simple, straightforward design makes it a solid diagnostic tool for testing local socket bindings and firewall configurations.
- Transparent buffer handling helps prevent memory spikes by setting explicit limits on data chunks pulled from the socket.

## Disadvantages
- Exception handling is entirely manual; if the targeted server is down, the client will immediately crash with a connection refused error.
- Completely reliant on a hardcoded byte window, which can cause data truncation if the incoming payload grows larger than 1024 bytes.
- Lacks automated retry or timeout logic, creating risks where the process could hang indefinitely if the network drops mid-transit.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: server2.py

## Description
This script creates a robust file-transfer server using standard TCP sockets. It binds to port 60000, opens a high-capacity listener queue, and waits for a client handshake. Once connected, it reads a handshake message, opens a local file named 'mytext.txt' in binary mode, and streams its content out to the client in 1024-byte chunks before appending a confirmation footer.

## When to Execute
Run using "python server2.py". *(Note: A file named "mytext.txt" must exist in the same directory for this script to read from).*
Execute this script to establish a dedicated data service node capable of delivering file assets over local network sockets.

## What We Learned
- Tuning socket configurations to support larger connection backlogs via higher listen limits.
- Merging low-level network streaming loops with local disk I/O routines to handle binary data transmission securely.
- Constructing sequenced network protocols where raw file chunks are systematically followed by clear termination headers.

## Advantages
- Handles files using binary streams , ensuring that formatting, special characters, or non-text assets don't get corrupted in transit.
- Segmented buffer loops keep memory usage low, as it only loads and pushes 1024 bytes at a time rather than caching whole files into RAM.
- Provides immediate console feedback for each transaction step, making it much easier to track connections and file states.

## Disadvantages
- The script opens and closes file handles directly inside its network execution loops, which can lead to silent failures if multiple processes compete for the asset.
- Uses basic blocking sockets that stall the server's primary loop until a client finishes downloading the current file stream.
- The pathing is tightly bound to a hardcoded filename string, preventing clients from requesting different files dynamically.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: client2.py

## Description
This script handles the matching client utility for the file transfer architecture. It connects to port 60000, fires off an initial handshake string to notify the server, and sets up a local file named 'received.txt' in binary write mode. It then enters a processing loop that captures incoming data blocks, commits them directly to disk, and closes down once the stream finishes.

## When to Execute
Run using "python client2.py".
Execute this file to download assets from your running file-transfer server and confirm that binary payloads are correctly written locally.

## What We Learned
- Initializing direct socket uploads by sending structured text strings immediately after a network handshake succeeds.
- Designing a continuous data drain loop that dynamically detects stream termination when recv() returns empty payloads.
- Managing local file writes in binary append mode to cleanly reconstruct segmented network data into a single file on disk.

## Advantages
- Writing files incrementally avoids massive memory footprints, allowing the client to pull down large text logs or assets smoothly.
- Automated termination checks keep the runtime predictable, safely wrapping up local write operations as soon as the server closes the channel.
- Completely isolates the target filename ('received.txt') from the server's layout, keeping your local workspace organized.

## Disadvantages
- If a file named 'received.txt' already exists in the execution directory, this script will overwrite it completely without warning or confirmation.
- The decoding logs assume incoming data is pure text format, which can trigger parsing errors if you adapt the server to stream actual binary media.
- Does not verify file integrity, meaning a dropped packet or interrupted network connection can result in a partial download without any error flags.