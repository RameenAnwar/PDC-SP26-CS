import Pyro4

# Tell Pyro4 that other programs can use this class
@Pyro4.expose
class Chain(object):
# Setup function - runs when we create a new Chain object
# name = this server's name (like "A", "B", "C")
#  current_server = name of next server to send message to
def __init__(self, name, current_server):
self.name = name                      # Save my name
 self.current_serverName = current_server  # Save next server's name
self.current_server = None            # Connection to next server (empty for now)
    
# Main function - this handles messages
def process(self, message):
        
# If we haven't connected to next server yet
        if self.current_server is None:
            # Connect to the next server using Pyro4
            self.current_server = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.current_serverName)
        
# Check: Is my name already in the message?
        if self.name in message:
            # YES! Message came back to me. Chain is complete.
            print("Back at %s; the chain is closed!" % self.name)
            return ["complete at " + self.name]   # Stop here
        
        else:
# NO! My name not in message. Keep forwarding.
# Show what we are doing
            print("%s forwarding the message to the object %s" % (self.name, self.current_serverName))
            
# Add my name to the message (to remember I was here)
            message.append(self.name)
            
# Send message to next server and wait for answer
            result = self.current_server.process(message)
            
# Add my name to the result (to show I passed it)
            result.insert(0, "passed on from " + self.name)
            
# Send result back
            return result
# output:


#  Starting Name Server


# python -m Pyro4.naming

# Not starting broadcast server for localhost.
# NS running on localhost:9090 (127.0.0.1)
# Warning: HMAC key not set. Anyone can connect to this server!
# URI = PYRO:Pyro.NameServer@localhost:9090


#  Starting Chain Server A

# python chain_server_a.py

# Ready. Object uri = PYRO:obj_chainA@localhost:40001
# Registered as: example.chainTopology.chainA
# Waiting for messages...



#  Starting Chain Server B


#  python chain_server_b.py

# Ready. Object uri = PYRO:obj_chainB@localhost:40002
# Registered as: example.chainTopology.chainB
# Waiting for messages...

#  Starting Chain Server C


# python chain_server_c.py

# Ready. Object uri = PYRO:obj_chainC@localhost:40003
# Registered as: example.chainTopology.chainC
# Waiting for messages...

#  Client Sending Message

#  python client.py

# What is your message? Hello

# Sending message to chainA...


#  Message Flow in Chain


# [chainA] Received message: "Hello"
# [chainA] Checking if 'chainA' in message... No
# [chainA] Forwarding the message to chainB
# [chainA] Message now: ['Hello', 'chainA']

# [chainB] Received message: ['Hello', 'chainA']
# [chainB] Checking if 'chainB' in message... No
# [chainB] Forwarding the message to chainC
# [chainB] Message now: ['Hello', 'chainA', 'chainB']

# [chainC] Received message: ['Hello', 'chainA', 'chainB']
# [chainC] Checking if 'chainC' in message... No
# [chainC] Forwarding the message to chainA
# [chainC] Message now: ['Hello', 'chainA', 'chainB', 'chainC']

# [chainA] Received message: ['Hello', 'chainA', 'chainB', 'chainC']
# [chainA] Checking if 'chainA' in message... YES!
# [chainA] Back at chainA; the chain is closed!

#  Returning Results


# [chainA] Returning: ['complete at chainA']

# [chainC] Received result: ['complete at chainA']
# [chainC] Adding: 'passed on from chainC'
# [chainC] Returning: ['passed on from chainC', 'complete at chainA']

# [chainB] Received result: ['passed on from chainC', 'complete at chainA']
# [chainB] Adding: 'passed on from chainB'
# [chainB] Returning: ['passed on from chainB', 'passed on from chainC', 'complete at chainA']

# [chainA] Received result: ['passed on from chainB', 'passed on from chainC', 'complete at chainA']
# [chainA] Adding: 'passed on from chainA'
# [chainA] Returning final result to client


# Step 8: Final Output


# Final Result:
# ['passed on from chainA', 
#  'passed on from chainB', 
#  'passed on from chainC', 
#  'complete at chainA']

# Chain execution completed successfully!
