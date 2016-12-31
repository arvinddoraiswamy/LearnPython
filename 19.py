import collections

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
