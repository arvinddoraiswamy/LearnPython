"""
This little snippet of code illustrates break and continue. continue is to skip an iteration and break is to
get out of a loop (usually) when a condition has been met. The key here is that break fails when there are
multiple loops to break out of.
"""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['@', '#', '$']

"""
A small snippet of code just to demonstrate 'continue'. You tend to use it when you're processing a huge list
and want to 'do something' on all of them, except a few. In other words, skip iterations but NOT terminate the
entire loop.
"""

for i in list1:
    if i == 2:
        continue
    print "Value of i that is not 2: "+str(i)

"""
Here is how you'd normally write code if you wanted to break out of a loop midway through the iterations.
There's probably many other ways but this is fairly ugly code.
"""

(i, j, k) = ('', '', '')
for i in list1:
    if k == '#':
        break;
    print "Value of i is "+str(i)
    for j in list2:
        if k == '#':
            break;
        print "Value of j is "+j
        for k in list3:
            print "Value of k is "+k
            if k == '#':
                print "Need to stop processing here"
                break;

"""
And since there isn't a better way to break out of a loop - the other option is to try and convert all your loops
into single dimensional loops instead.

The point is, do the calculation somewhere else of the main loop. Use the main loop ONLY for breaking out.
"""
(i, j, k) = ('', '', '')
def get_all_values(l1, l2, l3):
    for i in l1:
        for j in l2:
            for k in l3:
                yield i, j, k

for a, b, c in get_all_values(list1, list2, list3):
    if c == '#':
        print "Found the '#' character, lets get out of the loop now. 'break' will work well here."
        print "Values of a, b and c are "+str(a)+':'+b+':'+c
        break
