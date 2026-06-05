# Make print work the same in old and new Python
from __future__ import print_function

# Get Pyro4 tools
import Pyro4

# Connect to the first server in the chain
# Think of it like: "Call this phone number"
obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")

# Send "hello" to the server chain
# Ask it to process the message
# Then print what comes back
print("Result=%s" % obj.process(["hello"]))

# output:

# Server A forwarding the message to the object B
# Server B forwarding the message to the object C
# Server C forwarding the message to the object A
# Back at A; the chain is closed!

# Result=['passed on from A', 'passed on from B', 'passed on from C', 'complete at A']    