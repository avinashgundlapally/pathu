import os

name = input("Enter your Name: ") 

line = input("Enter your line: ")

print(name)
print(line)

filename = name+'.txt'

if os.path.exists(filename):
    append_write = 'a'
else:
    append_write = 'w'

dbFile = open(filename,append_write)
dbFile.write(line + '\n')
dbFile.close()
