import os
"""
Opening and transparently closing a file
"""
file_path = '/etc/passwd'
print "Does file exist at all?"
if os.path.exists(file_path):
    print "File exists"
else:
    print "File does not exist"

print "Open a file. Since you use 'with' you don't need to explicitly close it with f.close()"
with open('foo.txt') as f:
    print "The file descriptor for this file is", f.fileno()
    for line in f:
        print line

print "Reading a certain number of bytes from the file"
with open('foo.txt') as f:
    s1= f.read(6)
    print s1
    print "Read all the data from a file - note that the file pointer position is remembered here"
    s2=f.read()
    print s2

print "Reading a certain number of lines from the file"
with open('foo.txt') as f:
    s1= f.readline()
    print s1
    print "Current file position is", f.tell()
    print "Move file position by 7", f.seek(7, os.SEEK_CUR)
    print "Read the rest of the lines. Note that the file pointer position is remembered here"
    s2= [x for x in f.readlines()]
    for i in s2:
        print i

print "Read whole file as lines but without the extra newline character that readlines() gives you"
with open('foo.txt') as f:
    x= f.read().splitlines()
print x
print

print "Writing a certain number of lines to a file"
with open('blah.txt', 'w') as f:
    f.write('abcd')
    print "Reduce file size to the number inside the brackets. Here there will be only 1 character remaining."
    f.truncate(1)

l1=['a', 'b', 'c']
with open('blah.txt', 'a') as f:
    print "Write a sequence of strings to the file. Make sure that you close any previous handles before writing content"
    f.writelines(l1)

