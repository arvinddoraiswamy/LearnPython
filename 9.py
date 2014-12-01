"""
The most common way I have called functions has been when a function has a fixed number of arguments. So the function definition and the place
it is called from have the same number of arguments.

Sometimes though, you have 12 variables and want to pass all of them to a function that then processes it. You could define 12 variables in
both places and that'd work perfectly well. And sometimes that's what you'd want to do. But other times, when you don't care about the order
in which you are processing the arguments and just want to perform similar operations on ALL of the data that is sent - its useful to have
variable sized argument lists.
"""

def function(a, b=2):
    print "This is a", a
    print "This is b", b

def varfunc(a, *varargs, **keypairargs):
    print "This is a", a
    for arg in varargs:
        print "This is a variable argument", arg
    for key in keypairargs.keys():
        print "This is a keypair variable argument", keypairargs[key]

"""
So you can call it as normal and it behaves as expected.
"""
print "Calling as normal"
function(7, 5)
print "\n"

"""
...but you can also call it with a single argument, because 'b' is defined as a function argument.
"""
print "Calling with a single argument"
function(7)
print "\n"

"""
...and you can call it as a key=value pair too
"""
print "Calling with a key=value argument style. Not sure why really"
function(a=1, b=3)
print "\n"

"""
and lastly how about calling a function with a number of arguments < the arguments defined in the function's definition itself
The more the number of variables you want to pass, the more useful this becomes.
"""
print "Calling a function with a variable number of arguments"
varfunc(4, 8, 7, "a", "k", l="9")
