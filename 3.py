"""
Primary reference - http://nedbatchelder.com/text/iter.html

Best way to iterate over a list is to use a simple for loop. Don't use while loops or range()/xrange() if all you 
want to do is do something with the members of a list.

Anytime you want to do something repetitively with something which has data in Python, try and convert it
using any of the techniques in this file to a list or something you can iterate over.
"""

import operator

#Iterate over a list
mylist = ['a', 'b', 'c', 'd']
for letter in mylist:
    print letter

#Iterate over a list and get the index too. The customized index is auto generated as the first argument.

for i,v in enumerate(mylist, start=1):
    print str(i)+':'+str(v)

#Iterate over a string
for c in "Hello":
    print c

#Iterate over a dictionary getting only keys, only values, both or both in sorted form (sorted by key which is default, or by value using itemgetter())
dict1 = {'key1':4, 'key2':2, 'key3':3}
dict2 = {'key1':'40', 'key2':'2', 'key3':'30000'}

print "Keys only"
for key in dict1:
    print key

print "Values only"
for value in dict1.itervalues():
    print value

print "Keys and values"
for key, value in dict1.iteritems():
    print key+':'+str(value)

print "Keys and values sorted by key"
for key, value in sorted(dict1.iteritems()):
    print key+':'+str(value)

print "Keys and values sorted by value"
for key, value in sorted(dict1.items(), key=operator.itemgetter(1)):
    print key+':'+str(value)

print sorted(dict2.items(), key=operator.itemgetter(1), reverse=True)

#Iterate over the lines of a file
filename = 'test'
with open(filename) as f:
    for line in f:
        print repr(line)

#Common operations on a list and dictionary. Only showing that its possible to do a lot of things on an iterable.
mylist = [1,2,3,4]

total = sum(mylist)
smallest = min(dict1.itervalues())
greatest = max(mylist)
joined = ''.join(dict1)

print str(total)+':'+str(smallest)+':'+str(greatest)+':'+str(joined)

#Iterate over multiple lists simultaenously.
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

for i, j in zip(list1, list2):
    print i
    print j

#Create a dict using 2 lists which have keys and values separately
print dict(zip(list1, list2))
