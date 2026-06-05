import Pyro4

#uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
name = input("What is your name? ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))
#output:
# C:\Users\LAPTOP LAB\OneDrive - Higher Education Commission\Desktop\Python-Parallel-Programming-Cookbook-Second-Edition/Chapter06\Pyro4> python pyro_client.py

# What is your name? sara
# Hi welcome sara



