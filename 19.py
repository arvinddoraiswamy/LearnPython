import collections
''' Deque, Counter, Ordered Dict, Named Tuple, DefaultDict '''

print 'Rotate left or right using a collection'
l1= '616345622222'
c1= collections.deque(l1)

print 'Collection rotated 3 places to the left'
c1.rotate(-3)
print c1

print 'Collection rotated 3 places to the right, back to its original postion'
c1.rotate(3)
print c1

t1= list(l1)
count_dict= collections.Counter(t1)
print 'Counts number of times an item occurs in a list'
print count_dict.items()

print 'Get 2 most common'
common= count_dict.most_common(2)
print common

print 'Now to sort this dictionary, best to use OrderedDict in reverse order'
count= collections.OrderedDict(sorted(count_dict.items(), reverse=True))
print count

print 'A Named Tuple is nice if you have a huge list of values and do not remember the indices'
t1= collections.namedtuple('test', 'name age height') #The name here is not important
bob= t1(name='Bob', age=30, height=7)
print bob.name, bob.age, bob.height

print 'You can even convert a named tuple to a dictionary'
print bob._asdict().keys()

print 'Assign default values to dictionary keys so you do not get non-existent key errors'
def default_factory():
    return 'default value'

d1 = collections.defaultdict(default_factory, foo='123')
print 'd1:', d1
print 'foo =>', d1['foo']
print 'bar =>', d1['bar']
print d1['a']
