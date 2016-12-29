"""
Python is all about iterables. An iterable is effectively a set of values that you repeatedly perform the same
set of operations on. Sometimes you have data lying in multiple places and want them all "together" so you can
run a simple for loop on and run multiple functions on this collated data.

The itertools module helps you do just that. You can run different functions on different pieces of data and get
them into a form that is more easily consumable - and with less code.

I'd recommend clearly understanding what an iterable is and why we use one before trying to jump into itertools.

The following functions will be explored in detail, the list is straight from the Python docs. It has some nice
examples itself, but I'm learning about the module, so I want to go through each of these really slowly and
explain each well.

    count()
    cycle()
    repeat()
    chain()
    compress()
    dropwhile()
    groupby()
    ifilter()
    ifilterfalse()
    islice()
    imap()
    starmap()
    tee()
    takewhile()
    izip()
    izip_longest()
    product()
    permutations()
    combinations()
    combinations_with_replacement()
"""

import itertools

"""
If you want to generate an infinite stream of integers, this is the function to use. Used alone, this won't make
sense. But if you want to generate a bunch of numbers and stop on some other condition later, this can be used.
"""
def i_count():
    """
    count(start, stepsize)
    """
    print "The function being tested is count()\n"
    for i in itertools.count(1,0.5):
        print i
        if i == 5:
            break

"""
Very similar to count() in that continues indefinitely and you have to write code to ensure this doesn't
happen. Its different though, in the sense that in cycle(), you keep going back to the start of the list
instead of incrementing indefinitely.

Allocates a lot of memory though while doing this. (Not sure why and how though)
"""
def i_cycle():
    """
    cycle(iterable)
    """
    print "The function being tested is cycle()\n"
    l1 = ['a', 'b', 'c', 'd']
    for i in itertools.cycle(l1):
        print i

"""
Very similar to cycle() by default except that it doesn't allocate a lot of memory and repeats the object multiple
times. You can though specify the number of times that you want stuff to repeat.
"""
def i_repeat():
    """
    repeat(object, step)
    """
    print "The function being tested is repeat()\n"
    l1 = ['a', 'b', 'c', 'd']
    for i in itertools.repeat(l1, 2):
        print i

"""
Join multiple objects together so you can perform a single operation on a single list. Instead of doing
the operations on multiple lists.
"""
def i_chain():
    """
    chain(object1, object2)
    """
    print "The function being tested is chain()\n"
    l1 = ['a', 'b', 'c']
    l2 = ['d', 'e', 'f']

    l3 = list(itertools.chain(l1, l2))
    print l3

"""
Extract specific strings from a list and create another list.
"""
def i_compress():
    """
    compress(object1)
    """
    print "The function being tested is compress()\n"
    l1 = ['a', 'b', 'c']
    #l2 = list(itertools.compress(l1, [1, 1, 0]))
    l2 = list(itertools.compress(l1, [1, 1, 0]))
    print l2

"""
Read through a list, perform an operation on every member of the list and see if the result of that operation is true. If it is true, ignore that
result. When an operation returns false, return that value. The entire list is iterated over in this way.
"""
def i_dropwhile():
    """
    dropwhile(condition_to_drop, object)
    """
    print "The function being tested is dropwhile()\n"
    l1 = [1, 2, 4, 8, 10, 3]
    l2 = itertools.dropwhile(lambda x:x<5, l1)
    print list(l2)

"""
Look at an entire string of data. Split it internally into multiple bits of similarly grouped characters. Each group is assigned a key that is 
then returned. By default, each character is treated as a group - if the next character is different, a new group starts. 

You can however define a function instead, which changes the way the grouping is done. Remember groupby.
"""
def i_groupby():
    """
    groupby(object, key=keyfunc)
    """
    print "The function being tested is groupby()\n"
    l1='AABAABBCXCDDDYD'
    l2=[k for k,g in itertools.groupby(l1, key=keyfunc)]
    print l2

def keyfunc(l1):
    """
    Splitter function to customize the results of groupby. This splits a group up and then runs keyfunc on each split up part.
    """
    l1=l1+'B'
    return l1

"""
Study a list of elements. Pass each element to a function. If the function then returns True, the element is returned.
"""
def i_filter():
    """
    ifilter(function, object)
    """
    print "The function being tested is ifilter()\n"
    l1 = [1, 2, 4, 8, 10, 3]
    l2 = itertools.ifilter(lambda x:x<5, l1)
    print list(l2)
    
"""
Study a list of elements. Pass each element to a function. If the function then returns False, the element is returned. Its basically the
inverse of ifilter()
"""
def i_filterfalse():
    """
    ifilterfalse(function, object)
    """
    print "The function being tested is ifilterfalse()\n"
    l1 = [1, 2, 4, 8, 10, 3]
    l2 = itertools.ifilterfalse(lambda x:x<5, l1)
    print list(l2)

"""
Split a list of elements up into smaller parts. Looks very very similar to python slicing.
"""
def i_slice():
    """
    Single argument - itertools(lastelement)
    Two arguments   - itertools(startelement, lastelement)
    Three arguments - itertools(startelement, lastelement, stepsize)
    """
    l1= [1, 2, 4, 8, 10, 3]
    print "The function being tested is itertools() with a single argument"
    l2= itertools.islice(l1, 2)
    print list(l2)
    print "The function being tested is itertools() with 2 arguments"
    l2= itertools.islice(l1, 2, 4)
    print list(l2)
    print "The function being tested is itertools() with 3 arguments"
    l2= itertools.islice(l1, 2, 6, 2)
    print list(l2)
    
"""
Performs an operation ONCE on each element. Don't use this to find out all combinations - each element is touched only once. 
This will return a list. If the number of elements in both lists have to be the same, the function stops when the length of the shorter list
is reached. THAT is the only difference between imap and map.
"""
def i_imap():
    """
    imap(function, list1, list2, list3)
    """
    l1= [1, 2, 4, 8, 10, 3]
    l2= [4, 5, 3, 8, 1,]
    l3= itertools.imap(multiply, l1, l2)
    print list(l3)

def multiply(num1, num2):
    return num1 * num2

"""
Very similar to imap. Only this works on tuples instead. It internally splits the tuple into its individual members and passes each as arguments
to a function that then acts on them. Secondly, you can only pass a single list to it.
"""
def i_starmap():
    """
    starmap(function, list)
    """
    l1= [(1,2), (3,4), (5,6)]
    l2= itertools.starmap(multiply, l1)
    print list(l2)

"""
https://stackoverflow.com/questions/1271320/reseting-generator-object-in-python
http://discontinuously.com/2012/06/inside-python-tee/

You have a list that you want to perform some operations on. The operations that are performed are dependent on the value of each list member.
Suppose you want to start iterating through the list, and stop halfway - but start a new loop from where the first loop stopped tee() is a
useful function to use.

If you use a normal list, it'll work and you can add additional conditions to ensure it picks up where the first list left off. But there is
a lot of needless processing of the first few numbers. The more you process the first time around, the less useful this is.

tee() internally maintains a cache of the numbers - so if its a huge huge list, it might not be the best thing to use. Maybe :)
"""
def i_tee():
    l1= [1, 2, 4, 8, 10, 3, 9]
    t1,t2= itertools.tee(l1)

    for i in t1:
        if i<3:
            print i
        elif i==4 or i==9:
            print "A"+str(i)
            for i in t2:
                print "Now processing t2: "+str(i)
        else:
            print "something else: "+str(i)

"""
Processes a list and returns element until an element is False. The moment it finds a "False" element, it'll terminate. This is unlike ifilter
which continues to return "True" elements throughout the list.
"""
def i_takewhile():
    l1= [1, 2, 4, 8, 10, 3, 9]
    l2= itertools.takewhile(lambda x:x<6, l1)
    print list(l2)

"""
Takes list1 and list2. Combines their elements together. Ends when the length of the shortest list is reached. Returns a list of tuples.
"""
def i_izip():
    l1= [1, 2, 4, 8, 10, 3, 9]
    l2= ['d', 'e', 'f']
    l3= itertools.izip(l1, l2)
    print list(l3)

"""
Takes list1 and list2. Combines their elements together. Ends when the length of the longer list is reached. Gaps created because of a shorter
list are filled up with the 'fillvalue' character. Returns a list of tuples.
"""
def i_izip_longest():
    l1= [1, 2, 4, 8, 10, 3, 9]
    l2= ['d', 'e', 'f']
    l3= itertools.izip_longest(l1, l2, fillvalue='-')
    print list(l3)

"""
Compute all possible combinations that are possible. If you want to crack passwords and try every_single_letter this is what you need to take
a look at.
"""
def i_product():
    l1= [1, 2, 9]
    l2= ['d', 'e', 'f']

    l3= itertools.product(l1, l2)
    print list(l3)

"""
Compute all possible combinations where a result does not have all similar characters. 
"""
def i_permutations():
    l1= [1, 2, 9]
    l2= itertools.permutations(l1, 2)
    print list(l2)

"""
Computes all possible combinations where the result of any combination does not contain the exact same elements of a result previously computed.
If you just want all unique combinations, but the order of the combination does not matter - this is what you need.
"""
def i_combinations_with_replacement():
    l1= [1, 2, 9]
    l2= itertools.combinations_with_replacement(l1, 3)
    print list(l2)

"""
Similar to combinations_with_replacement but also excludes results where ANY element of a result is repeated even a single time.
"""
def i_combinations():
    l1= [1, 2, 9]
    l2= itertools.combinations(l1, 3)
    print list(l2)

if __name__ == "__main__":
    #i_count()
    #i_cycle()
    #i_repeat()
    #i_chain()
    #i_compress()
    #i_dropwhile()
    #i_groupby()
    #i_filter()
    #i_filterfalse()
    #i_slice()
    #i_imap()
    #i_starmap()
    #i_tee()
    #i_takewhile()
    #i_izip()
    i_izip_longest()
    #i_product()
    #i_permutations()
    #i_combinations_with_replacement()
    #i_combinations()
