from __future__ import division
"""
If you want to divide floating point numbers, have this at the start of your file
"""
x= 5.2/2
print x


"""
This is just a list of a number of built in functions that Python uses.
"""

l1='abcd'
l2=['a', 'X', 'm', 'd']
l3=''

"""
Check if a string is empty. If it is, it'll return FALSE
"""
print "Check if string is empty"
print any(l3)

"""
Convert integer to binary
"""
print "Convert integer to a binary number"
print bin(10)[2:]

"""
Integer to ASCII
"""
print "Get the ASCII character for a specific number"
print chr(97)

"""
Integer to Hex
"""
print "Get hex representation of a number"
print hex(97)

"""
Integer representation
"""
print "Get integer representation of a string"
print int('a', 16)

"""
ASCII to integer
"""
print "Get integer representation of an ASCII character"
print ord('a')

"""
Convert a list to a byte array
"""
print "Convert a list into a byte array"
print bytearray(l1)

"""
Get all attributes of an object. This is useful in identifying what methods you can call on an object.
"""
print "Get all attributes of a list"
print dir(l1)

"""
Lists all the elements of an iterable WITH a counter. Eliminates the need for a counter completely.
"""
print "List all the elements of an iterable with a counter"
print list(enumerate(l1, start=1))

"""
Get the value of the attribute of an element. Equivalent to obtaining the value of the attribute using object.attribute
"""
print "Value of the attribute of an object"
print getattr(l2, '__class__')

"""
Get representation of an object in memory
"""
print "Representation of an object in memory"
print id(l1)
print id(l2)

"""
Take input from users and display it after stripping new line char if any
"""
print raw_input("Test without new line:")

"""
Print reversed representation of an iterable
"""
print "Reverse the order of the elements in a list"
print list(reversed(l2))

"""
Print sorted version of a list
"""
print "Sort a list - you can pass a function to this to customize your sorting"
print sorted(l2, key=str.lower)

"""
Convert negative numbers to positive
"""
print "Convert all negative results to positive while displaying"
print abs(-4)
