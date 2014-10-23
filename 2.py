"""
Iterables - http://nedbatchelder.com/text/iter.html
"""

i = [4, 2, 3, 5, 6]
j = [5, 2, 1, 4, 7]

"""
Using map. Performs an operation ONCE on each element. Don't use this to find
out all combinations - each element is touched only once. This will return a list.

Also the number of elements in both lists have to be the same.
"""

def multiply(num1, num2):
    return num1 * num2

print "Using map with a previously defined function\n"
x = map(multiply, i, j)
print x

print "\nUsing map with lambdas\n"
x = map(lambda x1, y1: x1 * y1, i, j)
print x

"""
Using reduce. Operates best when you want just ONE value to be returned from
operations performed on a SINGLE LIST.

Remember, although it looks like a single argument is being passed to the function, internally PAIRS
of arguments are passed.
"""

print "\nUsing reduce with functions\n"
product = reduce(multiply, i)
print product

print "\nUsing reduce with lambdas\n"
product = reduce(lambda x, y: x * y, [6,2,6])
print product

"""
Using filter. Runs a function against each element and returns True only if
there is a match. So if you have a big list and want to process only
PART of it based on some condition - filter is the way to go.
"""

def greater(num1):
    if num1 > 3:
        return num1

print "\nUsing filter with lambdas\n"
x = list(filter((lambda x: x < 4), i))
print x

print "\nUsing filter with a function\n"
x = list(filter(greater, i))
print x

"""
Range - The last number is ignored but the first IS used. Remember :). Also use range if you actually want to generate a new list of
numbers from the original list.
"""

print "Simple usage of range:\n"
for i in range(0,4):
    print i

"""
XRange - Same as range but better performance wise while iterating through large lists.

python -m timeit 'for i in range(1000000):' ' pass'
10 loops, best of 3: 24.2 msec per loop

python -m timeit 'for i in xrange(1000000):' ' pass'
100 loops, best of 3: 11.6 msec per loop
"""

print "Simple usage of xrange. Xrange though apparently is NOT there in Python 3 so use range:\n"
for i in xrange(0,4):
    print i
