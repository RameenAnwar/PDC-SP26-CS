# Open the file 'test.txt' in write mode ('w')
# If the file does not exist, it will be created
# If it already exists, its content will be overwritten
f = open('test.txt', 'w')

# Write the first line to the file
# '\n' is used to move to the next line
f.write('first line of file \n')

# Write the second line to the file
f.write('second line of file \n')

# Close the file after writing to save changes
f.close()


# Open the same file again in read mode (default is 'r')
f = open('test.txt')

# Read the entire content of the file and store it in 'content'
content = f.read()

# Print the content of the file
print(content)

# Close the file after reading
f.close()