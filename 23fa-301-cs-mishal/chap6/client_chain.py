# Import the print_function from __future__ to enable Python 3 style print()
# (Ensures print() works consistently across Python versions)
from __future__ import print_function

# Import the entire Pyro4 module for remote object communication
import Pyro4

# Create a proxy object that connects to a remote Pyro4 object
# The proxy is identified by the name "example.chainTopology.1" registered in the Pyro4 name server
# This proxy acts as a local representative for the remote Chain object (first node)
obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")

# Call the 'process' method on the remote object asynchronously (blocking call)
# Pass a list containing the initial message ["hello"] as argument
# The remote object will process the message through the chain and return a result
# Print the returned result (should be a list with trace of nodes and completion message)
print("Result=%s" % obj.process(["hello"]))


#output
# Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']