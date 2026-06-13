# Open file in write mode (creates file if it doesn't exist)
f = open('test.txt', 'w')

# Write first line into the file
f.write('first line of file \n') 

# Write second line into the file
f.write('second line of file \n') 

f.close()     # Close the file after writing


# Open file again in read mode (default mode is read)
f = open('test.txt')

content = f.read()     # Read full content of file

print(content)     # Display file content

f.close()     # Close the file after reading