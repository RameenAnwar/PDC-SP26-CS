# Import print_function from future module to ensure compatibility across different Python versions
from __future__ import print_function
# Import the Pyro4 library to manage client-side Remote Procedure Calls (RPC)
import Pyro4

# Create a proxy connection to the first node in the chain topology (Node "1")
# 'PYRONAME:...' connects to the Name Server to look up the exact URI location of this starting object
obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")

# Initiate the chain process by calling the remote 'process' method on the target object
# We pass a list containing the starting message ["hello"]. Once the whole chain finishes processing 
# and returns the final tracking list, it will print out the formatted result string.
print("Result=%s" % obj.process(["hello"]))