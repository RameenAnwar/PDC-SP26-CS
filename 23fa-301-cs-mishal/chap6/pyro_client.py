# Import the Pyro4 library for distributed object communication (RPC)
import Pyro4

# Prompt the user to enter their name, strip any leading/trailing whitespace
# (Original commented line was for URI input, but now using name server lookup)
name = input("What is your name? ").strip()

# Create a Pyro4 proxy to the remote object registered as "server" in the name server
# This automatically looks up the URI from the Pyro4 naming service
server = Pyro4.Proxy("PYRONAME:server")

# Call the remote method 'welcomeMessage' on the server object, passing the user's name
# Print the returned welcome message
print(server.welcomeMessage(name))

#ouput
# What is your name? Mishal
# Hi welcome Mishal