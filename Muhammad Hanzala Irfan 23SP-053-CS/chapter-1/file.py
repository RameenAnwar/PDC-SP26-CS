# file.py

# Writing to a file
file = open("sample.txt", "w")
file.write("Welcome to Python File Handling")
file.close()

# Reading from a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()