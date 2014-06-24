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
Using map. Performs an operation ONCE on each element. Don't use this to find
out all combinations - each element is touched only once. This will return a list.

Also the number of elements in both lists have to be the same.
"""

def multiply(num1, num2):
    return num1 * num2

def greater(num1):
    if num1 > 3:
        return num1

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

print "\nUsing filter with lambdas\n"
x = list(filter((lambda x: x < 4), i))
print x

print "\nUsing filter with a function\n"
x = list(filter(greater, i))
print x
