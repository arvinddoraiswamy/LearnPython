"""
http://nedbatchelder.com/text/iter.html

The function hello_world() isn't executed completely before the for loop runs, because of the yield statements
in the hello_world() function. Each time it hits a "yield" it "returns" control to the for loop, which does
something with the "returned value".

You'll notice that the "Inside iterator" message is printed twice inbetween "Hello" and "World", showing that
it returns control twice. Also note that Hello and World are printed separately - not together as they would have
had it been a single function returning after a single call.

Also ABCD is printed just once - as earlier mentioned, control is transferred back ONLY WHEN it sees a yield.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def hello_world():
    yield "Hello"
    yield "World"
    print "ABCD"
    yield "Nothere"

for x in hello_world():
    print "Inside iterator"
    print x


"""
Here is a slightly more complex example written with the help of a generator.
"""
def odd(stream):
    for n in stream:
        if n%2 != 0:
            yield n

for i in odd(numbers):
    print str(i)+" is odd"

"""
Just to demonstrate why a generator is a bit more efficient and IMO clean, here is how I'd write it using
normal functions. Its 7 lines here vs 4 lines for a generator :).
"""
def funcodd(stream):
    odd_list = []
    for n in stream:
        if n%2 != 0:
            odd_list.append(n)

    return odd_list

for i in funcodd(numbers):
    print str(i)+" is odd"
