i = [4, 2, 3, 5, 6]
j = [5, 2, 1, 4, 7]

"""
Using for loops to perform operations. This is the usual stuff. Multiplies
every number by every other number and prints a result out.
"""

for c1 in range(0, len(i)):
   for c2 in range(0, len(j)):  
       print i[c1] * j[c2]


"""
Doing the same multiplication above but with list comprehensions instead.
"""
print "\nMultiplication using list comprehensions\n"
result = [x1 * y1 for x1 in i for y1 in j]
print result


"""
Using dictionary comprehensions to do the same thing as above but with a dictionary instead.
"""
print "Creating a new dictionary\n"
d1= {'a':1, 'b':2, 'c':3}
d2= {key: key+str(value) for key, value in d1.items()}
print d2.keys()
