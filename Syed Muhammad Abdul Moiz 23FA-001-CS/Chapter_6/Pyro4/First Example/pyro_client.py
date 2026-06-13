# Import the Pyro4 library to enable Remote Procedure Calls (RPC) between different Python scripts
import Pyro4

# Prompt the user in the terminal to enter their name, removing any accidental leading or trailing spaces using .strip()
name = input("What is your name? ").strip()

# Create a proxy connection to the remote object using its registered logical name ('server')
# 'PYRONAME:server' tells Pyro4 to automatically look up the server's actual location (URI) from the active Name Server
server = Pyro4.Proxy("PYRONAME:server")    

# Call the 'welcomeMessage' function remotely on the server, passing 'name' as an argument
# The server executes the function on its machine, returns the result, and this line prints that result to the client's console
print(server.welcomeMessage(name))