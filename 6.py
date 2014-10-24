#https://stackoverflow.com/questions/2776829/difference-between-python-generators-vs-iterators
#http://www.diveintopython3.net/iterators.html

list1 = ['a', 'b', 'c', 'd']

"""
Iterating through that list is easily done of course. But say you wanted to print only 'c' in that list?
And without using a loop? I'm not sure why you'd want to do it - but I guess it couldn't hurt to know :D

Note that the counter is preserved internally and it correctly moves to the next object. 'next' is the ONLY
method that the iterator has.
"""

iterator = iter(list1)
iterator.next()
iterator.next()
print iterator.next()

"""
Writing your own custom iterators is so you can iterate through them and perform whatever operations you want to
on them. Its a good idea to read the stack overflow thread that I refer to at the top - to understand why one
would need to even use custom iterators.

To understand custom iterators though, we first need to understand classes. If you have a simple program, then
you can probably write clean code - just using modules and importing them. Classes are apparently the OOP way
of doing things - I am unclear yet, as to what advantages they offer. So please help :)

All the same, here is a code snippet that shows how to define classes AND custom iterators.
"""

class Test:
    """
    This is how a class is defined along with its methods. The first 3 methods are compulsory
    if you want to create your own iterator. All the fancy filtering logic should go into the next() method.
    """
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def next(self):
        fib = self.number
        fib += 2
        self.number = fib
        if fib >= 15:
            raise StopIteration

        return fib

    """
    Since this is a class, you can, in addition to the 3 "iterator" methods, also define additional methods.
    These methods can be invoked by an object as usual.
    """
    def additionalmethod(self):
        print "You can define additional methods here and call that normally"

for i in Test(1):
    print i

t1 = Test(0)
t1.additionalmethod()
