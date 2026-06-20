# file.py
# Basic file handling: write two lines to a text file, then read them back.

f = open('test.txt', 'w')            # open in WRITE mode ('w' overwrites existing content)
f.write('first line of file \n')     # \n = newline character
f.write('second line of file \n')
f.close()                            # always close after writing to flush data to disk

f = open('test.txt')                 # open again in default READ mode
content = f.read()                   # read the entire file into a string
print(content)
f.close()
