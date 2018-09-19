"""
Lists. The Python documentation is pretty cool for this section but I've put this here just for completeness. Not going to add every method here
as that'll take forever - just a few that I didn't know about. Later, as and when I come across things - I will add them in.
"""
l1= [1, 2, 3, 4, 3]

print "Append an element"
l1.append(9)
print l1

print "Add the list to itself"
l1.extend(l1)
print l1

print "Insert an element"
l1.insert(1, 5)
print l1

print "Remove a specific element. Make sure you check for its existence before you remove it though"
if 10 in l1:
    l1.remove(10)
print l1

print "Take the last element off"
l1.pop()
print l1

print "Return first index of specific element. Starts at 1"
print l1.index(9)

print "How many times does 3 appear in the list?"
print l1.count(3)

print "Sort smallest to biggest. For custom sort example look at sorted in 8.py. Remember sort won't return anything :)"
l1.sort()
print l1

print "Reverse a list"
l1.reverse()
print l1

print "Delete specific element from list"
print l1
del(l1[2])
print l1

"""
Queues. Perform operations on either side.
"""
from collections import deque
queue= deque(['a', 'b', 'c'])
queue.appendleft('d')
print "List after appending element at the start"
print queue
print "List after popping the leftmost element"
queue.popleft()
print queue

"""
Tuples. Another way to organize data. You cannot modify a tuple like a list.
"""
t1= (1, 2, 3)
print t1[0]

"""
Sets. Unordered collection of data. If you just want a place to store stuff and not which element goes where, use a set.
"""
set1= set('abcdef')
set2= set('abxtdefg')

#Similar to a set but can't be altered
set3= frozenset('abxtdefg')
l1= ['a','b','b','c']

"""
Elements in both sets
"""
print set1 & set2

"""
Elements in one set but not in the other. It doesn't matter if the first set is smaller.
"""
print set1 - set2

"""
Elements in either set.
"""
print set1|set2

"""
Elements in set1 or set2 but not both
"""
print set1^set2

"""
Remove duplicates from a list
"""
print set(l1)

"""
Is one set a superset of the other?
"""

if set1.issuperset(set2):
    print "Set 1 is a superset"
elif set1.issubset(set2):
    print "Set 1 is a subset"
elif set1.isdisjoint(set2):
    print "Set 1 and Set 2 are totally different"
else:
    print set1.intersection(set2)

"""
String methods.
"""

s1= 'xabcdef'
s2= '41424344'

print "Convert string to sentence case"
print s1.capitalize()

"""
List of all possible encodings IN Python can be found here - https://docs.python.org/2.7/library/codecs.html#standard-encodings
"""
print "Encode a string using a specific encoding algorithm"
print s1.encode('base64')

print "Decode a string using a specific decoding algorithm"
print s2.decode('utf8')

print "Search for the index of a substring inside a string"
if 'cd' in s1:
    print s1.find('cd')

print "Is the string all numbers?"
print s2.isdigit()

print "Pad a string"
print s2.ljust(10,'0')

print "Strip characters from string"
print s1.lstrip('xfe')
print s1.rstrip('xfe')

print "Left Pad a string with a specific character"
s1= 'ab'
print s1.zfill(4)

print "Right Pad a string with a specific character"
s1= 'ab'
print s1.ljust(4,'x')+'ok'
print s1.rjust(4,'x')+'ok'

print "Swap string characters"
a="abc"
b=list(a)
(b[0], b[1]) = (b[1], b[0])
print ''.join(b)

"""
Dictionaries
"""
d1= {'a':1, 'b':2}

print('Print all keys and values')
print d1.keys()
print d1.values()

print('Print value of specific key')
if d1.has_key('a'):
    print d1['a']

print 'You CANNOT look up a key using its value. Do it the long way with the for loop'

print 'Iterate over keys and vaues'
for k1 in d1.iterkeys():
    print d1[k1]
for v1 in d1.itervalues():
    print v1
for (k1, v1) in d1.iteritems():
    print k1, v1

print 'Build dictionary on the fly'
print {x: x**2 for x in (2, 4, 6)}

print 'Clear dictionary'
d1.clear()
print d1.keys()

print 'Add new keys'
d1['c']= 3
d1['d']= 4
print d1.keys()

print 'Delete a key'
del d1['c']
print d1.keys()

print 'Delete a dictionary'
del d1

print 'Substrings with and without steps'
s1= 'abcdef'
print s1[0:2]
print s1[0::2]
print s1[::-2]
