
# If the file does not exist, it will be created
# If the file exists, its content will be overwritten because we opened with the write mode
f = open ('test.txt', 'w')
# Write first line to the file
# '\n' takes to next new line
f.write ('first line of file \n') 
# Write second line to the file
f.write ('second line of file \n') 
# Closing the file to save and reflect changes
f.close()
# Open the file in default read mode 
f = open ('test.txt')
#  Read the entire content of the file and store it in 'content'
content = f.read()
# print the variable
print (content)
# Closing the file after reading
f.close()

# expected ouptut will be 
# first line of file 
# second line of file 